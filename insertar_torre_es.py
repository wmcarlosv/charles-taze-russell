#!/usr/bin/env python3
"""Copia los números traducidos de La Torre del Vigía a la biblioteca española.

Añade el texto y sus referencias bíblicas (Reina-Valera 1960), de modo que
cada cita se pueda pulsar. Se puede ejecutar tantas veces como se quiera:
sólo añade lo que falta.
"""
import sqlite3
import sys

sys.path.insert(0, '/home/carlos/Programas/biblioteca-ia')
from pdf_vol import extrae  # noqa: E402

SRC = '/home/carlos/Programas/pastor-russell-library/biblioteca.db'
DST = '/home/carlos/Programas/biblioteca-ia/biblioteca.db'
OBRA = 'La Torre del Vigía'


def citas(dst, pid, texto):
    previo = -1
    for (a, b, ref, libro, cap, v1, v2) in extrae(texto):
        if a < previo or '\n\n' in texto[a:b]:
            continue
        dst.execute('insert into citas(pagina_id,inicio,fin,ref_texto,libro,capitulo,v_ini,v_fin) '
                    'values (?,?,?,?,?,?,?,?)', (pid, a, b, ref, libro, cap, v1, v2))
        previo = b


def main():
    src = sqlite3.connect(SRC, timeout=60)
    dst = sqlite3.connect(DST, timeout=60)
    dst.execute('PRAGMA journal_mode=WAL')
    filas = src.execute('select orden, titulo, texto from torre_es order by orden').fetchall()
    existentes = {r[0] for r in dst.execute(
        'select titulo from paginas where titulo_obra=?', (OBRA,))}
    nuevas = 0
    for orden, titulo, texto in filas:
        if titulo in existentes or not texto:
            continue
        cur = dst.execute(
            'insert into paginas(obra, volumen, titulo_obra, pagina, titulo, texto, idioma, indice) '
            'values (?,?,?,?,?,?,?,?)',
            (OBRA, 0, OBRA, orden, titulo, texto, 'es', 0))
        citas(dst, cur.lastrowid, texto)
        nuevas += 1
    dst.commit()

    # Referencias que falten en páginas ya copiadas.
    faltan = dst.execute(
        'select id, texto from paginas p where titulo_obra=? and not exists '
        '(select 1 from citas c where c.pagina_id=p.id)', (OBRA,)).fetchall()
    for pid, texto in faltan:
        citas(dst, pid, texto)
    dst.commit()

    if nuevas or faltan:
        dst.execute("insert into busqueda(busqueda) values('rebuild')")
        dst.commit()
    total = dst.execute('select count(*) from paginas where titulo_obra=?', (OBRA,)).fetchone()[0]
    nref = dst.execute('select count(*) from citas c join paginas p on p.id=c.pagina_id '
                       'where p.titulo_obra=?', (OBRA,)).fetchone()[0]
    print('añadidas %d · total %d · referencias %d' % (nuevas, total, nref))


if __name__ == '__main__':
    main()
