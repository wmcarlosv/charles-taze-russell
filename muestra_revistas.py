"""Genera una página de muestra: texto del PDF frente al texto publicado."""
import sqlite3, html, re, subprocess

DB = '/home/carlos/Programas/pastor-russell-library/biblioteca.db'
PDF = ('/home/carlos/Imágenes/Documentos compartidos/Pictures/Imágenes/Bible Study Library/'
       'Library/Library/Russell/TOWERS')

MUESTRAS = [
    ('The Watch Tower — July 1879', 'ZWT1879/Z79JUL.PDF'),
    ('The Watch Tower — September 1909', 'ZWT1909/WTSEP09.PDF'),
    ('The Watch Tower — December 1916', 'ZWT1916/WTDEC16.PDF'),
]

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row


def parrafos(texto, n=8):
    out = []
    for p in texto.split('\n\n'):
        p = p.strip()
        if not p or re.fullmatch(r'[\s—–_=*·.]+', p):
            continue
        out.append('<p>' + html.escape(p) + '</p>')
        if len(out) >= n:
            break
    return '\n'.join(out)


filas = []
for titulo, ruta in MUESTRAS:
    antes = subprocess.run(['pdftotext', '-layout', PDF + '/' + ruta, '-'],
                           capture_output=True, text=True).stdout
    despues = con.execute('select texto from paginas where titulo=?', (titulo,)).fetchone()[0]
    filas.append((titulo, antes, despues))

css = """
:root{--navy:#14243f;--gold:#c9a227;--parch:#f7f0df;--paper:#fffdf7;--line:#e3d6b8;--muted:#7b6f58}
*{box-sizing:border-box}body{margin:0;background:var(--parch);font-family:Georgia,"Times New Roman",serif;color:#2c2a26}
header{background:linear-gradient(135deg,#101d33,#14243f 55%,#1d3a6b);color:#f7efd9;border-bottom:3px solid var(--gold);padding:18px 30px}
header h1{margin:0;font-size:1.25em;letter-spacing:.05em}header p{margin:4px 0 0;font-size:.78em;letter-spacing:.12em;text-transform:uppercase;color:#d8c79c}
main{max-width:1440px;margin:0 auto;padding:22px 28px 40px}
.numero{margin:0 0 26px}.numero h2{color:var(--navy);font-size:1.02em;margin:0 0 10px;letter-spacing:.03em}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:18px;align-items:start}
.panel{background:var(--paper);border:1px solid var(--line);border-radius:7px;padding:18px 22px;box-shadow:0 14px 36px -30px rgba(0,0,0,.5)}
.panel .tag{display:inline-block;font-size:.6em;letter-spacing:.14em;text-transform:uppercase;font-weight:700;border-radius:10px;padding:2px 8px;margin-bottom:12px}
.antes .tag{background:#f0e2d0;color:#8a4a2a}.despues .tag{background:#e8efdc;color:#3f5a2a}
.panel p{font-size:.9em;line-height:1.6;margin:0 0 .8em;text-align:justify;white-space:pre-wrap}
.antes p{font-size:.78em;color:#5d544a}
footer{max-width:1440px;margin:0 auto;padding:0 28px 26px;font-size:.72em;color:#9b8d74}
@media(max-width:900px){.cols{grid-template-columns:1fr}}
"""

partes = []
for titulo, antes, despues in filas:
    partes.append(f"""
<section class="numero"><h2>{html.escape(titulo)}</h2>
<div class="cols">
<div class="panel antes"><span class="tag">Texto extraído del PDF</span>{parrafos(antes)}</div>
<div class="panel despues"><span class="tag">Texto publicado en la biblioteca</span>{parrafos(despues)}</div>
</div></section>""")

body = f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Limpieza de las revistas — antes y después</title><style>{css}</style></head><body>
<header><h1>Pastor Russell Library — limpieza de The Watch Tower</h1>
<p>Sin cabeceras, avisos ni publicidad · sólo los artículos de estudio</p></header>
<main>{''.join(partes)}</main>
<footer>Pastor Russell Library · muestra editorial · sin audio</footer></body></html>"""

open('/home/carlos/Programas/pastor-russell-library/muestra-revistas.html', 'w', encoding='utf-8').write(body)
print('ok', len(body))
