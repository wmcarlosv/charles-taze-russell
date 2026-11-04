#!/usr/bin/env python3
# Carga el libro «Foto-Drama de la Creación» desde el PDF a la biblioteca.
# Uso:
#   python3 cargar-fotodrama.py --dry    # solo muestra lo que haría
#   python3 cargar-fotodrama.py          # inserta en biblioteca.db
import os, re, sqlite3, subprocess, sys, shutil, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, 'biblioteca.db')
PDF = '/home/carlos/Desktop/SpanishPhotoDrama.pdf'
OBRA = 'Foto-Drama de la Creación'
VOLUMEN = 0
LAYOUT = '/tmp/opencode/fdrama-layout.txt'
IMG_SRC = '/tmp/opencode/fdall'
IMG_LIST = '/tmp/opencode/fdimg-list.txt'
IMG_DIR = os.path.join(BASE, 'img')

sys.path.insert(0, BASE)
import pdf_vol


def texto_layout():
    if not os.path.exists(LAYOUT):
        d = subprocess.run(['pdftotext', '-layout', PDF, '-'], capture_output=True)
        open(LAYOUT, 'wb').write(d.stdout)
    return open(LAYOUT, encoding='utf-8', errors='replace').read().split('\f')


def mapa_imagenes():
    """Devuelve {pagina_pdf: [(archivo_origen, nombre_destino), ...]}."""
    if not os.path.exists(IMG_LIST) or not os.path.isdir(IMG_SRC):
        os.makedirs(IMG_SRC, exist_ok=True)
        with open(IMG_LIST, 'w', encoding='utf-8') as f:
            subprocess.run(['pdfimages', '-list', PDF], stdout=f, check=False)
        subprocess.run(['pdfimages', '-png', PDF, os.path.join(IMG_SRC, 'im')],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    filas = []
    for ln in open(IMG_LIST, encoding='utf-8', errors='ignore'):
        p = ln.split()
        if len(p) >= 16 and p[0].isdigit() and p[1].isdigit() and p[2] == 'image':
            filas.append({'pg': int(p[0]), 'w': int(p[3]), 'h': int(p[4]), 'color': p[5]})
    mapa, cuenta = {}, {}
    for i, f in enumerate(filas):
        if f['w'] == 621 and f['h'] == 1220:   # fondo decorativo de la página
            continue
        pg = f['pg']
        cuenta[pg] = cuenta.get(pg, 0) + 1
        destino = 'fotodrama-%03d-%d.png' % (pg, cuenta[pg])
        mapa.setdefault(pg, []).append(('im-%03d.png' % i, destino))
    return mapa


def lineas(texto):
    ls = texto.split('\n')
    while ls and (not ls[-1].strip() or re.fullmatch(r'\d{1,3}', ls[-1].strip())):
        ls.pop()
    return ls


def es_titulo(s, maxlen=150):
    letras = [c for c in s if c.isalpha()]
    if len(letras) < 2 or len(s) > maxlen:
        return False
    return all(c.isupper() or not c.isalpha() for c in s)


def unir(buf):
    t = ' '.join(buf)
    t = re.sub(r'-\s+([a-záéíóúñ])', r'\1', t)   # palabra partida al final de línea
    return re.sub(r'\s+', ' ', t).strip()


def parrafos(ls, sangria=True):
    out, buf = [], []
    for raw in ls:
        s = raw.rstrip()
        if not s.strip():
            if buf:
                out.append(unir(buf)); buf = []
            continue
        lead = len(s) - len(s.lstrip(' '))
        txt = s.strip()
        if sangria and lead >= 2 and buf:
            out.append(unir(buf)); buf = []
        buf.append(txt)
    if buf:
        out.append(unir(buf))
    return [x for x in out if x]


def cuerpo_pagina(texto, quitar_titulo=True):
    ls = lineas(texto)
    titulo = None
    if quitar_titulo:
        for i, raw in enumerate(ls):
            s = raw.strip()
            if not s:
                continue
            if es_titulo(s, 100):
                titulo = re.sub(r'\s+', ' ', s).rstrip('.').strip()
                del ls[i]
            break
    return titulo, parrafos(ls)


def cuerpo_sin_primera(texto):
    ls = lineas(texto)
    for i, raw in enumerate(ls):
        if raw.strip():
            del ls[i]
            break
    return parrafos(ls)


def capturas(texto):
    return [re.sub(r'\s+', ' ', s).strip() for s in (l.strip() for l in lineas(texto))
            if s and es_titulo(s, 200)]


def bloques_lineas(texto):
    """Conserva los grupos separados por líneas en blanco (portada, créditos)."""
    return parrafos(lineas(texto), sangria=False)


def componer():
    pags = texto_layout()
    imgs = mapa_imagenes()
    caps = []

    def img_blocks(pg):
        return ['[[img:%s]]' % d for _, d in imgs.get(pg, [])]

    # 1. Presentación: portada y créditos
    bl = img_blocks(1) + bloques_lineas(pags[2]) + bloques_lineas(pags[3])
    caps.append({'titulo': 'Presentación', 'pdf': 3, 'bloques': bl})

    # 2. Prólogo (páginas 5-6)
    t, b = cuerpo_pagina(pags[4] + '\n\n' + pags[5])
    caps.append({'titulo': t or 'Prólogo', 'pdf': 5, 'bloques': b})

    # 3. Derechos y propósito (página 7)
    caps.append({'titulo': 'Derechos y propósito', 'pdf': 7,
                 'bloques': bloques_lineas(pags[6])})

    # 4. Lecciones: página de texto + página de ilustraciones
    n = 0
    for p in range(8, 199, 2):
        n += 1
        t, b = cuerpo_pagina(pags[p - 1])
        bl = img_blocks(p) + b
        i = p + 1
        cs = capturas(pags[i - 1])
        ims = [d for _, d in imgs.get(i, [])]
        for k in range(max(len(cs), len(ims))):
            if k < len(ims):
                bl.append('[[img:%s]]' % ims[k])
            if k < len(cs):
                bl.append('## ' + cs[k])
        caps.append({'titulo': t or ('Lección %d' % n), 'pdf': p, 'bloques': bl})

    # 5. Apéndice
    caps.append({'titulo': 'El sello de nuestra asociación', 'pdf': 200,
                 'bloques': img_blocks(200) + cuerpo_sin_primera(pags[199])})
    caps.append({'titulo': 'Hijos de Paz', 'pdf': 201,
                 'bloques': img_blocks(201) + cuerpo_sin_primera(pags[200])})
    caps.append({'titulo': 'Literatura', 'pdf': 202,
                 'bloques': img_blocks(202) + cuerpo_sin_primera(pags[201])})
    return caps, imgs


def main():
    dry = '--dry' in sys.argv
    caps, imgs = componer()
    total_citas = 0
    for c in caps:
        texto = '\n\n'.join(c['bloques'])
        c['texto'] = texto
        c['citas'] = pdf_vol.extrae(texto)
        total_citas += len(c['citas'])
    print('capítulos:', len(caps), 'citas:', total_citas,
          'imágenes:', sum(len(v) for v in imgs.values()))
    if dry:
        for c in caps[:3]:
            print('\n===', c['titulo'], '(pdf', c['pdf'], ') ===')
            print(c['texto'][:1200])
        print('\n--- últimos ---')
        for c in caps[-3:]:
            print(c['titulo'], '|', len(c['texto'].split()), 'palabras |', len(c['citas']), 'citas')
        print('\n--- muestra citas lección 1 ---')
        for x in caps[3]['citas'][:12]:
            print(x[2], '->', x[3], x[4], x[5], x[6])
        return

    # Respaldo de la base
    carpeta = os.path.join(BASE, 'respaldos')
    os.makedirs(carpeta, exist_ok=True)
    destino = os.path.join(carpeta, 'biblioteca-antes-fotodrama-%s.db' % datetime.date.today().isoformat())
    if not os.path.exists(destino):
        o = sqlite3.connect(DB); d = sqlite3.connect(destino)
        o.backup(d); d.close(); o.close()
        print('respaldo:', destino)

    # Copiar ilustraciones
    os.makedirs(IMG_DIR, exist_ok=True)
    copiadas = 0
    for pg, lista in imgs.items():
        for origen, nombre in lista:
            shutil.copy2(os.path.join(IMG_SRC, origen), os.path.join(IMG_DIR, nombre))
            copiadas += 1
    print('imágenes copiadas:', copiadas)

    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    viejos = [r['id'] for r in con.execute('select id from paginas where titulo_obra=?', (OBRA,))]
    for pid in viejos:
        con.execute('delete from citas where pagina_id=?', (pid,))
        con.execute('delete from busqueda where rowid=?', (pid,))
        con.execute('delete from paginas where id=?', (pid,))
    con.commit()
    print('páginas anteriores borradas:', len(viejos))

    for i, c in enumerate(caps, 1):
        cur = con.execute(
            'insert into paginas (obra,volumen,titulo_obra,pagina,pagina_pdf,titulo,texto,idioma,indice,original,resumen) '
            'values (?,?,?,?,?,?,?,?,?,?,?)',
            (OBRA, VOLUMEN, OBRA, i, c['pdf'], c['titulo'], c['texto'], 'es', 0, '', '[]'))
        pid = cur.lastrowid
        con.execute('insert into busqueda(rowid,texto,titulo) values (?,?,?)', (pid, c['texto'], c['titulo']))
        for (a, b, ref, libro, cap, v1, v2) in c['citas']:
            con.execute('insert into citas (pagina_id,inicio,fin,ref_texto,libro,capitulo,v_ini,v_fin) '
                        'values (?,?,?,?,?,?,?,?)', (pid, a, b, ref, libro, cap, v1, v2))
        print('ok %3d  %-55s %4d pal. %3d citas' % (i, c['titulo'][:55], len(c['texto'].split()), len(c['citas'])))

    con.execute("insert into busqueda(busqueda) values('rebuild')")
    con.commit()
    print('quick_check:', con.execute('pragma quick_check').fetchone()[0])
    print('citas totales:', con.execute('select count(*) from citas').fetchone()[0])
    con.close()


if __name__ == '__main__':
    main()
