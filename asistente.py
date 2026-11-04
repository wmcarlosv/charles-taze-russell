#!/usr/bin/env python3
# Pastor Russell Library — servidor local del piloto
import gzip, hashlib, json, os, re, sqlite3, sys, urllib.parse, urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, 'biblioteca.db')
PUERTO = int(os.environ.get('PUERTO', '8100'))
HOST = os.environ.get('HOST', '127.0.0.1')

DEEPL_KEY = (os.environ.get('DEEPL_API_KEY') or '').strip()
if not DEEPL_KEY:
    try:
        DEEPL_KEY = open(os.path.join(BASE, 'deepl.key'), encoding='utf-8').read().strip()
    except OSError:
        pass
DEEPL_URL = os.environ.get('DEEPL_API_URL') or (
    'https://api-free.deepl.com/v2/translate' if DEEPL_KEY.endswith(':fx')
    else 'https://api.deepl.com/v2/translate')

def conectar():
    con = sqlite3.connect(DB, timeout=15)
    con.row_factory = sqlite3.Row
    for p in ('PRAGMA busy_timeout=15000', 'PRAGMA synchronous=NORMAL',
              'PRAGMA cache_size=-64000', 'PRAGMA temp_store=MEMORY'):
        try: con.execute(p)
        except sqlite3.DatabaseError: pass
    return con

def esc(s):
    return (str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
            .replace('"','&quot;'))

def obras():
    con = conectar()
    rows = con.execute('''SELECT o.*, count(p.id) n FROM obras o
                          LEFT JOIN paginas p ON p.obra_id=o.id
                          GROUP BY o.id ORDER BY o.id''').fetchall()
    con.close()
    return [dict(r) for r in rows]

def indice(obra_id):
    con = conectar()
    rows = con.execute('SELECT id,orden,titulo FROM paginas WHERE obra_id=? ORDER BY orden', (obra_id,)).fetchall()
    con.close()
    return [dict(r) for r in rows]

def render_parrafos(texto, citas):
    """Devuelve párrafos con las referencias ya convertidas en enlaces."""
    out = []
    pos = 0
    for parte in texto.split('\n\n'):
        ini = pos
        fin = pos + len(parte)
        cs = [c for c in citas if ini <= c['inicio'] < fin]
        html = ''
        cur = ini
        for c in cs:
            a, b = c['inicio'], min(c['fin'], fin)
            if a < cur: continue
            html += esc(texto[cur:a])
            html += ('<a class="ref" href="#" data-libro="%s" data-cap="%d" data-v1="%d" data-v2="%d" data-ref="%s">%s</a>'
                     % (esc(c['libro']), c['capitulo'], c['v_ini'], c['v_fin'], esc(c['ref_texto']), esc(texto[a:b])))
            cur = b
        html += esc(texto[cur:fin])
        if html.strip():
            out.append({'texto': parte, 'html': html})
        pos = fin + 2
    return out

def pagina(pid):
    con = conectar()
    f = con.execute('''SELECT p.*, o.titulo obra, o.autor FROM paginas p
                       JOIN obras o ON o.id=p.obra_id WHERE p.id=?''', (pid,)).fetchone()
    if not f:
        con.close(); return None
    citas = [dict(c) for c in con.execute(
        'SELECT inicio,fin,ref_texto,libro,capitulo,v_ini,v_fin FROM citas WHERE pagina_id=? ORDER BY inicio', (pid,))]
    prev = con.execute('SELECT id FROM paginas WHERE obra_id=? AND orden<? ORDER BY orden DESC LIMIT 1',
                       (f['obra_id'], f['orden'])).fetchone()
    nxt = con.execute('SELECT id FROM paginas WHERE obra_id=? AND orden>? ORDER BY orden ASC LIMIT 1',
                      (f['obra_id'], f['orden'])).fetchone()
    con.close()
    return {'id': f['id'], 'obra_id': f['obra_id'], 'obra': f['obra'], 'autor': f['autor'],
            'orden': f['orden'], 'titulo': f['titulo'],
            'parrafos': render_parrafos(f['texto'], citas),
            'prev': prev['id'] if prev else None, 'next': nxt['id'] if nxt else None}

