#!/usr/bin/env python3
"""Importa el Tomo 1 y Sombras del Tabernáculo a la Biblioteca Russell.

- Descarga la KJV en JSON (dominio público) y construye la tabla `biblia`.
- Limpia y divide los textos en capítulos.
- Detecta referencias bíblicas y las enlaza.
"""
import json, os, re, sqlite3, subprocess, sys, urllib.request

import pulir
import revistas

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, 'biblioteca.db')
TXT = os.path.join(BASE, 'texto')
KJV = os.path.join(BASE, 'kjv')

BOOKS = [
 'Genesis','Exodus','Leviticus','Numbers','Deuteronomy','Joshua','Judges','Ruth',
 '1Samuel','2Samuel','1Kings','2Kings','1Chronicles','2Chronicles','Ezra','Nehemiah',
 'Esther','Job','Psalms','Proverbs','Ecclesiastes','SongofSolomon','Isaiah','Jeremiah',
 'Lamentations','Ezekiel','Daniel','Hosea','Joel','Amos','Obadiah','Jonah','Micah',
 'Nahum','Habakkuk','Zephaniah','Haggai','Zechariah','Malachi','Matthew','Mark','Luke',
 'John','Acts','Romans','1Corinthians','2Corinthians','Galatians','Ephesians',
 'Philippians','Colossians','1Thessalonians','2Thessalonians','1Timothy','2Timothy',
 'Titus','Philemon','Hebrews','James','1Peter','2Peter','1John','2John','3John','Jude',
 'Revelation']

# Nombre canónico y abreviaturas habituales en los tomos de Russell.
ABREV = {
 'gen':'Genesis','ge':'Genesis','gn':'Genesis','genesis':'Genesis',
 'ex':'Exodus','exo':'Exodus','exod':'Exodus','exodus':'Exodus',
 'lev':'Leviticus','leviticus':'Leviticus','num':'Numbers','nu':'Numbers','numbers':'Numbers',
 'deut':'Deuteronomy','deu':'Deuteronomy','dt':'Deuteronomy','deuteronomy':'Deuteronomy',
 'josh':'Joshua','jos':'Joshua','joshua':'Joshua','judg':'Judges','jdg':'Judges','judges':'Judges',
 'ruth':'Ruth','1sam':'1Samuel','1sa':'1Samuel','1samuel':'1Samuel',
 '2sam':'2Samuel','2sa':'2Samuel','2samuel':'2Samuel',
 '1kings':'1Kings','1kgs':'1Kings','1ki':'1Kings','2kings':'2Kings','2kgs':'2Kings','2ki':'2Kings',
 '1chron':'1Chronicles','1ch':'1Chronicles','1chronicles':'1Chronicles',
 '2chron':'2Chronicles','2ch':'2Chronicles','2chronicles':'2Chronicles',
 'ezra':'Ezra','neh':'Nehemiah','nehemiah':'Nehemiah','esth':'Esther','est':'Esther','esther':'Esther',
 'job':'Job','psa':'Psalms','ps':'Psalms','psalm':'Psalms','psalms':'Psalms',
 'prov':'Proverbs','pro':'Proverbs','pr':'Proverbs','proverbs':'Proverbs',
 'eccl':'Ecclesiastes','ecc':'Ecclesiastes','ecclesiastes':'Ecclesiastes',
 'song':'SongofSolomon','cant':'SongofSolomon','songofsolomon':'SongofSolomon',
 'isa':'Isaiah','is':'Isaiah','isaiah':'Isaiah','jer':'Jeremiah','jeremiah':'Jeremiah',
 'lam':'Lamentations','lamentations':'Lamentations','ezek':'Ezekiel','eze':'Ezekiel','ezekiel':'Ezekiel',
 'dan':'Daniel','daniel':'Daniel','hos':'Hosea','hosea':'Hosea','joel':'Joel','amos':'Amos',
 'obad':'Obadiah','obadiah':'Obadiah','jonah':'Jonah','jon':'Jonah',
 'mic':'Micah','micah':'Micah','nah':'Nahum','nahum':'Nahum','hab':'Habakkuk','habakkuk':'Habakkuk',
 'zeph':'Zephaniah','zep':'Zephaniah','zephaniah':'Zephaniah','hag':'Haggai','haggai':'Haggai',
 'zech':'Zechariah','zec':'Zechariah','zechariah':'Zechariah','mal':'Malachi','malachi':'Malachi',
 'matt':'Matthew','mat':'Matthew','mt':'Matthew','matthew':'Matthew',
 'mark':'Mark','mk':'Mark','mr':'Mark','luke':'Luke','lk':'Luke','lucas':'Luke',
 'john':'John','jn':'John','joh':'John','acts':'Acts','act':'Acts',
 'rom':'Romans','ro':'Romans','romans':'Romans',
 '1cor':'1Corinthians','1co':'1Corinthians','1corinthians':'1Corinthians',
 '2cor':'2Corinthians','2co':'2Corinthians','2corinthians':'2Corinthians',
 'gal':'Galatians','ga':'Galatians','galatians':'Galatians',
 'eph':'Ephesians','ephesians':'Ephesians','phil':'Philippians','php':'Philippians','philippians':'Philippians',
 'col':'Colossians','colossians':'Colossians',
 '1thess':'1Thessalonians','1th':'1Thessalonians','1thessalonians':'1Thessalonians',
 '2thess':'2Thessalonians','2th':'2Thessalonians','2thessalonians':'2Thessalonians',
 '1tim':'1Timothy','1ti':'1Timothy','1timothy':'1Timothy',
 '2tim':'2Timothy','2ti':'2Timothy','2timothy':'2Timothy','titus':'Titus','tit':'Titus',
 'philem':'Philemon','phlm':'Philemon','philemon':'Philemon',
 'heb':'Hebrews','hebrews':'Hebrews','james':'James','jas':'James',
 '1pet':'1Peter','1pe':'1Peter','1peter':'1Peter','2pet':'2Peter','2pe':'2Peter','2peter':'2Peter',
 '1john':'1John','1jn':'1John','1jo':'1John','2john':'2John','2jn':'2John','2jo':'2John',
 '3john':'3John','3jn':'3John','3jo':'3John','jude':'Jude','jud':'Jude',
 'rev':'Revelation','revelation':'Revelation','apoc':'Revelation',
}

