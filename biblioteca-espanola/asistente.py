#!/usr/bin/env python3
# Biblioteca de investigación — Estudiantes de la Biblia
import base64, gzip, hashlib, json, os, re, sqlite3, sys, tarfile, threading, time, unicodedata, urllib.parse, urllib.request, mimetypes, asyncio
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE = os.path.dirname(os.path.abspath(__file__))
VENDOR = os.path.join(BASE, 'vendor')
if os.path.isdir(VENDOR):
    sys.path.insert(0, VENDOR)
DATOS = os.environ.get('BIBLIOTECA_DATOS') or BASE
DB = os.path.join(DATOS, 'biblioteca.db')
PUERTO = int(os.environ.get('PUERTO', '8099'))
HOST = os.environ.get('HOST', '0.0.0.0')

# Voces masculinas de edge-tts, en orden de preferencia (Jorge primero).
VOCES_EDGE = ['es-MX-JorgeNeural', 'es-ES-AlvaroNeural', 'es-AR-TomasNeural',
              'es-CO-GonzaloNeural', 'es-US-AlonsoNeural', 'es-VE-SebastianNeural']
TTS_CACHE = os.path.join(DATOS, 'tts-cache')

LIBROS = {
 'genesis':'Génesis','gen':'Génesis','gn':'Génesis','exodo':'Éxodo','ex':'Éxodo','levitico':'Levítico','lev':'Levítico',
 'numeros':'Números','num':'Números','deuteronomio':'Deuteronomio','deut':'Deuteronomio','josue':'Josué','jos':'Josué',
 'jueces':'Jueces','jue':'Jueces','rut':'Rut','1samuel':'1 Samuel','2samuel':'2 Samuel','1sam':'1 Samuel','2sam':'2 Samuel','1reyes':'1 Reyes','2reyes':'2 Reyes','1rey':'1 Reyes','2rey':'2 Reyes',
 '1cronicas':'1 Crónicas','2cronicas':'2 Crónicas','1cron':'1 Crónicas','2cron':'2 Crónicas','1cr':'1 Crónicas','2cr':'2 Crónicas','esdras':'Esdras','esd':'Esdras','nehemias':'Nehemías','neh':'Nehemías',
 'ester':'Ester','est':'Ester','job':'Job','salmos':'Salmos','salmo':'Salmos','sal':'Salmos','proverbios':'Proverbios','prov':'Proverbios',
 'eclesiastes':'Eclesiastés','ecl':'Eclesiastés','cantares':'Cantares','cant':'Cantares','isaias':'Isaías','isa':'Isaías','is':'Isaías',
 'jeremias':'Jeremías','jer':'Jeremías','lamentaciones':'Lamentaciones','lam':'Lamentaciones','ezequiel':'Ezequiel','ezeq':'Ezequiel',
 'daniel':'Daniel','dan':'Daniel','oseas':'Oseas','ose':'Oseas','joel':'Joel','amos':'Amós','am':'Amós','abdias':'Abdías','abd':'Abdías',
 'jonas':'Jonás','jon':'Jonás','miqueas':'Miqueas','miq':'Miqueas','nahum':'Nahúm','nah':'Nahúm','habacuc':'Habacuc','hab':'Habacuc',
 'sofonias':'Sofonías','sof':'Sofonías','ageo':'Hageo','hageo':'Hageo','hag':'Hageo','zacarias':'Zacarías','zac':'Zacarías',
 'malaquias':'Malaquías','mal':'Malaquías','mateo':'Mateo','mat':'Mateo','marcos':'Marcos','mar':'Marcos','mr':'Marcos','mc':'Marcos','lucas':'Lucas','luc':'Lucas',
 'juan':'Juan','jn':'Juan','hechos':'Hechos','hech':'Hechos','romanos':'Romanos','rom':'Romanos','1corintios':'1 Corintios','2corintios':'2 Corintios',
 '1cor':'1 Corintios','2cor':'2 Corintios','galatas':'Gálatas','gal':'Gálatas','efesios':'Efesios','efe':'Efesios','filipenses':'Filipenses','fil':'Filipenses',
 'colosenses':'Colosenses','col':'Colosenses','1tesalonicenses':'1 Tesalonicenses','2tesalonicenses':'2 Tesalonicenses','1tes':'1 Tesalonicenses','2tes':'2 Tesalonicenses','1ts':'1 Tesalonicenses','2ts':'2 Tesalonicenses',
 '1timoteo':'1 Timoteo','2timoteo':'2 Timoteo','1tim':'1 Timoteo','2tim':'2 Timoteo','1ti':'1 Timoteo','2ti':'2 Timoteo','tito':'Tito','tit':'Tito','filemon':'Filemón','flm':'Filemón',
 'hebreos':'Hebreos','heb':'Hebreos','santiago':'Santiago','sant':'Santiago','stg':'Santiago','1pedro':'1 Pedro','2pedro':'2 Pedro','1ped':'1 Pedro','2ped':'2 Pedro','1pet':'1 Pedro','2pet':'2 Pedro','1p':'1 Pedro','2p':'2 Pedro',
 '1juan':'1 Juan','2juan':'2 Juan','3juan':'3 Juan','1j':'1 Juan','2j':'2 Juan','3j':'3 Juan','1jn':'1 Juan','2jn':'2 Juan','3jn':'3 Juan','judas':'Judas','jud':'Judas','apocalipsis':'Apocalipsis','apoc':'Apocalipsis','ap':'Apocalipsis',
}

ORDEN = ['Génesis','Éxodo','Levítico','Números','Deuteronomio','Josué','Jueces','Rut','1 Samuel','2 Samuel','1 Reyes','2 Reyes',
 '1 Crónicas','2 Crónicas','Esdras','Nehemías','Ester','Job','Salmos','Proverbios','Eclesiastés','Cantares','Isaías','Jeremías',
 'Lamentaciones','Ezequiel','Daniel','Oseas','Joel','Amós','Abdías','Jonás','Miqueas','Nahúm','Habacuc','Sofonías','Hageo',
 'Zacarías','Malaquías','Mateo','Marcos','Lucas','Juan','Hechos','Romanos','1 Corintios','2 Corintios','Gálatas','Efesios',
 'Filipenses','Colosenses','1 Tesalonicenses','2 Tesalonicenses','1 Timoteo','2 Timoteo','Tito','Filemón','Hebreos','Santiago',
 '1 Pedro','2 Pedro','1 Juan','2 Juan','3 Juan','Judas','Apocalipsis']

def sinacento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower().strip()

def conectar():
    con = sqlite3.connect(DB, timeout=15)
    con.row_factory = sqlite3.Row
    for pragma in ('PRAGMA busy_timeout=15000', 'PRAGMA synchronous=NORMAL',
                   'PRAGMA cache_size=-64000', 'PRAGMA temp_store=MEMORY',
                   'PRAGMA mmap_size=134217728'):
        try:
            con.execute(pragma)
        except sqlite3.DatabaseError:
            pass
    return con

