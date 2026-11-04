"""Comprobación de las revistas ya importadas."""
import sqlite3, re, sys

con = sqlite3.connect('/home/carlos/Programas/pastor-russell-library/biblioteca.db')
con.row_factory = sqlite3.Row
oid = con.execute("select id from obras where titulo='The Watch Tower'").fetchone()[0]
filas = con.execute('select titulo,texto from paginas where obra_id=? order by orden', (oid,)).fetchall()
print('números:', len(filas))
print('caracteres:', sum(len(f['texto']) for f in filas))
restos = {
    'cabecera': r"(?im)^\s*(?:VOL\.|NO\.|PITTSBURGH,? PA\.|ALLEGHENY, PA\.)",
    'suscripción': r'(?i)SUBSCRIPTIONS AND BUSINESS',
    'cartas': r'(?im)^\s*INTERESTING LETTERS\s*\.?\s*$',
    'avisos': r'(?im)^\s*PUBLIC MINISTRIES OF THE TRUTH\s*$',
    'pagina': r'(?im)^\s*(?:R\d+\s*:\s*)?page\s+\d+\s*$',
    'portada': r"(?i)HERALD OF CHRIST['’]?S PRESENCE",
}
for nombre, patron in restos.items():
    hits = [f['titulo'] for f in filas if re.search(patron, f['texto'])]
    print('%-12s %3d %s' % (nombre, len(hits), hits[:4]))
cortos = [(f['titulo'], len(f['texto'])) for f in filas if len(f['texto']) < 8000]
print('números cortos:', cortos)
for titulo in ('The Watch Tower — July 1879', 'The Watch Tower — January 1900',
               'The Watch Tower — September 1909', 'The Watch Tower — December 1916'):
    f = con.execute('select texto from paginas where obra_id=? and titulo=?', (oid, titulo)).fetchone()
    print('\n===', titulo, len(f['texto']) if f else 'FALTA')
    if f:
        print(f['texto'][:260].replace('\n', ' | '))