def canon(s):
    k = re.sub(r'[^a-z0-9]', '', s.lower())
    return ABREV.get(k)

def download_kjv():
    os.makedirs(KJV, exist_ok=True)
    api = json.load(urllib.request.urlopen('https://api.github.com/repos/aruljohn/Bible-kjv/contents/', timeout=30))
    nombres = [x['name'] for x in api if x['type'] == 'file' and x['name'].endswith('.json') and x['name'] != 'Books.json']
    for n in nombres:
        dest = os.path.join(KJV, n)
        if os.path.isfile(dest) and os.path.getsize(dest) > 1000:
            continue
        print('KJV', n, flush=True)
        url = 'https://raw.githubusercontent.com/aruljohn/Bible-kjv/master/' + urllib.parse.quote(n)
        data = urllib.request.urlopen(url, timeout=30).read()
        open(dest, 'wb').write(data)

def crear_db():
    con = sqlite3.connect(DB)
    con.executescript('''
    PRAGMA journal_mode=WAL;
    DROP TABLE IF EXISTS obras;
    DROP TABLE IF EXISTS paginas;
    DROP TABLE IF EXISTS citas;
    DROP TABLE IF EXISTS biblia;
    DROP TABLE IF EXISTS busqueda;
    CREATE TABLE obras(id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, descripcion TEXT, color TEXT);
    CREATE TABLE paginas(id INTEGER PRIMARY KEY, obra_id INTEGER, orden INTEGER, titulo TEXT, texto TEXT);
    CREATE TABLE citas(id INTEGER PRIMARY KEY, pagina_id INTEGER, inicio INTEGER, fin INTEGER,
        ref_texto TEXT, libro TEXT, capitulo INTEGER, v_ini INTEGER, v_fin INTEGER);
    CREATE TABLE biblia(libro TEXT, capitulo INTEGER, versiculo INTEGER, texto TEXT,
        PRIMARY KEY(libro, capitulo, versiculo));
    CREATE TABLE IF NOT EXISTS traducciones(hash TEXT PRIMARY KEY, texto_en TEXT, texto_es TEXT);
    CREATE VIRTUAL TABLE busqueda USING fts5(texto, titulo, content='paginas', content_rowid='id',
        tokenize='unicode61 remove_diacritics 2');
    ''')
    con.commit()
    return con

