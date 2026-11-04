#!/usr/bin/env python3
"""Prepara la carpeta audio/ de la biblioteca con la Biblia Reina-Valera 1960.

Origen: /home/carlos/Desktop/RV-1960
Destino: audio/<slug>/<capitulo>.mp3

El origen tiene una carpeta numerada por libro (01 Genesis … 66 Apocalipsis) y
un MP3 por capítulo con el número al final del nombre ("Genesis 01.mp3").
"""
import os, re, shutil, sqlite3

BASE = os.path.dirname(os.path.abspath(__file__))
ORIGEN = '/home/carlos/Desktop/RV-1960'
DESTINO = os.path.join(BASE, 'audio')

SLUGS = [
    'genesis', 'exodo', 'levitico', 'numeros', 'deuteronomio', 'josue', 'jueces', 'rut',
    '1-samuel', '2-samuel', '1-reyes', '2-reyes', '1-cronicas', '2-cronicas', 'esdras',
    'nehemias', 'ester', 'job', 'salmos', 'proverbios', 'eclesiastes', 'cantares', 'isaias',
    'jeremias', 'lamentaciones', 'ezequiel', 'daniel', 'oseas', 'joel', 'amos', 'abdias',
    'jonas', 'miqueas', 'nahum', 'habacuc', 'sofonias', 'hageo', 'zacarias', 'malaquias',
    'mateo', 'marcos', 'lucas', 'juan', 'hechos', 'romanos', '1-corintios', '2-corintios',
    'galatas', 'efesios', 'filipenses', 'colosenses', '1-tesalonicenses', '2-tesalonicenses',
    '1-timoteo', '2-timoteo', 'tito', 'filemon', 'hebreos', 'santiago', '1-pedro', '2-pedro',
    '1-juan', '2-juan', '3-juan', 'judas', 'apocalipsis',
]


def capitulos():
    con = sqlite3.connect(os.path.join(BASE, 'biblioteca.db'))
    filas = con.execute('SELECT libro, count(DISTINCT capitulo) FROM biblia GROUP BY libro').fetchall()
    con.close()
    return filas


def main():
    os.makedirs(DESTINO, exist_ok=True)
    carpetas = []
    for nombre in os.listdir(ORIGEN):
        ruta = os.path.join(ORIGEN, nombre)
        m = re.match(r'^(\d{2})', nombre)
        if os.path.isdir(ruta) and m:
            carpetas.append((int(m.group(1)), nombre, ruta))
    carpetas.sort()
    if len(carpetas) != 66:
        print('Aviso: se esperaban 66 carpetas y hay %d' % len(carpetas))

    copiados = 0
    for numero, nombre, ruta in carpetas:
        if not (1 <= numero <= 66):
            continue
        slug = SLUGS[numero - 1]
        destino = os.path.join(DESTINO, slug)
        os.makedirs(destino, exist_ok=True)
        for archivo in sorted(os.listdir(ruta)):
            if not archivo.lower().endswith('.mp3'):
                continue
            m = re.search(r'(\d+)\s*\.mp3$', archivo, re.I)
            if not m:
                print('  sin número de capítulo:', archivo)
                continue
            cap = int(m.group(1))
            origen = os.path.join(ruta, archivo)
            dst = os.path.join(destino, '%d.mp3' % cap)
            if not os.path.exists(dst) or os.path.getsize(dst) != os.path.getsize(origen):
                shutil.copyfile(origen, dst)
                copiados += 1

    print('Copiados/actualizados: %d archivos' % copiados)
    print('Total en audio/: %d archivos, %.1f GB' % (
        sum(1 for r, _, fs in os.walk(DESTINO) for f in fs if f.endswith('.mp3')),
        sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(DESTINO)
            for f in fs if f.endswith('.mp3')) / 1073741824))

    faltan = []
    for libro, n in capitulos():
        # el orden de la base es el mismo que SLUGS
        idx = next((i for i, s in enumerate(SLUGS)
                    if s == re.sub(r'[^a-z0-9]+', '-', libro.lower()
                                   .replace('á','a').replace('é','e').replace('í','i')
                                   .replace('ó','o').replace('ú','u').replace('ñ','n')).strip('-')), None)
        if idx is None:
            continue
        for c in range(1, n + 1):
            if not os.path.exists(os.path.join(DESTINO, SLUGS[idx], '%d.mp3' % c)):
                faltan.append((libro, c))
    print('Capítulos sin archivo: %d' % len(faltan))
    for f in faltan[:20]:
        print('  ', f)


if __name__ == '__main__':
    main()