def parsea_ref(texto):
    t = sinacento(texto).replace('  ', ' ').strip()
    m = re.match(r'^([1-3]?\s*[a-záéíóúñ]+)\.?\s*(\d{1,3})'
                 r'(?:\s*[:.,]\s*(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?(?:\s*,\s*(\d{1,3}))?)?$', t)
    if not m:
        return None
    libro = LIBROS.get(m.group(1).replace(' ', '').replace('.', ''))
    if not libro:
        return None
    cap = int(m.group(2))
    v1 = int(m.group(3)) if m.group(3) else None
    v2 = int(m.group(4)) if m.group(4) else v1
    if m.group(5):
        v2 = max(v2 or 0, int(m.group(5)))
    return {'libro': libro, 'capitulo': cap, 'v_ini': v1, 'v_fin': v2}

def fts_query(q):
    """Convierte la consulta en sintaxis FTS5.

    Admite: varias palabras (todas), «frase exacta», palabra1 OR palabra2
    y -palabra para excluir.
    """
    q = q.strip()
    if not q:
        return ''

    def pieza(p):
        p = p.strip().replace('"', '').strip()
        if not p:
            return ''
        return '"%s"' % p if len(p) <= 4 else '"%s"*' % p

    grupos = re.split(r'\s+OR\s+|\s*\|\s*', q, flags=re.I)
    incluidos, excluidos = [], []
    for g in grupos:
        inc = []
        for tok in re.findall(r'"[^"]+"|\S+', g):
            if tok.startswith('-') and len(tok) > 1:
                t = pieza(tok[1:])
                if t:
                    excluidos.append(t)
            else:
                t = pieza(tok)
                if t:
                    inc.append(t)
        if inc:
            incluidos.append(' AND '.join(inc))
    if not incluidos:
        return ''
    base = incluidos[0] if len(incluidos) == 1 else '(' + ') OR ('.join(incluidos) + ')'
    for e in excluidos:
        base += ' NOT ' + e
    return base

def entero(q, clave, defecto=0, minimo=None, maximo=None):
    try:
        v = int(q.get(clave, [defecto])[0] or defecto)
    except (TypeError, ValueError):
        v = defecto
    if minimo is not None:
        v = max(minimo, v)
    if maximo is not None:
        v = min(maximo, v)
    return v

def acorta(texto, maximo=260):
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto if len(texto) <= maximo else texto[:maximo].rsplit(' ', 1)[0] + '…'

_ACENTOS = {'a':'[aáàâäã]','e':'[eéèëê]','i':'[iíìïî]','o':'[oóòôöõ]','u':'[uúùûü]',
            'n':'[nñ]','c':'[cç]'}

def _patron_acentos(t):
    salida = []
    for c in t:
        clases = _ACENTOS.get(c.lower())
        salida.append(clases if clases else re.escape(c))
    return ''.join(salida)

def _busca_termino(texto, terminos):
    """Primera aparición de cualquiera de los términos, sin distinguir acentos."""
    for x in terminos:
        if not x:
            continue
        m = re.search(_patron_acentos(x), texto, re.I)
        if m:
            return m.start()
    return -1

