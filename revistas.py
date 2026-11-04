"""Selección de los artículos de estudio de The Watch Tower.

Los PDFs traen el número completo: portada con publicidad, avisos de
suscripción, noticias de convenciones, cartas de lectores, informes y
poemas.  Este módulo deja sólo los artículos de investigación bíblica.

Cuando el número trae índice (CONTENTS) se recorta artículo por artículo
siguiendo sus títulos.  Cuando no lo trae (números antiguos, de un solo
tema) se conserva el cuerpo y se quitan los bloques fijos de avisos.
"""

import re

# Entradas del índice que no son artículos de estudio.
NO_ARTICULO = (
    'poem', 'interesting letters', 'letters', 'items', 'item', 'convention',
    'notices', 'notice', 'higher prices', 'subscriptions', 'business communications',
    'pilgrim', 'colporteur', 'obituary', 'marriage', 'deaths', 'financial',
    'reports', 'report', 'berean', 'sermons weekly', 'public ministries',
    'tabernacle every sunday', 'volunteer', 'hymn', 'booklet', 'chart',
    'edition', 'sample copies', 'price', 'announcement', 'questions',
    'portrait', 'funeral', 'floral', 'oration', 'address at', 'addresses at',
    'closing scenes', 'biography', 'will and testament', 'photo',
)

# Secciones que cierran el cuerpo de un número.
CORTES = (r'INTERESTING LETTERS', r'LETTERS EXPRESSING',
          r'PUBLIC MINISTRIES OF THE TRUTH', r'BROOKLYN TABERNACLE EVERY SUNDAY',
          r'ENTERED AS SECOND-CLASS', r'STUDIES IN THE SCRIPTURES',
          r'VOLUNTEER MATTER', r'BEREAN (?:STUDIES|QUESTIONS)', r'HYMNS OF DAWN',
          r'BLUE PRINT CHART', r"BROTHER RUSSELL.S SERMONS", r'SEMI-MONTHLY',
          r'SUBSCRIPTIONS AND BUSINESS', r'PUBLISHED BY')

CORTE_RE = re.compile(r'(?im)^[ \t]*(?:\d+[ \t]*)?(?:%s)[ \t]*$' % '|'.join(CORTES))

