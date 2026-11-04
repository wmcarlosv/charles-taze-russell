#!/usr/bin/env python3
# Relaciona las voces del índice temático con los capítulos del Foto-Drama.
# Uso: python3 indexar-fotodrama.py [--dry]
import os, re, sqlite3, sys, unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, 'biblioteca.db')
OBRA = 'Foto-Drama de la Creación'


def norm(s):
    s = unicodedata.normalize('NFD', s or '')
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower()
    return re.sub(r'\s+', ' ', s).strip()


def norm_con_mapa(texto):
    out, mapa = [], []
    for i, ch in enumerate(texto):
        base = unicodedata.normalize('NFD', ch)
        base = ''.join(c for c in base if unicodedata.category(c) != 'Mn').lower()
        for b in base:
            out.append(b); mapa.append(i)
    return ''.join(out), mapa


def termino_busqueda(t):
    t = (t or '').strip()
    # ACCIÓN(ES) -> ACCIÓN ; BESTIA(S) -> BESTIA ; COMER(-IDO/-IENDO) -> COMER
    t = re.sub(r'\([^)]*\)', '', t).strip(' ,;')
    # ANTONIO, MARCOS -> ANTONIO ; ANTIOQUIA, IGLESIA DE -> ANTIOQUIA
    if ',' in t:
        t = t.split(',')[0].strip()
    return t


def contexto(texto, ini, fin):
    a = max(texto.rfind('.', 0, ini), texto.rfind('!', 0, ini), texto.rfind('?', 0, ini),
            texto.rfind('\n\n', 0, ini))
    a = a + 1 if a >= 0 else max(0, ini - 80)
    fines = [x for x in (texto.find('.', fin), texto.find('!', fin), texto.find('?', fin),
                         texto.find('\n\n', fin)) if x != -1]
    b = min(fines) + 1 if fines else min(len(texto), fin + 120)
    return re.sub(r'\s+', ' ', texto[a:b]).strip()[:320]


def main():
    dry = '--dry' in sys.argv
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    pags = []
    for f in con.execute('SELECT id, pagina, titulo, texto FROM paginas WHERE titulo_obra=? ORDER BY pagina', (OBRA,)):
        n, mapa = norm_con_mapa(f['texto'])
        pags.append({'id': f['id'], 'pagina': f['pagina'], 'titulo': f['titulo'],
                     'texto': f['texto'], 'norm': n, 'mapa': mapa})
    temas = con.execute('SELECT id, termino_es, termino FROM temas ORDER BY id').fetchall()
    filas = []
    con_match = 0
    for t in temas:
        cand = termino_busqueda(t['termino_es'] or t['termino'])
        cn = norm(cand)
        if len(cn) < 2:
            continue
        patron = re.compile(r'(?<![a-z0-9])' + re.escape(cn) + r'(?![a-z0-9])')
        mejores = []
        for p in pags:
            posiciones = [m.start() for m in patron.finditer(p['norm'])]
            if not posiciones:
                continue
            # ¿aparece en un título/caption del capítulo?
            titulo_n = norm(p['titulo'])
            en_titulo = bool(re.search(r'(?<![a-z0-9])' + re.escape(cn) + r'(?![a-z0-9])', titulo_n))
            cabecera = 0
            for pos in posiciones[:1]:
                ini_orig = p['mapa'][pos]
                bloque = p['texto'][p['texto'].rfind('\n\n', 0, ini_orig) + 2:ini_orig + 40]
                if bloque.lstrip().startswith('## '):
                    cabecera = 1
                    break
            score = len(posiciones) + (5 if en_titulo else 0) + (3 if cabecera else 0)
            mejores.append((score, len(posiciones), en_titulo or cabecera, p, posiciones[0]))
        if not mejores:
            continue
        # Para términos muy cortos: evitar palabras vacías y, si no hay
        # título ni varias apariciones, conservar al menos la mejor página.
        if len(cn) <= 3:
            if cn in {'dos', 'fin', 'ave', 'hoz', 'uno', 'ser', 'ver', 'dar', 'tan', 'tal', 'mas', 'sus', 'mis', 'tuy', 'aun'}:
                continue
            fuertes = [x for x in mejores if x[2] or x[1] >= 2]
            if fuertes:
                mejores = fuertes
        mejores.sort(key=lambda x: (-x[0], x[3]['pagina']))
        con_match += 1
        for score, cuenta, fuerte, p, pos in mejores[:3]:
            ini_orig = p['mapa'][pos]
            fin_orig = p['mapa'][min(pos + len(cn) - 1, len(p['mapa']) - 1)] + 1
            term = p['texto'][ini_orig:fin_orig]
            filas.append((t['id'], p['id'], ini_orig, term, contexto(p['texto'], ini_orig, fin_orig), score))
    print('términos con coincidencia:', con_match, 'de', len(temas), '| enlaces:', len(filas))
    if dry:
        for f in filas[:12]:
            print(f[0], f[2], repr(f[3]), '|', f[4][:90])
        return
    con.execute('''CREATE TABLE IF NOT EXISTS temafoto(
        tema_id INTEGER NOT NULL, pid INTEGER NOT NULL, pos INTEGER NOT NULL,
        term TEXT, ctx TEXT, score REAL DEFAULT 0,
        PRIMARY KEY(tema_id, pid))''')
    con.execute('DELETE FROM temafoto')
    con.executemany('INSERT INTO temafoto(tema_id,pid,pos,term,ctx,score) VALUES (?,?,?,?,?,?)', filas)
    con.execute('CREATE INDEX IF NOT EXISTS ix_temafoto ON temafoto(tema_id)')
    con.commit()
    print('guardados', con.execute('select count(*) from temafoto').fetchone()[0])
    con.close()


if __name__ == '__main__':
    main()