def contexto(texto, terminos, ancho=220):
    t = re.sub(r'(?m)^##\s*', '', texto)
    # saltar el encabezado en mayusculas (argumentos de capitulo)
    seg = t[:800]
    letras = [c for c in seg if c.isalpha()]
    ratio = (sum(1 for c in letras if c.isupper()) / len(letras)) if letras else 0
    if ratio > 0.45:
        for i in range(0, min(len(t) - 80, 1800)):
            if sum(1 for c in t[i:i + 80] if c.islower()) >= 30:
                t = t[i:]
                break
    pos = _busca_termino(t, terminos)
    if pos < 0:
        # respaldo: texto con acentos descompuestos u otras variantes
        bajo = sinacento(t)
        for x in terminos:
            pos = bajo.find(sinacento(x))
            if pos >= 0:
                break
    if pos < 0:
        return acorta(t, 260)
    # si la primera aparicion esta en el sumario inicial, buscar mas adelante
    if pos < 500 and len(t) > 500:
        for x in terminos:
            m2 = re.search(_patron_acentos(x), t[500:], re.I)
            if m2:
                pos = 500 + m2.start()
                break
    ini = max(0, pos - ancho // 2)
    fin = min(len(t), pos + ancho)
    # ajustar a limites de frase
    p_ini = t.rfind('. ', max(0, ini - 90), pos)
    if p_ini > 0:
        ini = p_ini + 2
    p_fin = t.find('. ', pos, min(len(t), fin + 120))
    if p_fin > 0:
        fin = p_fin + 1
    frag = t[ini:fin].strip()
    if ini > 0:
        frag = '… ' + frag
    if fin < len(t):
        frag = frag + ' …'
    return re.sub(r'\s+', ' ', frag)


BIBLIA_ORDEN = ['Génesis','Éxodo','Levítico','Números','Deuteronomio','Josué','Jueces','Rut','1 Samuel','2 Samuel','1 Reyes','2 Reyes','1 Crónicas','2 Crónicas','Esdras','Nehemías','Ester','Job','Salmos','Proverbios','Eclesiastés','Cantares','Isaías','Jeremías','Lamentaciones','Ezequiel','Daniel','Oseas','Joel','Amós','Abdías','Jonás','Miqueas','Nahúm','Habacuc','Sofonías','Hageo','Zacarías','Malaquías','Mateo','Marcos','Lucas','Juan','Hechos','Romanos','1 Corintios','2 Corintios','Gálatas','Efesios','Filipenses','Colosenses','1 Tesalonicenses','2 Tesalonicenses','1 Timoteo','2 Timoteo','Tito','Filemón','Hebreos','Santiago','1 Pedro','2 Pedro','1 Juan','2 Juan','3 Juan','Judas','Apocalipsis']
BIBLIA_AT = set(BIBLIA_ORDEN[:39])

def biblia_indice():
    con = conectar()
    filas = {f['libro']: f for f in con.execute(
        'SELECT libro, max(capitulo) cap, count(*) n FROM biblia GROUP BY libro')}
    con.close()
    libros = []
    for b in BIBLIA_ORDEN:
        f = filas.get(b)
        if not f:
            continue
        libros.append({'libro': b, 'capitulos': f['cap'], 'versiculos': f['n'],
                       'testamento': 'AT' if b in BIBLIA_AT else 'NT'})
    return {'libros': libros,
            'versiculos': sum(x['versiculos'] for x in libros),
            'capitulos': sum(x['capitulos'] for x in libros)}

def biblia_capitulo(libro, cap):
    con = conectar()
    filas = con.execute('SELECT versiculo, texto FROM biblia WHERE libro=? AND capitulo=? ORDER BY versiculo',
                        (libro, cap)).fetchall()
    comentado = set()
    try:
        for v_ini, v_fin in con.execute(
                'SELECT v_ini, v_fin FROM citas WHERE libro=? AND capitulo=? AND v_ini IS NOT NULL',
                (libro, cap)):
            fin = v_fin if v_fin and v_fin >= v_ini else v_ini
            if fin - v_ini > 300:
                fin = v_ini + 300
            comentado.update(range(v_ini, fin + 1))
    except Exception:
        pass
    con.close()
    return {'libro': libro, 'capitulo': cap,
            'versiculos': [dict(f, comentado=f['versiculo'] in comentado) for f in filas]}

def biblia_comentarios(libro, cap, verso):
    con = conectar()
    filas = con.execute(
        'SELECT p.id, p.titulo, p.titulo_obra, p.volumen, p.pagina, c.ref_texto, c.inicio '
        'FROM citas c JOIN paginas p ON p.id = c.pagina_id '
        'WHERE c.libro=? AND c.capitulo=? AND c.v_ini<=? '
        'AND COALESCE(c.v_fin, c.v_ini)>=? '
        'ORDER BY p.volumen, p.pagina, p.id',
        (libro, cap, verso, verso)).fetchall()
    marcas = {}
    refs = {}
    orden = []
    for f in filas:
        if f['id'] not in refs:
            refs[f['id']] = {'id': f['id'], 'titulo': f['titulo'] or '',
                             'obra': f['titulo_obra'] or f['titulo'] or '',
                             'volumen': f['volumen'], 'pagina': f['pagina'],
                             'ref': f['ref_texto'] or '', 'marca': '',
                             'posiciones': []}
            orden.append(f['id'])
        refs[f['id']]['posiciones'].append(f['inicio'] or 0)
    for pid in orden:
        r = refs[pid]
        if r['obra'] == 'La Torre del Vigía':
            if pid not in marcas:
                t = con.execute('SELECT texto FROM paginas WHERE id=?', (pid,)).fetchone()
                marcas[pid] = t['texto'] if t else ''
            t = marcas[pid]
            ms = re.findall(r'\[(R\d+ : page \d+)\]', t[:min(r['posiciones'])])
            if ms:
                r['marca'] = ms[-1]
    con.close()
    return {'libro': libro, 'capitulo': cap, 'versiculo': verso,
            'refs': [refs[i] for i in orden]}

def biblia_buscar(q, libro=None, limite=40, offset=0):
    fq = fts_query(q)
    if not fq:
        return {'total': 0, 'resultados': []}
    con = conectar()
    filtro = ''
    args = [fq]
    if libro:
        filtro = ' AND libro=?'
        args.append(libro)
    total = con.execute('SELECT count(*) FROM biblia_fts WHERE biblia_fts MATCH ?' + filtro, args).fetchone()[0]
    filas = con.execute(
        'SELECT rowid, libro, capitulo, versiculo, texto, bm25(biblia_fts) r FROM biblia_fts '
        'WHERE biblia_fts MATCH ?' + filtro + ' ORDER BY r LIMIT ? OFFSET ?',
        args + [limite, offset]).fetchall()
    con.close()
    terminos = [t for t in re.split(r'\s+', q.replace('"', '')) if t]
    return {'total': total, 'libro': libro or '',
            'resultados': [{'libro': f['libro'], 'capitulo': f['capitulo'], 'versiculo': f['versiculo'],
                            'texto': f['texto'], 'extracto': contexto(f['texto'], terminos, 190)} for f in filas]}

def buscar(q, limite=40, offset=0, obra=None, orden=''):
    fq = fts_query(q)
    if not fq:
        return {'total': 0, 'resultados': []}
    filtro = ''
    params = [fq]
    if obra:
        filtro = ' AND p.titulo_obra = ?'
        params.append(obra)
    con = conectar()
    total = con.execute(
        'SELECT count(*) FROM busqueda b JOIN paginas p ON p.id=b.rowid WHERE busqueda MATCH ?' + filtro,
        params).fetchone()[0]
    orden_sql = 'p.volumen, p.pagina' if orden == 'pagina' else 'r'
    filas = con.execute(
        'SELECT p.id, p.titulo_obra, p.volumen, p.pagina, p.titulo, p.texto, bm25(busqueda) AS r '
        'FROM busqueda b JOIN paginas p ON p.id=b.rowid WHERE busqueda MATCH ?' + filtro +
        ' ORDER BY ' + orden_sql + ' LIMIT ? OFFSET ?', params + [limite, offset]).fetchall()
    terminos = [p for p in re.split(r'\s+', q.replace('"', '')) if p]
    res = []
    for f in filas:
        marca = ''
        if (f['titulo_obra'] or '') == 'La Torre del Vigía':
            bajo = f['texto'].lower()
            pos = -1
            for t in terminos:
                i = bajo.find(t.lower())
                if i >= 0 and (pos < 0 or i < pos):
                    pos = i
            if pos > 0:
                ms = re.findall(r'\[(R\d+ : page \d+)\]', f['texto'][:pos])
                if ms:
                    marca = ms[-1]
        res.append({
            'id': f['id'], 'obra': f['titulo_obra'], 'volumen': f['volumen'],
            'pagina': f['pagina'], 'titulo': f['titulo'],
            'extracto': contexto(f['texto'], terminos), 'marca': marca,
        })
    # distribucion por volumen (sólo cuando se pide la primera página)
    dist = []
    if offset == 0:
        dist = con.execute(
            'SELECT p.titulo_obra, count(*) n FROM busqueda b JOIN paginas p ON p.id=b.rowid '
            'WHERE busqueda MATCH ?' + filtro + ' GROUP BY p.titulo_obra ORDER BY n DESC', params).fetchall()
    con.close()
    return {'total': total, 'resultados': res, 'distribucion': [dict(d) for d in dist]}

def parrafos(texto, n=4):
    partes = re.split(r'(?<=[.!?»"])\s+', texto)
    salida, buf = [], []
    for p in partes:
        buf.append(p)
        if len(buf) >= n:
            salida.append(' '.join(buf)); buf = []
    if buf:
        salida.append(' '.join(buf))
    return salida

def bloques(texto, n=5):
    if '\n\n' in texto:
        out, pos = [], 0
        for parte in texto.split('\n\n'):
            if parte.strip():
                out.append({'ini': pos, 'fin': pos + len(parte)})
            pos += len(parte) + 2
        return out
    out, cortes, cuenta = [], [0], 0
    for m in re.finditer(r'(?<=[.!?»"])\s+', texto):
        cuenta += 1
        if cuenta % n == 0:
            cortes.append(m.end())
    cortes.append(len(texto))
    for a, b in zip(cortes, cortes[1:]):
        if b > a:
            out.append({'ini': a, 'fin': b})
    return out


_CURIOSIDADES = None


def curiosidades():
    """Cifras y datos curiosos del corpus, calculados una sola vez."""
    global _CURIOSIDADES
    if _CURIOSIDADES is not None:
        return _CURIOSIDADES
    con = conectar()
    try:
        palabras = 0
        imagenes = set()
        largo = None
        for r in con.execute('SELECT titulo_obra, titulo, texto FROM paginas'):
            t = r['texto'] or ''
            n = len(t.split())
            palabras += n
            if r['titulo_obra'] == 'Foto-Drama de la Creación':
                imagenes.update(re.findall(r'\[\[img:([^|\]]+)', t))
            if largo is None or n > largo['palabras']:
                largo = {'obra': r['titulo_obra'], 'titulo': r['titulo'], 'palabras': n}
        citas = con.execute('SELECT count(*) FROM citas').fetchone()[0]
        versiculos = con.execute('SELECT count(DISTINCT ref_texto) FROM citas').fetchone()[0]
        top_v = con.execute('SELECT ref_texto, count(*) c FROM citas GROUP BY ref_texto '
                            'ORDER BY c DESC LIMIT 1').fetchone()
        top_t = con.execute('SELECT termino_es, termino, nrefs FROM temas '
                            'ORDER BY nrefs DESC LIMIT 1').fetchone()
        foto_caps = con.execute("SELECT count(*) FROM paginas "
                                "WHERE titulo_obra='Foto-Drama de la Creación'").fetchone()[0]
        foto_enlaces = con.execute('SELECT count(*) FROM temafoto').fetchone()[0]
        datos = {
            'palabras': palabras,
            'paginas': con.execute('SELECT count(*) FROM paginas').fetchone()[0],
            'citas': citas,
            'versiculos': versiculos,
            'versiculo_top': {'ref': top_v['ref_texto'], 'n': top_v['c']} if top_v else None,
            'tema_top': {'es': top_t['termino_es'], 'en': top_t['termino'],
                         'n': top_t['nrefs']} if top_t else None,
            'foto_caps': foto_caps,
            'foto_imgs': len(imagenes),
            'foto_enlaces': foto_enlaces,
            'capitulo_largo': largo,
            'temas': con.execute('SELECT count(*) FROM temas').fetchone()[0],
            'libros': 66,
            'capitulos_biblia': 1189,
        }
    finally:
        con.close()
    _CURIOSIDADES = datos
    return datos


_GALERIA = None


def galeria_foto():
    """Láminas del Foto-Drama con el capítulo al que pertenecen."""
    global _GALERIA
    if _GALERIA is not None:
        return _GALERIA
    con = conectar()
    items = []
    for f in con.execute("SELECT id, pagina, titulo, texto FROM paginas "
                         "WHERE titulo_obra='Foto-Drama de la Creación' ORDER BY pagina"):
        t = f['texto'] or ''
        for m in re.finditer(r'\[\[img:([^|\]]+)(?:\|([^\]]*))?\]\]', t):
            siguiente = t.find('[[img:', m.end())
            trozo = t[m.end(): siguiente if siguiente != -1 else len(t)]
            cap = re.match(r'\s*##\s+([^\n]+)', trozo)
            caption = (m.group(2) or (cap.group(1).strip() if cap else '') or f['titulo'])
            items.append({'img': m.group(1), 'pid': f['id'], 'pagina': f['pagina'],
                          'titulo': f['titulo'], 'caption': caption})
    con.close()
    _GALERIA = {'total': len(items), 'items': items}
    return _GALERIA


def pagina(pid):
    con = conectar()
    f = con.execute('SELECT * FROM paginas WHERE id=?', (pid,)).fetchone()
    if not f:
        con.close(); return None
    citas = con.execute('SELECT inicio,fin,ref_texto,libro,capitulo,v_ini,v_fin FROM citas WHERE pagina_id=? ORDER BY inicio', (pid,)).fetchall()
    prev = con.execute('SELECT id FROM paginas WHERE titulo_obra=? AND (pagina<? OR (pagina=? AND id<?)) ORDER BY pagina DESC, id DESC LIMIT 1',
                       (f['titulo_obra'], f['pagina'], f['pagina'], pid)).fetchone()
    nxt = con.execute('SELECT id FROM paginas WHERE titulo_obra=? AND (pagina>? OR (pagina=? AND id>?)) ORDER BY pagina ASC, id ASC LIMIT 1',
                      (f['titulo_obra'], f['pagina'], f['pagina'], pid)).fetchone()
    con.close()
    return {
        'id': f['id'], 'obra': f['titulo_obra'], 'volumen': f['volumen'], 'pagina': f['pagina'],
        'titulo': f['titulo'], 'idioma': f['idioma'],
        'resumen': json.loads(f['resumen']) if f['resumen'] else [],
        'original': f['original'] if (f['original'] and f['original'] != f['texto']) else None,
        'bloques': bloques(f['texto']),
        'texto': f['texto'],
        'citas': [dict(c) for c in citas],
        'prev': prev['id'] if prev else None,
        'next': nxt['id'] if nxt else None,
    }

def versiculo(ref, simple=False):
    r = parsea_ref(ref)
    if not r:
        return {'error': 'No he reconocido la referencia. Prueba con «Juan 3:16».'}
    con = conectar()
    if r['v_ini'] is None:
        filas = con.execute('SELECT versiculo, texto FROM biblia WHERE libro=? AND capitulo=? ORDER BY versiculo',
                            (r['libro'], r['capitulo'])).fetchall()
    else:
        filas = con.execute('SELECT versiculo, texto FROM biblia WHERE libro=? AND capitulo=? AND versiculo BETWEEN ? AND ? ORDER BY versiculo',
                            (r['libro'], r['capitulo'], r['v_ini'], r['v_fin'])).fetchall()
    paginas = []
    if not simple:
        if r['v_ini'] is None:
            q = ('SELECT DISTINCT p.id,p.titulo_obra,p.volumen,p.pagina,p.titulo,p.texto FROM citas c JOIN paginas p ON p.id=c.pagina_id '
                 'WHERE c.libro=? AND c.capitulo=? LIMIT 60')
            args = (r['libro'], r['capitulo'])
        else:
            q = ('SELECT DISTINCT p.id,p.titulo_obra,p.volumen,p.pagina,p.titulo,p.texto FROM citas c JOIN paginas p ON p.id=c.pagina_id '
                 'WHERE c.libro=? AND c.capitulo=? AND c.v_ini<=? AND (c.v_fin>=? OR c.v_fin IS NULL) LIMIT 60')
            args = (r['libro'], r['capitulo'], r['v_fin'], r['v_ini'])
        for f in con.execute(q, args):
            paginas.append({'id': f['id'], 'obra': f['titulo_obra'], 'volumen': f['volumen'],
                            'pagina': f['pagina'], 'titulo': f['titulo'],
                            'extracto': contexto(f['texto'], [r['libro']], 200)})
    con.close()
    etiqueta = '%s %d' % (r['libro'], r['capitulo'])
    if r['v_ini']:
        etiqueta += ':%d' % r['v_ini'] if r['v_ini'] == r['v_fin'] else ':%d-%d' % (r['v_ini'], r['v_fin'])
    return {'ref': etiqueta, 'libro': r['libro'], 'capitulo': r['capitulo'],
            'v_ini': r['v_ini'], 'v_fin': r['v_fin'],
            'versiculos': [dict(x) for x in filas], 'paginas': paginas,
            'disponible': bool(filas)}

VACIAS = set('''de la el los las un una unos unas y o u que qué como cómo cuando cuál cuáles quien quién
por para con sin sobre entre según del al es son fue ser esta este esto estas estos lo le les se su sus
mi tu nos os me te hay ha han he hemos está están estaba enseña enseñan dice dicen habla hablan trata tratan
significa significado explica explican muestra muestran biblioteca libro libros obra obras russell
acerca tema respecto cuales cual dime quiero saber necesito sobre biblia biblias escritura
 escrituras señor dios cristo jesús'''.split())


def palabras_clave(q):
    limpio = re.sub(r'[¿?¡!.,;:()"«»]', ' ', q.lower())
    todas = [w for w in limpio.split() if len(w) > 2]
    claves = [w for w in todas if w not in VACIAS]
    return claves or sorted(todas, key=len, reverse=True)[:1]


def preguntar(q):
    q = (q or '').strip()
    if not q:
        return {'tipo': 'vacio', 'respuesta': 'Escribe una pregunta, una palabra o una referencia bíblica.'}
    ref = parsea_ref(q)
    if ref:
        v = versiculo(q)
        n = len(v['paginas'])
        if not v['disponible']:
            return {'tipo': 'versiculo', 'respuesta':
                    'No tengo todavía el texto RVR1960 de %s (la descarga de la Biblia sigue en curso). '
                    'Pero la biblioteca cita ese pasaje en %d páginas.' % (v['ref'], n),
                    'versiculo': v}
        texto = ' '.join(x['texto'] for x in v['versiculos'])
        return {'tipo': 'versiculo', 'respuesta':
                '%s (RVR1960): «%s». La biblioteca comenta o cita este pasaje en %d páginas.'
                % (v['ref'], texto, n), 'versiculo': v}
    m = re.search(r'([1-3]?\s*[A-Za-zÁÉÍÓÚÑáéíóúñ]+)\s+(\d{1,3}):(\d{1,3})', q)
    if m and LIBROS.get(sinacento(m.group(1)).replace(' ', '')):
        return preguntar(m.group(0))
    claves = palabras_clave(q)
    consulta = ' '.join(claves[:6]) if claves else q
    r = buscar(consulta, limite=6)
    if not r['total'] and claves:
        r = buscar(max(claves, key=len), limite=6)
        consulta = max(claves, key=len)
    if not r['total']:
        return {'tipo': 'sinresultados', 'respuesta':
                'No encuentro «%s» en la biblioteca. Prueba con otra palabra, en singular, o con una cita bíblica (por ejemplo «Romanos 5:12»).' % q,
                'resultados': []}
    dist = ', '.join('%s (%d)' % (d['titulo_obra'], d['n']) for d in r['distribucion'][:4])
    return {'tipo': 'tema',
            'respuesta': 'He encontrado %d páginas relacionadas con «%s». Se reparten así: %s. Estos son los pasajes más pertinentes:'
                         % (r['total'], consulta, dist),
            'resultados': r['resultados']}

def _trozos(texto, limite=1700):
    partes, buf = [], ''
    for frase in re.split(r'(?<=[.!?])\s+', texto):
        if len(buf) + len(frase) > limite and buf:
            partes.append(buf)
            buf = ''
        buf += frase + ' '
    if buf.strip():
        partes.append(buf)
    return partes


def _traduce_trozo(t):
    u = ('https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=es&q=' +
         urllib.parse.quote(t))
    with urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=45) as r:
        d = json.loads(r.read().decode('utf-8', 'replace'))
    if isinstance(d, list):
        return ' '.join(x for x in d if isinstance(x, str))
    return str(d)