# Bloques fijos de aviso que aparecen en cualquier número.
AVISOS = (
    # Cabecera del número
    r'(?im)^[ \t]*(?:SEMI-?)?MONTHLY[ \t]*$',
    r'(?im)^[ \t]*VOL\.[ \t]+[IVXLC]+[^\n]*$',
    r'(?im)^[ \t]*\d{4}\s*--\s*A\.\s*M\.\s*\d+[ \t]*$',
    r'(?im)^[ \t]*A\.\s*D\.\s*\d{4}\s*--\s*A\.\s*M\.\s*\d+[ \t]*$',
    r'(?im)^[ \t]*PITTSBURGH,? PA\.[^\n]*\d{4}[^\n]*$',
    r'(?im)^[ \t]*(?:NO|NUM|NOS)\.?[ \t]*\d+[^\n]*$',
    r'(?im)^[ \t]*[A-Z][A-Z .,]*?\b(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER),?[ \t]+\d{4}\.?[ \t]*$',
    r'(?ims)^[ \t]*REGULAR CONTRIBUTORS[^\n]*$.*?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|^[ \t]*=+[ \t]*$|\Z)',
    # Indice, portada y datos de la sociedad
    r'(?ims)^[ \t]*CONTENTS\.?[ \t]*$.*?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|\Z)',
    r'(?ims)^[ \t]*PUBLISHED BY[^\n]*$.*?(?=^[ \t]*ENTERED AS SECOND-CLASS[^\n]*$|^[ \t]*Please address the SOCIETY[^\n]*$|^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$)',
    r'(?ims)^[ \t]*The Watch Tower Editorial Committee:.*?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|\Z)',
    r'(?im)^[ \t]*Please address the SOCIETY[^\n]*$',
    # Publicidad fija de la sociedad
    r'(?ims)^[ \t]*STUDIES IN THE SCRIPTURES[^\n]*$.*?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|^[ \t]*(?:CONTENTS|PUBLISHED BY)[ \t]*$|\Z)',
    r'(?ims)^[ \t]*SUBSCRIPTIONS AND BUSINESS COMMUNICATIONS[ \t]*$.*?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|\Z)',
    r'(?is)\bTHIS JOURNAL AND ITS MISSION\b.*?CHARLES T\. RUSSELL,\s*Editor\.?',
    r'(?is)\bA POST OFFICE THIEF IS STILL ROBBING OUR MAIL!.*?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|\Z)',
    r'(?ims)^[ \t]*VOLUNTEER MATTER[ \t]*$.*?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|\Z)',
    # Cabecera de la segunda mitad del número (1892-1894)
    r"(?is)Zion['\u2019]s Watch Tower and Herald of Christ['\u2019]s Presence\.\s*Published Twice a Month\..{0,1200}?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|\Z)",
    # Avisos postales y de envío
    r"(?ims)^[ \t]*ALLEGHENY,? PA\.,? [A-Z]+ [0-9]{4},?[ \t]*$.*?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|\Z)",
    r"(?ims)^[ \t]*NEW POSTAL RULINGS.*?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|\Z)",
    # Publicidad de Biblias y tarjetas
    r"(?ims)^[ \t]*(?:Combination |Divinity Circuit |Cambridge India Paper )?Teachers['\u2019]? Bibles[.,]?(?:[ \t]+described[^\n]*)?[ \t]*$.*?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|\Z)",
    r"(?ims)^[ \t]*Motto Cards\..*?(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|\Z)",
    # Secciones de cierre
    r'(?ims)^[ \t]*PUBLIC MINISTRIES OF THE TRUTH[ \t]*\.?[ \t]*$.*\Z',
    r'(?ims)^[ \t]*BROOKLYN TABERNACLE[^\n]*$.*\Z',
    r'(?ims)^[ \t]*INTERESTING LETTERS[^\n]*$.*\Z',
    r'(?ims)^[ \t]*LETTERS EXPRESSING[^\n]*$.*\Z',
    r'(?ims)^[ \t]*(?:BEREAN (?:STUDIES|QUESTIONS)[^\n]*)$.*\Z',
)


def entradas(texto):
    """Devuelve ([(titulo, pagina, principal)], fin del bloque CONTENTS)."""
    for m in re.finditer(r'(?m)^\s*CONTENTS\.?\s*$', texto, re.I):
        st = m.end()
        fin = re.search(r'(?m)^\s*(?:page\s+\d+|R\d+\s*:\s*page\s+\d+|PUBLISHED BY)\s*$',
                        texto[st:])
        en = st + (fin.start() if fin else 4000)
        buf, sangria, out = [], 0, []
        for ln in texto[st:en].splitlines():
            s = ln.strip()
            if not s:
                continue
            if not buf:
                sangria = len(ln) - len(ln.lstrip(' \t'))
            mm = (re.match(r'^(.*?)(?:\.\s*){2,}(\d{1,3})\s*$', s)
                  or re.match(r'^(.*?\S)\s{2,}(\d{1,3})\s*$', s)
                  or re.match(r"^(.*?[A-Za-z)\"\u201d'])\s+(\d{1,3})\s*$", s))
            if mm:
                out.append(((' '.join(buf) + ' ' + mm.group(1)).strip(),
                            int(mm.group(2)), sangria < 2))
                buf, sangria = [], 0
            elif s.upper() not in ('CONTENTS', '----------'):
                buf.append(s)
        if out:
            return out, en
    return [], 0


def buscar_titulo(texto, titulo, desde):
    """Localiza el título en el cuerpo, tolerando saltos y puntuación."""
    palabras = [p for p in re.findall(r"[A-Za-z0-9']+", titulo) if len(p) > 1]
    if not palabras:
        return None
    patron = r'[^A-Za-z0-9]{1,40}'.join(re.escape(w) for w in palabras[:6])
    m = re.search(patron, texto[desde:], re.I)
    return desde + m.start() if m else None


