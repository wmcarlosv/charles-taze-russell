#!/usr/bin/env python3
"""Traduce The Watch Tower (1879-1916) al español y guarda el resultado.

- Usa el mismo caché que la biblioteca inglesa (tabla traducciones), de modo
  que las traducciones ya hechas se reutilizan y no se repiten.
- Guarda cada número traducido en la tabla `torre_es` para poder insertarlo
  después en la biblioteca española sin volver a traducir.
- Se puede interrumpir y volver a empezar: lo traducido queda guardado.
"""
import hashlib
import json
import os
import re
import sqlite3
import sys
import time
import urllib.parse
import urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, 'biblioteca.db')
LOG = '/tmp/opencode/torre.log'

MESES = {1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
         7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre',
         12: 'diciembre'}
MES_EN = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
           'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11,
           'december': 12}


def log(msg):
    linea = time.strftime('%H:%M:%S ') + msg
    print(linea, flush=True)
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(linea + '\n')


def google(texto):
    """Traduce un bloque de hasta ~4000 caracteres con dos servicios."""
    q = urllib.parse.quote(texto)
    fuentes = (
        ('https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=es&q=' + q, 'lista'),
        ('https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=es&dt=t&q=' + q, 'gtx'),
    )
    ultimo = ''
    for intento in range(4):
        for url, tipo in fuentes:
            try:
                d = json.load(urllib.request.urlopen(url, timeout=60))
                if tipo == 'lista':
                    return ''.join(x for x in d if isinstance(x, str)).strip()
                return ''.join(x[0] for x in d[0] if x and x[0]).strip()
            except Exception as e:
                ultimo = e
        espera = 30 * (intento + 1)
        log('  aviso: %s; espero %ds' % (ultimo, espera))
        time.sleep(espera)
    return ''


def traducir_lote(parrafos):
    """Traduce varios párrafos juntos usando marcas que el traductor respeta."""
    marcas = ['@@%d@@' % (i + 1) for i in range(len(parrafos))]
    texto = '\n\n'.join(m + '\n' + p for m, p in zip(marcas, parrafos))
    salida = google(texto)
    if salida:
        pos = [salida.find(m) for m in marcas]
        if all(p >= 0 for p in pos) and pos == sorted(pos):
            partes = []
            for i, p in enumerate(pos):
                ini = p + len(marcas[i])
                fin = pos[i + 1] if i + 1 < len(pos) else len(salida)
                partes.append(salida[ini:fin].strip())
            if len(partes) == len(parrafos) and all(partes):
                return partes
    # Si las marcas no sobreviven, se traduce párrafo por párrafo.
    return [google(p) for p in parrafos]


ABREV = re.compile(r'\b(?:[A-ZÁÉÍÓÚÑ][a-záéíóúñ]{0,5}|[A-Z]{1,3})\.$')


def unir_cortes(parrafos):
    """Vuelve a unir párrafos que el traductor cortó dentro de una cita."""
    out = []
    for p in parrafos:
        if out and ((OUT_ABREV(out[-1]) and re.match(r'^\d{1,3}[:.,]', p)) or p[:1].islower()):
            out[-1] = out[-1] + ' ' + p
        else:
            out.append(p)
    return out


def OUT_ABREV(p):
    return bool(ABREV.search(p.strip()))


def crear_tabla(con):
    con.execute('''CREATE TABLE IF NOT EXISTS torre_es(
        id INTEGER PRIMARY KEY, orden INTEGER, titulo TEXT, anio INTEGER,
        mes INTEGER, texto TEXT)''')
    con.commit()


def main():
    con = sqlite3.connect(DB, timeout=60)
    con.execute('PRAGMA journal_mode=WAL')
    crear_tabla(con)
    oid = con.execute("select id from obras where titulo='The Watch Tower'").fetchone()[0]
    paginas = con.execute(
        'select id, orden, titulo, texto from paginas where obra_id=? order by orden',
        (oid,)).fetchall()
    log('números a traducir: %d' % len(paginas))

    hechos = {r[0] for r in con.execute('select orden from torre_es')}
    for n, (pid, orden, titulo, texto) in enumerate(paginas, 1):
        if orden in hechos:
            continue
        m = re.search(r'— (\w+) (\d{4})$', titulo)
        mes = MES_EN.get(m.group(1).lower(), 0) if m else 0
        anio = int(m.group(2)) if m else 0
        nombre_es = 'La Torre del Vigía — %s de %s' % (MESES.get(mes, ''), anio)

        parrafos = [p.strip() for p in texto.split('\n\n') if p.strip()]
        salida, lote, chars = [], [], 0
        for p in parrafos:
            h = hashlib.sha256(p.encode('utf-8')).hexdigest()
            fila = con.execute('select texto_es from traducciones where hash=?', (h,)).fetchone()
            if fila and fila[0]:
                salida.append(fila[0])
                continue
            if lote and (chars + len(p) > 3600 or len(lote) >= 8):
                trad = traducir_lote(lote)
                for orig, esp in zip(lote, trad):
                    if esp:
                        hh = hashlib.sha256(orig.encode('utf-8')).hexdigest()
                        con.execute('insert or replace into traducciones(hash,texto_en,texto_es) '
                                    'values (?,?,?)', (hh, orig, esp))
                        salida.append(esp)
                    else:
                        salida.append('')
                con.commit()
                lote, chars = [], 0
            lote.append(p)
            chars += len(p)
        if lote:
            trad = traducir_lote(lote)
            for orig, esp in zip(lote, trad):
                if esp:
                    hh = hashlib.sha256(orig.encode('utf-8')).hexdigest()
                    con.execute('insert or replace into traducciones(hash,texto_en,texto_es) '
                                'values (?,?,?)', (hh, orig, esp))
                    salida.append(esp)
                else:
                    salida.append('')
            con.commit()
        idioma = 'es' if len(salida) == len(parrafos) else 'parcial'
        cuerpo = '\n\n'.join(unir_cortes([x for x in salida if x]))
        con.execute('insert or replace into torre_es(orden,titulo,anio,mes,texto) values (?,?,?,?,?)',
                    (orden, nombre_es, anio, mes, cuerpo))
        con.commit()
        log('[%d/%d] %s  %d párrafos  %d caracteres  %s' %
            (n, len(paginas), nombre_es, len(parrafos), len(cuerpo), idioma))
    log('terminado')


if __name__ == '__main__':
    main()