def traducir(texto):
    if not texto or not texto.strip():
        return ''
    h = hashlib.sha1(texto.encode('utf-8')).hexdigest()
    con = conectar()
    f = con.execute('SELECT texto FROM traducciones WHERE hash=?', (h,)).fetchone()
    if f:
        con.close()
        return f['texto']
    con.close()
    partes = []
    for t in _trozos(texto):
        for intento in range(3):
            try:
                partes.append(_traduce_trozo(t))
                break
            except Exception:
                time.sleep(2 + intento * 3)
        else:
            return None
    es = ' '.join(partes).strip()
    if es:
        con = conectar()
        con.execute('INSERT OR REPLACE INTO traducciones (hash,texto) VALUES (?,?)', (h, es))
        con.commit()
        con.close()
    return es




_REFSMAP = None
def _mapa_refs():
    """referencia -> (página, posición, aproximada) para el índice temático."""
    global _REFSMAP
    if _REFSMAP is None:
        con = conectar()
        d = {}
        for r in con.execute('SELECT ref, pid, pos, aprox FROM refmap'):
            d[r['ref']] = (r['pid'], r['pos'], r['aprox'] or 0)
        for r in con.execute('SELECT ref, pid, pos, aprox FROM tmap'):
            d.setdefault(r['ref'], (r['pid'], r['pos'], r['aprox'] or 0))
        con.close()
        _REFSMAP = d
    return _REFSMAP