# Cabecera de la revista: título, lema, volumen, editor, colaboradores,
# condiciones de suscripción y dirección. Se repite en cada número.
PORTADA = re.compile(
    r"(?is)(?:SUPPLEMENT\s+TO\s+)?ZION['\u2019]?S\s+WATCH\s+TOWER[,.]?\s*"
    r"(?:AND\s+)?[\"\u201c']?HERALD\s+OF\s+CHRIST['\u2019]?S\s+PRESENCE[\"\u201d']?[,.]?"
    r".{0,3000}?"
    r"(?=^[ \t]*(?:R\d+\s*:\s*)?page\s+\d+[ \t]*$|^[ \t]*PITTSBURGH[^\n]*\d{4}[^\n]*$|\Z)",
    re.M)

# Línea de saludo de los números antiguos ("To the readers of the ...").
SALUDO = re.compile(r'(?im)^[ \t]*To the readers of the [^\n]*$')

# Avisos sueltos que no son artículos: direcciones, pedidos, suscripciones,
# envíos gratis a los pobres, sellos, cambios de dirección...
SUELTOS = re.compile(
    r'(?is)^[\s—–-]*(?:'
    r'all orders should be addressed|all communications should be addressed|'
    r'all subscriptions should be|subscriptions should be sent|'
    r'terms:?\s*--|terms,? \d+ cents|foreign terms|foreign postage|'
    r'n\.?b\.?\s*--\s*this paper|'
    r'please send us no foreign|foreign subscribers will please|'
    r'subscribers who remove|'
    r'money orders?,? (?:etc\.?,? )?(?:should be|made payable|payable)|'
    r'postage stamps|postal cards?|'
    r'this paper will be sent free|will be sent free to any of the lord.s poor|'
    r'if you have not received your full order|'
    r'volume \d+, india paper|'
    r'sample copies|'
    r'entered as second-class'
    r')[^\n]*(?:\n(?!\n)[^\n]*){0,6}?\s*(?=\n\s*\n|\Z)',
    re.M)

MARCAS_AVISO = (
    'prices are net', 'postpaid', 'per copy', 'copies', 'address all',
    'scripture studies and scenarios', 'bethel hymns', 'german memorial number',
    'angelico', 'studies in the scriptures', 'entered as second-class',
    'foreign agencies', "terms to the lord's poor", 'annual subscription',
    'missionary', 'colporteur', 'volunteer', 'vols.', 'sample copies',
    'sent free', 'free on application', 'published monthly', 'angelophone',
    'memorial number', 'memorial issue', 'these studies are recommended',
    'series i', 'morocco', 'bethel family', 'pittsburgh, pa.', "herald of christ's presence",
    'stamps', 'subscribers', 'millennial day dawn', 'brother boyer', 'outlines of six sermons',
    'in tract form', 'foreign terms', 'foreign postage', 'money order', 'postal card',
    'supplement to', 'post office changes', 'pittsburgh church meetings',
    'church meetings', 'services held', 'meeting hall',
)


def quitar_cabecera(texto):
    """Quita la portada publicitaria con que empiezan algunos números."""
    ps = [p for p in texto.split('\n\n') if p.strip()]
    i = 0
    while i < len(ps) and i < 30:
        p = ps[i].strip()
        basura = bool(re.fullmatch(r'[\s—–_=*·.]+', p))
        aviso = any(m in p.lower() for m in MARCAS_AVISO)
        if basura or aviso:
            i += 1
            continue
        break
    if i >= 2:
        return '\n\n'.join(ps[i:])
    return texto