def biblia_libros():
    con = conectar()
    rows = con.execute('SELECT libro, max(capitulo) caps, count(*) n FROM biblia GROUP BY libro').fetchall()
    con.close()
    orden = ['Genesis','Exodus','Leviticus','Numbers','Deuteronomy','Joshua','Judges','Ruth',
     '1Samuel','2Samuel','1Kings','2Kings','1Chronicles','2Chronicles','Ezra','Nehemiah',
     'Esther','Job','Psalms','Proverbs','Ecclesiastes','SongofSolomon','Isaiah','Jeremiah',
     'Lamentations','Ezekiel','Daniel','Hosea','Joel','Amos','Obadiah','Jonah','Micah',
     'Nahum','Habakkuk','Zephaniah','Haggai','Zechariah','Malachi','Matthew','Mark','Luke',
     'John','Acts','Romans','1Corinthians','2Corinthians','Galatians','Ephesians',
     'Philippians','Colossians','1Thessalonians','2Thessalonians','1Timothy','2Timothy',
     'Titus','Philemon','Hebrews','James','1Peter','2Peter','1John','2John','3John','Jude','Revelation']
    d = {r['libro']: dict(r) for r in rows}
    return [d[b] for b in orden if b in d]

def biblia_capitulo(libro, cap):
    con = conectar()
    rows = con.execute('SELECT versiculo,texto FROM biblia WHERE libro=? AND capitulo=? ORDER BY versiculo',
                       (libro, cap)).fetchall()
    con.close()
    return {'libro': libro, 'capitulo': cap, 'versiculos': [dict(r) for r in rows]}

def buscar(q):
    q = (q or '').strip()
    if not q: return {'total': 0, 'resultados': []}
    # FTS5: comillas para frases, resto palabras
    fq = ' '.join('"%s"' % x if ' ' in x else x for x in q.replace('"',' ').split())
    con = conectar()
    try:
        total = con.execute('SELECT count(*) FROM busqueda WHERE busqueda MATCH ?', (fq,)).fetchone()[0]
        rows = con.execute('''SELECT p.id,p.titulo,o.titulo obra,p.texto,bm25(busqueda) r
                              FROM busqueda b JOIN paginas p ON p.id=b.rowid
                              JOIN obras o ON o.id=p.obra_id
                              WHERE busqueda MATCH ? ORDER BY r LIMIT 30''', (fq,)).fetchall()
    except sqlite3.OperationalError:
        total, rows = 0, []
    con.close()
    out = []
    for r in rows:
        t = r['texto']
        i = t.lower().find(q.lower())
        if i < 0: i = 0
        out.append({'id': r['id'], 'titulo': r['titulo'], 'obra': r['obra'],
                    'extracto': t[max(0,i-100):i+220].strip()})
    return {'total': total, 'resultados': out}

_TT = {}