def importar_kjv(con):
    for n in sorted(os.listdir(KJV)):
        if not n.endswith('.json') or n == 'Books.json':
            continue
        try:
            d = json.load(open(os.path.join(KJV, n), encoding='utf-8'))
        except Exception:
            continue
        libro = d.get('book') or n[:-5]
        libro = libro.replace(' ', '')
        for cap in d.get('chapters', []):
            c = int(cap['chapter'])
            for v in cap.get('verses', []):
                con.execute('insert or replace into biblia values (?,?,?,?)',
                            (libro, c, int(v['verse']), v['text'].strip()))
    con.commit()
    print('KJV versículos', con.execute('select count(*) from biblia').fetchone()[0], flush=True)

def limpiar(texto):
    t = texto.replace('\f', '\n')
    t = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', ' ', t)
    lineas = []
    for ln in t.splitlines():
        s = ln.strip()
        s = re.sub(r'^(?:R\d+\s*:\s*)?page\s+\d+\s*', '', s, flags=re.I).strip()
        if not s:
            lineas.append('')
            continue
        if s.lower() == 'flyleaf':
            continue
        if re.fullmatch(r'[A-Z]?\d{1,4}', s):      # A10, B123
            continue
        if re.fullmatch(r'[A-Z]?[ivxlcdm]{1,6}', s, re.I):  # Aii, iv
            continue
        lineas.append(s)
    # unir líneas en párrafos
    parrafos, buf = [], []
    for s in lineas:
        if s == '':
            if buf:
                parrafos.append(' '.join(buf)); buf = []
        else:
            buf.append(s)
    if buf:
        parrafos.append(' '.join(buf))
    # Unir párrafos partidos por una marca de página: el anterior queda sin
    # puntuación final y el siguiente continúa en minúscula o con conector.
    unidos = []
    for p in parrafos:
        p = p.replace('--', '—').strip()
        if not p:
            continue
        if (unidos and (not re.search(r'[.!?;:»"—–]$', unidos[-1])
                        or re.search(r'[,;]$', unidos[-1]))
                and not re.search(r'\d+:\d+(?:[-,]\d+)?[.,;]?$', unidos[-1])
                and (p[:1].islower() or re.match(r'(and|but|or|for|that|which|who|whom|whose|where|when|while|as|in|of|to|with|from|by|on|at|it|this|these|those)\b', p, re.I))):
            unidos[-1] += ' ' + p
        else:
            unidos.append(p)
    final = []
    for p in unidos:
        if len(p) <= 1600:
            final.append(p)
            continue
        frases = re.split(r'(?<=[.!?])\s+', p)
        buf = ''
        for f in frases:
            if len(buf) + len(f) + 1 > 1400 and buf:
                final.append(buf)
                buf = f
            else:
                buf = (buf + ' ' + f).strip()
        if buf:
            final.append(buf)
    return '\n\n'.join(final)