_REFCTX = None
def _mapa_refctx():
    """Destinos afinados (referencia + palabra guía) -> (pid, pos, término)."""
    global _REFCTX
    if _REFCTX is None:
        con = conectar()
        try:
            _REFCTX = {(r['ref'], r['ctx']): (r['pid'], r['pos'], r['term'])
                       for r in con.execute('SELECT ref, ctx, pid, pos, term FROM refctx')}
        except Exception:
            _REFCTX = {}
        con.close()
    return _REFCTX

def _con_contexto(lineas):
    """Añade a cada referencia el rótulo temático que la precede en el índice.

    Sirve para que, al pulsar la referencia, el lector salte al párrafo donde
    aparece esa palabra (p. ej. AARÓN -> «Representa: Iglesia, T29» resalta
    «Iglesia») y no sólo a la marca de página.
    """
    for ln in lineas:
        if not ln:
            continue
        segs = ln[2] if len(ln) == 3 else (ln[1] if len(ln) > 1 else [])
        etiqueta = re.sub(r'\s+', ' ', str(ln[0] or '')).strip().strip(':').strip()
        ultimo = etiqueta
        for sg in segs:
            if not isinstance(sg, list) or not sg:
                continue
            if sg[0] == 't':
                txt = re.sub(r'\s+', ' ', str(sg[1])).strip()
                trozos = [x.strip() for x in re.split(r'[;,:]', txt) if x.strip()]
                trozo = trozos[-1] if trozos else ''
                if len(re.sub(r'[^0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]', '', trozo)) >= 3:
                    ultimo = trozo
                elif len(re.sub(r'[^0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]', '', txt)) >= 3:
                    ultimo = txt.strip(' ;,.')
            elif sg[0] == 'r':
                ctx = ultimo or etiqueta
                if len(sg) == 3:
                    sg.append(ctx)
                elif len(sg) >= 4 and not sg[3]:
                    sg[3] = ctx
    return lineas

_CACHE_TEXTOS = {}

def _texto_comprimido(ruta):
    """Devuelve (bytes, gzip) y los conserva mientras el archivo no cambie."""
    st = os.stat(ruta)
    clave = (ruta, st.st_mtime_ns, st.st_size)
    it = _CACHE_TEXTOS.get(clave)
    if it:
        return it
    d = open(ruta, 'rb').read()
    it = (d, gzip.compress(d, 6))
    if len(_CACHE_TEXTOS) >= 8:
        _CACHE_TEXTOS.clear()
    _CACHE_TEXTOS[clave] = it
    return it

def _tts_limpiar(texto):
    t = re.sub(r'\[\[img:[^\]]*\]\]', ' ', texto or '')
    t = re.sub(r'\[[A-Z]\d+\]', ' ', t)
    t = re.sub(r'(?m)^\s*##\s*', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:12000]


def _tts_trozos(texto, maximo=1800):
    partes = re.split(r'(?<=[.!?;:])\s+', texto)
    out, buf = [], ''
    for p in partes:
        p = p.strip()
        if not p:
            continue
        if buf and len(buf) + 1 + len(p) > maximo:
            out.append(buf); buf = p
        else:
            buf = (buf + ' ' + p).strip()
    if buf:
        out.append(buf)
    return out or [texto[:maximo]]