RESTOS = [re.compile(p, re.I) for p in (
    r"^ZION['\u2019]?S WATCH TOWER(?: AND)?\.?$",
    r"^HERALD OF CHRIST['\u2019]?S PRESENCE\.?$",
    r"^Zion['\u2019]s Watch Tower and Herald of Christ['\u2019]s Presence\.?$",
    r'^Published (?:Twice|Once) a Month\.?$',
    r'^TOWER PUBLISHING (?:COMPANY|CO\.).*$',
    r'^C\. ?T\. ?RUSSELL,? (?:EDITOR|Editor).*$',
    r'^SUBSCRIPTION PRICE.*$',
    r"^FREE TO THE LORD['\u2019]S POOR.*$",
    r"^(?:Combination |Divinity Circuit |Cambridge India Paper |Bagster |Holman )?Teachers['\u2019]? Bibles[.,]?$",
    r'^Postage,? \d+c.*$',
    r"^The Cheapest Teachers['\u2019]? Bible.*$",
    r'^COMBINES ALL THE .HELPS. FEATURES.*$',
    r'^All Orders should be addressed.*$',
    r'^N\.?B\.?\s*[—–-].*(?:poor|free).*$',
)]


FUERTES = ('divinity circuit', 'thumb index', 'red under gold', 'french seal',
           'french morocco', 'leather lined', 'teachers\u2019 bibles', "teachers' bibles",
           'minion type edition', 'pictorial edition', 'india paper edition',
           'postage, 25c', 'postage, 20c', 'postage, 26c')


def _es_publicidad(p):
    bajo = p.lower()
    precios = len(re.findall(r'\$\s?\d|\d+[.,]\d{2}|\d+\s?c\.', p))
    if any(x in bajo for x in FUERTES) and (precios >= 1 or bajo.endswith('edition.')):
        return True
    if 'price' in bajo and any(x in bajo for x in ('cents', 'dollars', 'per dozen', 'postage')):
        return True
    marcas = sum(x in bajo for x in ('postage', 'per copy', 'postpaid', 'cloth', 'leather',
                                     'price', 'wholesale', 'retail', 'edition', 'editions'))
    return marcas >= 3 and precios >= 4


def quitar_restos(texto):
    """Quita restos de cabecera y listas de precios que quedan sueltos."""
    ps = [p.strip() for p in texto.split('\n\n') if p.strip()]
    out = [p for p in ps if not any(r.match(p) for r in RESTOS) and not _es_publicidad(p)]
    return '\n\n'.join(out)


def quitar_avisos(texto):
    texto = texto.replace('\f', '\n')
    t = PORTADA.sub(' ', texto)
    t = SALUDO.sub(' ', t)
    t = SUELTOS.sub(' ', t)
    for patron in AVISOS:
        t = re.sub(patron, ' ', t)
    return t


def segmentar(texto):
    """Devuelve el texto de los artículos o None si no hay índice utilizable."""
    lista, fin = entradas(texto)
    if not lista:
        return None
    principales = [(t, p) for t, p, principal in lista if principal]
    if not principales:
        return None
    conservados, cursor = [], fin
    for titulo, _ in principales:
        if any(x in titulo.lower() for x in NO_ARTICULO):
            continue
        pos = buscar_titulo(texto, titulo, cursor)
        if pos is None:
            continue
        conservados.append((pos, titulo))
        cursor = pos + 10
    if not conservados:
        return None
    trozos = []
    for i, (pos, _) in enumerate(conservados):
        fin_trozo = conservados[i + 1][0] if i + 1 < len(conservados) else len(texto)
        ini = pos
        while ini > 0 and texto[ini - 1] in '"“‘(':
            ini -= 1
        frag = texto[ini:fin_trozo]
        m = CORTE_RE.search(frag[200:])
        if m:
            frag = frag[:200 + m.start()]
        if len(frag) > 300:
            trozos.append(frag)
    return '\n\n'.join(trozos) if trozos else None


def preparar(texto):
    """Segmenta y quita avisos; devuelve texto listo para limpiar."""
    cuerpo = segmentar(texto)
    if cuerpo is None:
        cuerpo = texto
    limpio = quitar_avisos(cuerpo)
    # Nunca perder el número por un recorte demasiado agresivo.
    if len(limpio) < max(3000, int(len(texto) * 0.15)):
        limpio = quitar_avisos(texto)
    return limpio