def recortar_inicio(texto):
    """Quita el título repetido y la línea de sinopsis que trae el PDF."""
    ps = [p.strip() for p in texto.split('\n\n') if p.strip()]
    for i, p in enumerate(ps):
        # La sinopsis del PDF es una línea larga llena de guiones; el cuerpo
        # empieza con una frase de prosa y tiene muy pocos guiones.
        if (len(p) > 200 and (p.count('--') + p.count('—')) < 3
                and re.match(r'(THE|IN|AS|EVEN|EVERY|WE|OUR|THIS|IT|IF|NO|ONE|MANY|NOT|BUT|WHEN|WHERE|WHY|HOW|ALL|GOD|CHRIST)\b', p, re.I)):
            return '\n\n'.join(ps[i:])
    return texto


def dividir_volumen1():
    t = open(os.path.join(TXT, 'volume1.txt'), encoding='utf-8').read()
    titulos = [
        "Earth's Night of Sin to Terminate in a Morning of Joy",
        "The Existence of a Supreme Intelligent Creator Established",
        "The Bible as a Divine Revelation Viewed in the Light of Reason",
        "The Epochs and Dispensations Marked in the Development of the Divine Plan",
        '"The Mystery Hid from Ages and from Generations, But Now Made Manifest"',
        "Our Lord's Return: Its Object, the Restitution of All Things",
        "The Permission of Evil and Its Relation to God's Plan",
        "The Day of Judgment",
        "Ransom and Restitution",
        "Spiritual and Human Natures Separate and Distinct",
        "The Three Ways: The Broad Way, the Narrow Way, the Highway",
        "Explanation of the Chart of the Ages",
        "The Kingdoms of This World",
        "The Kingdom of God",
        "The Day of Jehovah",
        "Concluding Thoughts",
    ]
    # El PDF marca cada capítulo con \x02\x06. Es la única separación fiable:
    # las frases de los títulos también aparecen en el prólogo y el índice.
    marcas = [m.start() for m in re.finditer('\x02\x06', t)]
    caps = []
    for i, pos in enumerate(marcas):
        fin = marcas[i+1] if i+1 < len(marcas) else len(t)
        titulo = titulos[i] if i < len(titulos) else 'Chapter %d' % (i+1)
        caps.append((titulo, recortar_inicio(limpiar(t[pos:fin]))))
    return caps

def dividir_shadows():
    t = open(os.path.join(TXT, 'shadows.txt'), encoding='utf-8').read()
    titulos = [
        'The Typical Tabernacle',
        'Israelites, Levites and the Priesthood',
        'Consecrating the Priesthood',
        'The Great "Day of Atonement"',
        'Another Type of the Atonement',
        'Sacrifices Subsequent to the "Day of Atonement"',
        '"The Ashes of a Heifer Sprinkling the Unclean"',
        'Other Significant Types',
    ]
    marcas = [m.start() for m in re.finditer(r'CHAPTER\s+[IVX]+', t, re.I)]
    caps = []
    for i, pos in enumerate(marcas):
        fin = marcas[i+1] if i+1 < len(marcas) else len(t)
        titulo = 'Chapter %s — %s' % (roman(i+1), titulos[i] if i < len(titulos) else '')
        caps.append((titulo, recortar_inicio(limpiar(t[pos:fin]))))
    return caps



def dividir_por_estudios(texto, titulos):
    """Divide los tomos II–IV por sus encabezados STUDY I, STUDY II..."""
    marcas = [m.start() for m in re.finditer(r'STUDY\s+[IVX]+', texto)]
    caps = []
    for i, pos in enumerate(marcas):
        fin = marcas[i+1] if i+1 < len(marcas) else len(texto)
        titulo = titulos[i] if i < len(titulos) else 'Study %d' % (i+1)
        caps.append((titulo, recortar_inicio(limpiar(texto[pos:fin]))))
    return caps