def _tts_limpiar_cache(maximo=350 * 1024 * 1024, archivos=400):
    try:
        fs = [os.path.join(TTS_CACHE, f) for f in os.listdir(TTS_CACHE) if f.endswith('.mp3')]
        fs.sort(key=os.path.getmtime)
        total = sum(os.path.getsize(f) for f in fs)
        while fs and (total > maximo or len(fs) > archivos):
            f = fs.pop(0)
            total -= os.path.getsize(f)
            try:
                os.remove(f)
            except OSError:
                pass
    except Exception:
        pass


def _tts_archivo(texto, voz):
    """Genera (o reutiliza) el MP3 de edge-tts. Devuelve None si no está disponible."""
    try:
        import edge_tts
    except Exception:
        return None
    clave = hashlib.sha256((voz + '|r-10|p-10|' + texto).encode('utf-8')).hexdigest()
    try:
        os.makedirs(TTS_CACHE, exist_ok=True)
    except Exception:
        return None
    destino = os.path.join(TTS_CACHE, clave + '.mp3')
    if os.path.isfile(destino) and os.path.getsize(destino) > 1000:
        return destino
    tmp = destino + '.part'

    async def sintetizar():
        with open(tmp, 'wb') as f:
            for trozo in _tts_trozos(texto):
                c = edge_tts.Communicate(trozo, voz, rate='-10%', pitch='-10Hz')
                async for chunk in c.stream():
                    if chunk.get('type') == 'audio':
                        f.write(chunk['data'])

    try:
        asyncio.run(asyncio.wait_for(sintetizar(), 90))
        if os.path.getsize(tmp) > 1000:
            os.replace(tmp, destino)
            _tts_limpiar_cache()
            return destino
    except Exception as e:
        print('tts:', e, flush=True)
    try:
        os.remove(tmp)
    except OSError:
        pass
    return None