def _deepl(textos):
    data = [('auth_key', DEEPL_KEY), ('source_lang', 'EN'), ('target_lang', 'ES'),
            ('preserve_formatting', '1')]
    data += [('text', t) for t in textos]
    req = urllib.request.Request(DEEPL_URL, data=urllib.parse.urlencode(data).encode('utf-8'),
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
    d = json.load(urllib.request.urlopen(req, timeout=45))
    return [x.get('text', '') for x in d.get('translations', [])]

def _google(texto):
    if len(texto) > 4500:
        partes = re.split(r'(?<=[.!?])\s+', texto)
        out, buf = [], ''
        for p in partes:
            if len(buf) + len(p) + 1 > 4500 and buf:
                out.append(buf); buf = p
            else:
                buf = (buf + ' ' + p).strip()
        if buf: out.append(buf)
        return ' '.join(_google(p) for p in out)
    url = ('https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=es&dt=t&q='
           + urllib.parse.quote(texto))
    d = json.load(urllib.request.urlopen(url, timeout=30))
    return ''.join(x[0] for x in d[0] if x and x[0]).strip()

def traducir(textos):
    con = conectar()
    textos = [str(t or '') for t in textos]
    res = [''] * len(textos)
    faltan = []
    proveedor = 'deepl' if DEEPL_KEY else 'google'
    for i, t in enumerate(textos):
        if not t.strip():
            continue
        h = hashlib.sha256(((proveedor + '|' if proveedor == 'deepl' else '') + t).encode('utf-8')).hexdigest()
        row = con.execute('SELECT texto_es FROM traducciones WHERE hash=?', (h,)).fetchone()
        if row:
            res[i] = row[0]
        else:
            faltan.append((i, t, h))
    if proveedor == 'deepl' and faltan:
        try:
            trads = _deepl([x[1] for x in faltan])
            if len(trads) == len(faltan):
                for (i, t, h), es in zip(faltan, trads):
                    if es:
                        res[i] = es
                        con.execute('INSERT OR REPLACE INTO traducciones(hash,texto_en,texto_es) VALUES (?,?,?)', (h, t, es))
                con.commit()
                faltan = [x for x in faltan if not res[x[0]]]
            else:
                proveedor = 'google'
        except Exception:
            proveedor = 'google'
    if proveedor == 'google':
        for i, t, h in faltan:
            h = hashlib.sha256(t.encode('utf-8')).hexdigest()
            row = con.execute('SELECT texto_es FROM traducciones WHERE hash=?', (h,)).fetchone()
            if row:
                res[i] = row[0]; continue
            try:
                es = _google(t)
            except Exception:
                es = ''
            if es:
                con.execute('INSERT OR REPLACE INTO traducciones(hash,texto_en,texto_es) VALUES (?,?,?)', (h, t, es))
                con.commit()
            res[i] = es
    con.close()
    return {'traducciones': res, 'proveedor': proveedor}

class Handler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    def log_message(self, *a): pass
    def _send(self, data, tipo='application/json; charset=utf-8', code=200):
        if isinstance(data, str): data = data.encode('utf-8')
        if len(data) > 800 and 'gzip' in (self.headers.get('Accept-Encoding') or ''):
            data = gzip.compress(data, 6)
            self.send_response(code)
            self.send_header('Content-Type', tipo)
            self.send_header('Content-Encoding', 'gzip')
            self.send_header('Vary', 'Accept-Encoding')
        else:
            self.send_response(code)
            self.send_header('Content-Type', tipo)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(data)
    def _json(self, obj, code=200):
        self._send(json.dumps(obj, ensure_ascii=False), 'application/json; charset=utf-8', code)
    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(u.query)
        r = u.path
        try:
            if r in ('/', '/index.html'):
                return self._send(open(os.path.join(BASE, 'app.html'), 'rb').read(), 'text/html; charset=utf-8')
            if r == '/api/obras':
                return self._json(obras())
            if r == '/api/indice':
                return self._json(indice(int(q.get('obra_id', ['1'])[0])))
            if r == '/api/pagina':
                d = pagina(int(q.get('id', ['1'])[0]))
                return self._json(d or {'error': 'no encontrada'}, 200 if d else 404)
            if r == '/api/biblia':
                return self._json(biblia_libros())
            if r == '/api/biblia/capitulo':
                return self._json(biblia_capitulo(q.get('libro', ['John'])[0], int(q.get('cap', ['1'])[0])))
            if r == '/api/buscar':
                return self._json(buscar(q.get('q', [''])[0]))
            if r == '/api/estado':
                con = conectar()
                n = con.execute('select count(*) from paginas').fetchone()[0]
                c = con.execute('select count(*) from citas').fetchone()[0]
                v = con.execute('select count(*) from biblia').fetchone()[0]
                con.close()
                return self._json({'paginas': n, 'citas': c, 'versiculos': v, 'traductor': 'deepl' if DEEPL_KEY else 'google'})
            self._json({'error': 'no encontrado'}, 404)
        except Exception as e:
            self._json({'error': str(e)}, 500)
    def do_POST(self):
        u = urllib.parse.urlparse(self.path)
        if u.path != '/api/traducir':
            return self._json({'error': 'no encontrado'}, 404)
        try:
            n = int(self.headers.get('Content-Length', '0'))
            body = json.loads(self.rfile.read(n) or b'{}')
            textos = body.get('textos') or []
            if not isinstance(textos, list) or len(textos) > 30:
                return self._json({'error': 'lista no válida'}, 400)
            return self._json(traducir(textos))
        except Exception as e:
            return self._json({'error': str(e)}, 500)

if __name__ == '__main__':
    print('Pastor Russell Library en http://%s:%d' % (HOST, PUERTO), flush=True)
    ThreadingHTTPServer((HOST, PUERTO), Handler).serve_forever()