def dividir_por_titulos(texto, titulos):
    """Divide los tomos V–VI por sus títulos de capítulo en mayúsculas."""
    body = texto.find("AUTHOR'S FOREWORD")
    cursor = body if body >= 0 else 0
    marcas = []
    for titulo in titulos:
        pat = re.escape(titulo).replace(r'\ ', r'\s+')
        m = re.search(pat, texto[cursor:], re.I)
        if not m:
            print('AVISO: no encontrado', titulo, flush=True)
            continue
        pos = cursor + m.start()
        marcas.append((pos, titulo))
        cursor = pos + len(m.group(0))
    caps = []
    for i, (pos, titulo) in enumerate(marcas):
        fin = marcas[i+1][0] if i+1 < len(marcas) else len(texto)
        caps.append((titulo, recortar_inicio(limpiar(texto[pos:fin]))))
    return caps


def dividir_por_pares(texto, pares):
    """Como dividir_por_titulos, pero el marcador puede ser una frase corta."""
    body = texto.find("AUTHOR'S FOREWORD")
    cursor = body if body >= 0 else 0
    marcas = []
    for marcador, titulo in pares:
        pat = re.escape(marcador).replace(r'\ ', r'\s+')
        m = re.search(pat, texto[cursor:], re.I)
        if not m:
            print('AVISO: no encontrado', marcador, flush=True)
            continue
        pos = cursor + m.start()
        marcas.append((pos, titulo))
        cursor = pos + len(m.group(0))
    caps = []
    for i, (pos, titulo) in enumerate(marcas):
        fin = marcas[i+1][0] if i+1 < len(marcas) else len(texto)
        caps.append((titulo, recortar_inicio(limpiar(texto[pos:fin]))))
    return caps


TOWERS = '/home/carlos/Imágenes/Documentos compartidos/Pictures/Imágenes/Bible Study Library/Library/Library/Russell/TOWERS'
MANNA = '/home/carlos/Imágenes/Documentos compartidos/Pictures/Imágenes/Bible Study Library/Library/Library/Devotion/MANNA/MANNA.PDF'
MESES = {'JAN':1,'FEB':2,'MAR':3,'APR':4,'MAY':5,'JUN':6,'JUL':7,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DEC':12}
NOMBRES = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}



def importar_towers(con):
    if not os.path.isdir(TOWERS):
        print('AVISO: no está la carpeta TOWERS', flush=True)
        return
    cur = con.execute("insert into obras(titulo,autor,descripcion,color) values (?,?,?,?)",
        ('The Watch Tower', 'Charles Taze Russell',
         "Zion's Watch Tower and Herald of Christ's Presence, 1879–1916. English originals.", '#4a2f5a'))
    oid = cur.lastrowid
    archivos = []
    for d in sorted(os.listdir(TOWERS)):
        if not d.upper().startswith('ZWT'):
            continue
        anio = int(re.sub(r'\D', '', d) or 0)
        for fn in sorted(os.listdir(os.path.join(TOWERS, d))):
            if not fn.lower().endswith('.pdf'):
                continue
            m = re.search(r'(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)', fn.upper())
            if not m:
                continue
            mes = MESES[m.group(1)]
            archivos.append((anio, mes, os.path.join(TOWERS, d, fn)))
    archivos.sort()
    cache = os.path.join(TXT, 'towers')
    os.makedirs(cache, exist_ok=True)
    crudos = []
    for anio, mes, ruta in archivos:
        guardado = os.path.join(cache, '%d-%02d.txt' % (anio, mes))
        if os.path.isfile(guardado) and os.path.getmtime(guardado) >= os.path.getmtime(ruta):
            out = open(guardado, encoding='utf-8', errors='replace').read()
        else:
            try:
                out = subprocess.run(['pdftotext', '-layout', ruta, '-'], capture_output=True,
                                     text=True, timeout=60).stdout
            except Exception:
                continue
            open(guardado, 'w', encoding='utf-8').write(out)
        cuerpo = revistas.preparar(out)
        # Si el recorte deja muy poco, se conserva el número completo sin avisos.
        if len(cuerpo) < max(12000, int(len(out) * 0.15)):
            cuerpo = revistas.quitar_avisos(out)
        texto = revistas.quitar_restos(revistas.quitar_cabecera(limpiar(cuerpo)))
        if len(texto) < 300:
            # Números que sólo traían el aviso de que se sustituían por un tomo.
            texto = ('Special issue notice: this number was replaced by Volume IV of '
                     'Studies in the Scriptures.')
            if len(cuerpo) < 200:
                continue
        crudos.append(('%s %d' % (NOMBRES[mes], anio), texto))
    vocab = pulir.construir_vocabulario([t for _, t in crudos])
    n = 0
    for mes_anio, texto in crudos:
        texto = pulir.pulir(texto, vocab)
        if len(texto) < 300:
            continue
        titulo = 'The Watch Tower — ' + mes_anio
        n += 1
        cur = con.execute('insert into paginas(obra_id,orden,titulo,texto) values (?,?,?,?)',
                          (oid, n, titulo, texto))
        pid = cur.lastrowid
        for (a, b, ref, libro, cap, v1, v2) in citas_de(texto):
            con.execute('insert into citas(pagina_id,inicio,fin,ref_texto,libro,capitulo,v_ini,v_fin) values (?,?,?,?,?,?,?,?)',
                        (pid, a, b, ref, libro, cap, v1, v2))
        con.commit()
    print('Watch Tower', n, 'números', flush=True)