class Manejador(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def log_message(self, fmt, *args):
        pass

    def _enviar(self, d, tipo, estado=200, cache=True, max_age=None, comprimible=True, gz=None):
        usar_gzip = (comprimible and len(d) >= 700
                     and 'gzip' in (self.headers.get('Accept-Encoding') or '').lower())
        if usar_gzip:
            d = gz if gz else gzip.compress(d, 6)
        self.send_response(estado)
        self.send_header('Content-Type', tipo)
        if usar_gzip:
            self.send_header('Content-Encoding', 'gzip')
            self.send_header('Vary', 'Accept-Encoding')
        self.send_header('Content-Length', str(len(d)))
        if not cache:
            self.send_header('Cache-Control', 'no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
        elif max_age:
            self.send_header('Cache-Control', 'public, max-age=%d' % max_age)
        self.end_headers()
        self.wfile.write(d)

    def _json(self, obj, estado=200):
        d = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self._enviar(d, 'application/json; charset=utf-8', estado)

    def _archivo(self, ruta, tipo, cache=True, max_age=None):
        if not os.path.isfile(ruta):
            self.send_error(404); return
        texto = (tipo.startswith('text/') or 'json' in tipo or 'javascript' in tipo
                 or 'svg' in tipo or 'xml' in tipo)
        gz = None
        if texto:
            d, gz = _texto_comprimido(ruta)
        else:
            try:
                d = open(ruta, 'rb').read()
            except FileNotFoundError:
                self.send_error(404); return
        self._enviar(d, tipo, 200, cache, max_age, comprimible=texto, gz=gz)

    def _audio(self, ruta, tipo='audio/mpeg'):
        """Entrega audio MP3 con soporte de Range para poder buscar dentro de la pista."""
        if not os.path.isfile(ruta):
            self.send_error(404); return
        tam = os.path.getsize(ruta)
        inicio, fin, codigo = 0, tam - 1, 200
        rango = self.headers.get('Range', '')
        if rango:
            m = re.match(r'bytes=(\d*)-(\d*)', rango.strip())
            if m:
                if not m.group(1) and m.group(2):
                    # rango del final: bytes=-N
                    largo_final = int(m.group(2))
                    inicio = max(0, tam - largo_final)
                    fin = tam - 1
                else:
                    if m.group(1):
                        inicio = int(m.group(1))
                    if m.group(2):
                        fin = int(m.group(2))
                if inicio > fin or inicio >= tam:
                    self.send_response(416)
                    self.send_header('Content-Range', 'bytes */%d' % tam)
                    self.send_header('Content-Length', '0')
                    self.end_headers(); return
                fin = min(fin, tam - 1)
                codigo = 206
        largo = fin - inicio + 1
        self.send_response(codigo)
        self.send_header('Content-Type', tipo)
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(largo))
        self.send_header('Cache-Control', 'public, max-age=604800')
        if codigo == 206:
            self.send_header('Content-Range', 'bytes %d-%d/%d' % (inicio, fin, tam))
        self.end_headers()
        try:
            with open(ruta, 'rb') as f:
                f.seek(inicio)
                restante = largo
                while restante > 0:
                    bloque = f.read(min(65536, restante))
                    if not bloque:
                        break
                    self.wfile.write(bloque)
                    restante -= len(bloque)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def _autorizado(self):
        ip = self.client_address[0] if self.client_address else '127.0.0.1'
        if ip.startswith('127.') or ip in ('::1', 'localhost'):
            return True
        ruta = os.path.join(BASE, 'clave.txt')
        try:
            clave = open(ruta, encoding='utf-8').read().strip()
        except Exception:
            return True
        if not clave:
            return True
        cab = self.headers.get('Authorization', '')
        if not cab.startswith('Basic '):
            return False
        try:
            datos = base64.b64decode(cab[6:]).decode('utf-8', 'replace')
            _, _, passwd = datos.partition(':')
            return passwd == clave
        except Exception:
            return False

    def do_POST(self):
        ruta = urllib.parse.urlparse(self.path).path
        if ruta != '/api/tts':
            self.send_error(404); return
        try:
            largo = int(self.headers.get('Content-Length') or 0)
            if largo > 200000:
                return self._json({'error': 'texto demasiado largo'}, 413)
            datos = json.loads(self.rfile.read(largo) or b'{}')
            texto = _tts_limpiar(str(datos.get('texto') or ''))
            if not texto:
                return self._json({'error': 'texto vacío'}, 400)
            voz = str(datos.get('voz') or VOCES_EDGE[0])
            if voz not in VOCES_EDGE:
                voz = VOCES_EDGE[0]
            ruta_mp3 = _tts_archivo(texto, voz)
            if not ruta_mp3:
                return self._json({'error': 'texto a voz no disponible: instala edge-tts y revisa la conexión'}, 503)
            return self._audio(ruta_mp3, 'audio/mpeg')
        except Exception as e:
            return self._json({'error': str(e)}, 500)

    def do_GET(self):
        if not self._autorizado():
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm="Biblioteca Estudios"')
            self.send_header('Content-Length', '0')
            self.end_headers()
            return
        p = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(p.query)
        ruta = p.path
        try:
            if ruta in ('/', '/index.html'):
                return self._archivo(os.path.join(BASE, 'app.html'), 'text/html; charset=utf-8', cache=False)
            if ruta.startswith('/img/'):
                rel = urllib.parse.unquote(ruta[len('/img/'):])
                if not rel or '..' in rel or rel.startswith('/'):
                    self.send_error(404); return
                tipo = mimetypes.guess_type(rel)[0] or 'application/octet-stream'
                return self._archivo(os.path.join(BASE, 'img', rel), tipo, max_age=604800)
            if ruta in ('/tutorial', '/tutorial.html'):
                return self._archivo(os.path.join(BASE, 'tutorial.html'), 'text/html; charset=utf-8', cache=False)
            if ruta in ('/mana', '/mana/'):
                return self._archivo(os.path.join(BASE, 'mana', 'vista-previa.html'),
                                     'text/html; charset=utf-8', cache=False)
            if ruta.startswith('/mana/'):
                rel = urllib.parse.unquote(ruta[len('/mana/'):])
                permitidos = {'vista-previa.html', 'mana-completo.json', 'mana-diario.json',
                              'devociones-matutinas.json', 'suplemento.json', 'LEEME.md'}
                if rel not in permitidos:
                    self.send_error(404); return
                tipo = mimetypes.guess_type(rel)[0] or 'application/octet-stream'
                return self._archivo(os.path.join(BASE, 'mana', rel), tipo, cache=False)
            if ruta.startswith('/audio/'):
                rel = urllib.parse.unquote(ruta[len('/audio/'):])
                if not re.fullmatch(r'[a-z0-9-]+/(?:\d{1,3}|completo)\.(?:mp3|opus)', rel):
                    self.send_error(404); return
                tipo = 'audio/ogg' if rel.lower().endswith('.opus') else 'audio/mpeg'
                return self._audio(os.path.join(BASE, 'audio', rel), tipo)
            if ruta == '/tutorial.pdf':
                return self._archivo(os.path.join(BASE, 'tutorial.pdf'), 'application/pdf', max_age=3600)
            if ruta == '/tutorial-fotos.zip':
                return self._archivo(os.path.join(BASE, 'tutorial-fotos.zip'), 'application/zip', max_age=3600)
            if ruta == '/icono.png':
                return self._archivo(os.path.join(BASE, 'icono.png'), 'image/png', max_age=604800)
            if ruta in ('/icono-192.png', '/icono-512.png', '/russell-icono.png',
                        '/russell-192.png', '/russell-512.png'):
                nombre = os.path.basename(ruta)
                return self._archivo(os.path.join(BASE, nombre), 'image/png', max_age=604800)
            if ruta == '/manifest.json':
                return self._archivo(os.path.join(BASE, 'manifest.json'), 'application/manifest+json', max_age=86400)
            if ruta == '/sw.js':
                return self._archivo(os.path.join(BASE, 'sw.js'), 'application/javascript', cache=False)
            if ruta == '/api/biblia':
                return self._json(biblia_indice())
            if ruta == '/api/galeria':
                return self._json(galeria_foto())
            if ruta == '/api/curiosidades':
                return self._json(curiosidades())
            if ruta == '/api/biblia/capitulo':
                return self._json(biblia_capitulo(q.get('libro', [''])[0], entero(q, 'cap', 1, 1, 200)))
            if ruta == '/api/biblia/comentarios':
                return self._json(biblia_comentarios(q.get('libro', [''])[0],
                                                     entero(q, 'cap', 1, 1, 200),
                                                     entero(q, 'v', 1, 1, 200)))
            if ruta == '/api/biblia/buscar':
                return self._json(biblia_buscar((q.get('q', [''])[0] or '')[:200], q.get('libro', [None])[0],
                                                entero(q, 'limit', 40, 1, 100),
                                                entero(q, 'offset', 0, 0)))
            if ruta == '/api/buscar':
                texto = (q.get('q', [''])[0] or '')[:200]
                obra = q.get('obra', [None])[0]
                off = entero(q, 'offset', 0, 0)
                lim = entero(q, 'limit', 40, 1, 100)
                orden = q.get('orden', [''])[0]
                return self._json(buscar(texto, limite=lim, offset=off, obra=obra, orden=orden))
            if ruta == '/api/pagina':
                r = pagina(entero(q, 'id'))
                return self._json(r or {'error': 'no encontrada'})
            if ruta == '/api/versiculo':
                return self._json(versiculo(q.get('ref', [''])[0],
                                            bool(q.get('simple', [''])[0])))
            if ruta == '/api/preguntar':
                return self._json(preguntar(q.get('q', [''])[0]))
            if ruta == '/api/traducir':
                t = traducir(q.get('texto', [''])[0])
                return self._json({'texto': t})
            if ruta == '/api/indice':
                obra = q.get('obra', [''])[0]
                con = conectar()
                filas = con.execute('SELECT id, pagina, titulo FROM paginas WHERE titulo_obra=? ORDER BY pagina LIMIT 2000', (obra,)).fetchall()
                con.close()
                return self._json([dict(f) for f in filas])
            if ruta == '/api/obras':
                con = conectar()
                filas = con.execute("SELECT titulo_obra, volumen, count(*) n, min(id) first_id FROM paginas GROUP BY titulo_obra ORDER BY CASE WHEN titulo_obra='La Torre del Vigía' THEN 1 ELSE 0 END, volumen, titulo_obra").fetchall()
                con.close()
                return self._json([dict(f) for f in filas])
            if ruta == '/api/temas':
                letra = (q.get('letra', [''])[0] or '').upper()
                texto = (q.get('q', [''])[0] or '').strip()
                con = conectar()
                sql = 'SELECT id, termino, termino_es, nrefs FROM temas'
                cond = []; args = []
                if letra and letra != 'TODAS':
                    cond.append('letra=?'); args.append(letra.upper())
                if texto:
                    qn = '%' + sinacento(texto) + '%'
                    cond.append('(tnorm LIKE ? OR cnorm LIKE ? OR lower(termino) LIKE ?)')
                    args += [qn, qn, '%'+texto.lower()+'%']
                if cond: sql += ' WHERE ' + ' AND '.join(cond)
                sql += ' ORDER BY tnorm COLLATE NOCASE, termino LIMIT 500'
                if texto:
                    sql = sql.replace(' ORDER BY ', ' ORDER BY (tnorm LIKE ?) DESC, ')
                    args.append(qn)
                filas = con.execute(sql, args).fetchall()
                total = con.execute('SELECT count(*) FROM temas').fetchone()[0]
                con.close()
                return self._json({'total': total, 'items': [dict(f) for f in filas]})
            if ruta == '/api/temas_letras':
                con = conectar()
                filas = con.execute('SELECT letra l, count(*) n FROM temas GROUP BY letra ORDER BY l').fetchall()
                total = con.execute('SELECT count(*) FROM temas').fetchone()[0]
                con.close()
                return self._json({'total': total, 'letras': [dict(f) for f in filas]})
            if ruta == '/api/tema':
                tid = entero(q, 'id')
                con = conectar()
                f = con.execute('SELECT id, termino, termino_es, nrefs, cuerpo, cuerpo_es FROM temas WHERE id=?', (tid,)).fetchone()
                if not f:
                    con.close(); return self._json({'error': 'no encontrado'}, 404)
                lineas = json.loads(f['cuerpo'])
                lineas_es = json.loads(f['cuerpo_es']) if f['cuerpo_es'] else lineas
                lineas = _con_contexto(lineas)
                lineas_es = _con_contexto(lineas_es)
                refs = {}
                for ln in lineas:
                    for sg in ln[2]:
                        if sg[0] == 'r' and sg[1] not in refs:
                            rm = _mapa_refs().get(sg[1])
                            if rm: refs[sg[1]] = list(rm)
                # años que el índice original codificó como referencias: se muestran como texto
                for ln in lineas_es:
                    segs = ln[2] if len(ln) == 3 else (ln[1] if len(ln) > 1 else [])
                    for i, sg in enumerate(segs):
                        if (isinstance(sg, list) and len(sg) >= 3 and sg[0] == 'r'
                                and sg[1] not in refs and re.fullmatch(r'[;,]?\s*\d{3,4}', str(sg[2]).strip())):
                            segs[i] = ['t', sg[2]]
                # destino afinado por (referencia, palabra guía): párrafo y término exactos
                for ln in lineas_es:
                    segs = ln[2] if len(ln) == 3 else (ln[1] if len(ln) > 1 else [])
                    for sg in segs:
                        if not (isinstance(sg, list) and len(sg) >= 4 and sg[0] == 'r' and sg[3]):
                            continue
                        rc = _mapa_refctx().get((sg[1], sg[3]))
                        if rc:
                            sg.extend([rc[0], rc[1], rc[2]])
                try:
                    foto = []
                    for r in con.execute(
                            'SELECT f.pid, f.pos, f.term, f.ctx, p.pagina, p.titulo, p.texto '
                            'FROM temafoto f JOIN paginas p ON p.id=f.pid '
                            'WHERE f.tema_id=? ORDER BY p.pagina', (tid,)):
                        item = dict(r)
                        m = re.search(r'\[\[img:([^|\]]+)', item.pop('texto') or '')
                        item['img'] = m.group(1) if m else None
                        foto.append(item)
                except sqlite3.OperationalError:
                    foto = []
                con.close()
                return self._json({'id': f['id'], 'termino': f['termino'], 'termino_es': f['termino_es'] or f['termino'],
                                   'nrefs': f['nrefs'], 'lineas': lineas_es, 'lineas_en': lineas, 'refs': refs,
                                   'foto': foto})
            if ruta == '/api/estado':
                con = conectar()
                n = con.execute('SELECT count(*) FROM biblia').fetchone()[0]
                c = con.execute('SELECT count(*) FROM citas').fetchone()[0]
                p2 = con.execute('SELECT count(*) FROM paginas').fetchone()[0]
                tv = con.execute('SELECT count(*) FROM temas').fetchone()[0]
                con.close()
                return self._json({'paginas': p2, 'citas': c, 'versiculos': n, 'temas': tv})
        except Exception as e:
            return self._json({'error': str(e)}, 500)
        self.send_error(404)


_RESPALDO_CANDADO = threading.Lock()

def respaldo_automatico(dias=7):
    """Copia la base una vez al día (de forma consistente) y conserva las últimas."""
    import datetime, glob
    with _RESPALDO_CANDADO:
        try:
            carpeta = os.path.join(DATOS, 'respaldos')
            os.makedirs(carpeta, exist_ok=True)
            destino = os.path.join(carpeta, 'biblioteca-%s.db' % datetime.date.today().isoformat())
            origen = DB
            if os.path.exists(destino) and os.path.getmtime(origen) <= os.path.getmtime(destino):
                return
            # copia con la API de SQLite: consistente aunque haya escrituras
            tmp = destino + '.tmp.%d' % os.getpid()
            con = sqlite3.connect(origen, timeout=10)
            dst = sqlite3.connect(tmp)
            try:
                con.backup(dst)
            finally:
                dst.close(); con.close()
            ok_con = sqlite3.connect(tmp)
            try:
                ok = ok_con.execute('PRAGMA quick_check').fetchone()[0]
            finally:
                ok_con.close()
            if ok != 'ok':
                try: os.remove(tmp)
                except OSError: pass
                print('respaldo automático: verificación fallida', flush=True)
                return
            os.replace(tmp, destino)
            copias = sorted(glob.glob(os.path.join(carpeta, 'biblioteca-*.db')))
            for viejo in copias[:-dias]:
                os.remove(viejo)
        except Exception as e:
            print('respaldo automático:', e, flush=True)

_RESPALDO_SIS_CANDADO = threading.Lock()

def respaldo_sistema(dias=7):
    """Copia diaria de la aplicación y sus datos (no solo la base)."""
    import datetime, glob
    with _RESPALDO_SIS_CANDADO:
        try:
            carpeta = os.path.join(DATOS, 'respaldos')
            os.makedirs(carpeta, exist_ok=True)
            destino = os.path.join(carpeta, 'sistema-%s.tar.gz' % datetime.date.today().isoformat())
            # Las ilustraciones de img/ son estáticas y ya vienen en el instalador;
            # no se incluyen para que el respaldo y el arranque sigan siendo rápidos.
            rutas = ['app.html', 'asistente.py', 'tutorial.html', 'tutorial.pdf',
                     'tutorial-fotos.zip', 'manifest.json', 'sw.js', 'lanzador.sh',
                     'limpiar-sistema.sh', 'mdns.sh', 'pdf_vol.py', 'preparar-audio.py', 'icono.png',
                     'icono-192.png', 'icono-512.png', 'russell-icono.png', 'russell-192.png',
                     'russell-512.png', 'mana',
                     'audio-versiculos.md', 'auditoria-contenido.md', 'tomo2-revision.md',
                     'tomo3-revision.md', 'tomo4-revision.md', 'tomo5-revision.md', 'tomo6-revision.md',
                     'audio-biblia.md']
            if os.path.exists(destino):
                reciente = 0
                for rel in rutas:
                    ruta = os.path.join(BASE, rel)
                    if os.path.exists(ruta):
                        reciente = max(reciente, os.path.getmtime(ruta))
                if reciente <= os.path.getmtime(destino):
                    return
            tmp = destino + '.tmp.%d' % os.getpid()

            def sin_basura(ti):
                if '__pycache__' in ti.name:
                    return None
                return ti

            with tarfile.open(tmp, 'w:gz') as t:
                for rel in rutas:
                    ruta = os.path.join(BASE, rel)
                    if not os.path.exists(ruta):
                        continue
                    t.add(ruta, arcname=rel, filter=sin_basura)
            os.replace(tmp, destino)
            copias = sorted(glob.glob(os.path.join(carpeta, 'sistema-*.tar.gz')))
            for viejo in copias[:-dias]:
                os.remove(viejo)
        except Exception as e:
            print('respaldo del sistema:', e, flush=True)

def _bucle_respaldo():
    while True:
        time.sleep(3600)
        respaldo_automatico()
        respaldo_sistema()

def _respaldo_inicial():
    respaldo_automatico()
    respaldo_sistema()

if __name__ == '__main__':
    # Los respaldos iniciales no deben retrasar el arranque del servidor.
    threading.Thread(target=_respaldo_inicial, daemon=True).start()
    threading.Thread(target=_bucle_respaldo, daemon=True).start()
    print('Biblioteca en http://%s:%d' % (HOST, PUERTO), flush=True)
    ThreadingHTTPServer((HOST, PUERTO), Manejador).serve_forever()