MESES_EN = ['January','February','March','April','May','June','July','August','September','October','November','December']


def importar_manna(con):
    """Importa Daily Heavenly Manna: 366 lecturas diarias."""
    if not os.path.isfile(MANNA):
        return
    cur = con.execute("insert into obras(titulo,autor,descripcion,color) values (?,?,?,?)",
        ('Daily Heavenly Manna', 'Charles Taze Russell',
         'Daily devotions with a Scripture text and a Watch Tower extract. 366 readings.', '#6b5a1d'))
    oid = cur.lastrowid
    txt = subprocess.run(['pdftotext', '-layout', MANNA, '-'], capture_output=True, text=True, timeout=90).stdout
    txt = txt.replace('\f', '\n')
    pat = re.compile(r'(?m)^\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})\s*$')
    marcas = [(m.start(), m.group(1), int(m.group(2))) for m in pat.finditer(txt)]
    n = 0
    for i, (pos, mes, dia) in enumerate(marcas):
        fin = marcas[i+1][0] if i+1 < len(marcas) else len(txt)
        frag = txt[pos:fin]
        frag = re.sub(r'^\s*'+re.escape(mes)+r'\s+'+str(dia)+r'\s*', '', frag, count=1)
        texto = limpiar(frag)
        if len(texto) < 100:
            continue
        n += 1
        cur = con.execute('insert into paginas(obra_id,orden,titulo,texto) values (?,?,?,?)',
                          (oid, n, '%s %d' % (mes, dia), texto))
        pid = cur.lastrowid
        for (a, b, ref, libro, cap, v1, v2) in citas_de(texto):
            con.execute('insert into citas(pagina_id,inicio,fin,ref_texto,libro,capitulo,v_ini,v_fin) values (?,?,?,?,?,?,?,?)',
                        (pid, a, b, ref, libro, cap, v1, v2))
    print('Manna', n, 'lecturas', flush=True)

def roman(n):
    r = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
    return r[n-1] if 0 < n <= len(r) else str(n)

PAT = re.compile(
    r'(?<![\w])'
    r'((?:[1-3]\s*)?[A-Z][A-Za-z.]{1,18})\s*\.?\s*'
    r'(\d{1,3})\s*[:.]\s*(\d{1,3})'
    r'(?:\s*[-–]\s*(\d{1,3}))?'
    r'(?:\s*[,;]\s*(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?)?'
)

def citas_de(texto):
    out = []
    for m in PAT.finditer(texto):
        libro = canon(m.group(1))
        if not libro:
            continue
        cap, v1 = int(m.group(2)), int(m.group(3))
        vs = [int(x) for x in m.groups()[3:] if x]
        v2 = max([v1] + vs)
        if not (1 <= cap <= 150 and 1 <= v1 <= 200):
            continue
        out.append((m.start(), m.end(), m.group(0).strip(), libro, cap, v1, v2))
    return out

def main():
    download_kjv()
    con = crear_db()
    importar_kjv(con)
    cur = con.execute("insert into obras(titulo,autor,descripcion,color) values (?,?,?,?)",
        ('The Divine Plan of the Ages', 'Charles Taze Russell',
         'Studies in the Scriptures, Series I. The English original.', '#1d3a6b'))
    obra1 = cur.lastrowid
    cur = con.execute("insert into obras(titulo,autor,descripcion,color) values (?,?,?,?)",
        ('Tabernacle Shadows of the Better Sacrifices', 'Charles Taze Russell',
         'A helping hand for the Royal Priesthood. The English original.', '#6b4a1d'))
    obra2 = cur.lastrowid
    libros = [
        (obra1, dividir_volumen1()),
        (obra2, dividir_shadows()),
        (None, None),
    ]
    # Tomos II, III y IV
    mas = [
        ('The Time is at Hand', 'Studies in the Scriptures, Series II. The English original.', '#26466f', 'VOLUME2.txt', [
            'Special Times and Seasons Divinely Appointed', 'Bible Chronology',
            'The Fulfilment of Time Prophecy at the First Advent of Christ',
            'The Times of the Gentiles', "The Manner of Our Lord's Return and Appearing",
            "Earth's Great Jubilee", 'The Parallel Dispensations', 'Elias Shall First Come',
            'The Man of Sin—Antichrist', 'The Time is at Hand']),
        ('Thy Kingdom Come', 'Studies in the Scriptures, Series III. The English original.', '#3a4a6b', 'VOLUME3.txt', [
            '"Thy Kingdom Come"', '"The Time of the End," or "Day of His Preparation"',
            'Days of Waiting for the Kingdom', 'The Cleansing of the Sanctuary',
            'The Time of Harvest', 'The Work of Harvest',
            'The Deliverance and Exaltation of the Church', 'The Restoration of Israel',
            'Thy God Reigneth!', 'A Kindly Comment on This Chapter',
            "The Testimony of God's Stone Witness and Prophet, the Great Pyramid in Egypt"]),
        ('The Battle of Armageddon', 'Studies in the Scriptures, Series IV. The English original.', '#5a3a2a', 'VOLUME4.txt', [
            '"The Day of Vengeance"', '"The Doom of Babylon"—"Christendom"',
            'The Necessity and Justice of the Day of Vengeance',
            'Babylon Arraigned Before the Great Court',
            'Babylon Before the Great Court: Her Confusion—National',
            'Babylon Before the Great Court: Her Confusion—Ecclesiastical',
            "The Nations Assembled and the Preparation of the Elements for the Great Fire of God's Indignation",
            'The Cries of the Reapers', 'The Conflict Irrepressible',
            'Proposed Remedies—Social and Financial', 'The Battle of Armageddon',
            "Our Lord's Great Prophecy",
            'The Establishment of the Kingdom, and How It Will Manifest Itself',
            "Jehovah's Footstool Made Glorious"]),
    ]
    for titulo, desc, color, archivo, titulos in mas:
        cur = con.execute("insert into obras(titulo,autor,descripcion,color) values (?,?,?,?)",
                          (titulo, 'Charles Taze Russell', desc, color))
        oid = cur.lastrowid
        texto = open(os.path.join(TXT, archivo), encoding='utf-8').read()
        libros.append((oid, dividir_por_estudios(texto, titulos)))
    mas2 = [
        ('The Atonement Between God and Man', 'Studies in the Scriptures, Series V. The English original.', '#2f5a4a', 'VOLUME5.txt', [
            ('THE FACT AND PHILOSOPHY OF', 'The Fact and Philosophy of the Atonement'),
            ('THE AUTHOR OF THE ATONEMENT', 'The Author of the Atonement'),
            ('THE ONLY BEGOTTEN ONE', 'The Mediator of the Atonement: The Only Begotten One'),
            ('THE UNDEFILED ONE', 'The Mediator of the Atonement: The Undefiled One'),
            ('"MADE LIKE UNTO HIS BRETHREN"', 'The Mediator of the Atonement: Made Like unto His Brethren'),
            ("DAVID'S SON AND DAVID'S LORD", "The Mediator of the Atonement: David's Son and David's Lord"),
            ('THE CHANNEL OF THE ATONEMENT', 'The Channel of the Atonement: The Holy Spirit of God'),
            ('THE BAPTISM, WITNESS AND SEAL', 'The Baptism, Witness and Seal of the Spirit of At-one-ment'),
            ('THE SPIRIT OF A SOUND MIND', 'The Spirit of a Sound Mind'),
            ('SUPPOSED OBJECTIONS CONSIDERED', 'The Holy Spirit of At-one-ment: Supposed Objections Considered'),
            ('THE SUBJECT OF THE ATONEMENT', 'The Subject of the Atonement—Man'),
            ('HOPES FOR LIFE EVERLASTING', 'Hopes for Life Everlasting and Immortality Secured by the Atonement'),
            ('THE NECESSITY FOR THE ATONEMENT', 'The Necessity for the Atonement—The Curse'),
            ('"A RANSOM FOR ALL"', 'A Ransom for All: The Only Basis for At-one-ment'),
            ('THE MINISTRY OF RECONCILIATION', 'The Ministry of Reconciliation or At-one-ment')]),
        ('The New Creation', 'Studies in the Scriptures, Series VI. The English original.', '#5a4a2a', 'VOLUME6.txt', [
            'In the Beginning', 'The New Creation', 'The Call of the New Creation',
            'The New Creation Predestinated', 'The Organization of the New Creation',
            'Order and Discipline in the New Creation', 'The Law of the New Creation',
            'The Rest, or Sabbath of the New Creation', 'The Judgment of the New Creation',
            'The Baptism of the New Creation', 'The Passover of the New Creation',
            'Marital and Other Privileges and Obligations of the New Creation',
            'Parental Obligations of the New Creation',
            'Sundry Earthly Obligations of the New Creation',
            'The Foes and Besetments of the New Creation',
            'The Present Inheritance of the New Creation',
            'The Resurrection Inheritance of the New Creation']),
    ]
    for titulo, desc, color, archivo, titulos in mas2:
        cur = con.execute("insert into obras(titulo,autor,descripcion,color) values (?,?,?,?)",
                          (titulo, 'Charles Taze Russell', desc, color))
        oid = cur.lastrowid
        texto = open(os.path.join(TXT, archivo), encoding='utf-8').read()
        if titulos and isinstance(titulos[0], tuple):
            libros.append((oid, dividir_por_pares(texto, titulos)))
        else:
            libros.append((oid, dividir_por_titulos(texto, titulos)))
    importar_towers(con)
    importar_manna(con)
    total = 0
    for obra_id, caps in libros:
        if not caps:
            continue
        for i, (titulo, texto) in enumerate(caps, 1):
            if len(texto) < 100:
                continue
            cur = con.execute('insert into paginas(obra_id,orden,titulo,texto) values (?,?,?,?)',
                              (obra_id, i, titulo, texto))
            pid = cur.lastrowid
            for (a, b, ref, libro, cap, v1, v2) in citas_de(texto):
                con.execute('insert into citas(pagina_id,inicio,fin,ref_texto,libro,capitulo,v_ini,v_fin) values (?,?,?,?,?,?,?,?)',
                            (pid, a, b, ref, libro, cap, v1, v2))
            total += 1
    con.execute("insert into busqueda(busqueda) values('rebuild')")
    con.commit()
    print('capítulos', total, 'páginas', con.execute('select count(*) from paginas').fetchone()[0],
          'citas', con.execute('select count(*) from citas').fetchone()[0], flush=True)
    con.close()

if __name__ == '__main__':
    main()
