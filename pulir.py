"""Limpieza editorial del texto extraído de los PDFs de The Watch Tower.

No cambia ni una palabra del original: solo arregla la forma.
- Une palabras y compuestos partidos por el salto de línea.
- Corrige comillas, rayas, puntos suspensivos y rangos numéricos.
- Elimina separadores sueltos, marcas de página y espacios dobles.
- Pone en minúsculas correctas los títulos que vienen todo en mayúsculas.
- Vuelve a unir párrafos que el PDF cortó al cambiar de página.
"""

import re

MESES = ('JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY',
         'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER')

MENORES = {'a', 'an', 'the', 'and', 'but', 'or', 'nor', 'for', 'of', 'to',
           'in', 'on', 'at', 'by', 'with', 'from', 'as', 'into', 'upon',
           'than', 'that', 'per', 'via'}

SUFIJOS = ('tion', 'sion', 'ment', 'ness', 'ing', 'ings', 'ed', 'ly', 'es',
           'al', 'ous', 'ive', 'ity', 'ties', 'ance', 'ence', 'able', 'ible')

SEPARADOR = re.compile(r'^(?:—{3,}|–{3,}|-{3,}|_{3,}|={3,}|\*{3,}|\.{3,}|·{3,})[\s]*|'
                       r'[\s]*(?:—{3,}|–{3,}|-{3,}|_{3,}|={3,}|\*{3,}|\.{3,}|·{3,})$')
BASURA = re.compile(r'^[\s—–_=*·.]+$')
PAGINA = re.compile(r'\b(?:R\d+\s*:\s*)?page\s+\d+\b', re.I)
GUION = re.compile(r'([A-Za-z]+(?:-[A-Za-z]+)*)-\s+([A-Za-z]+)')


def construir_vocabulario(textos):
    """Cuenta palabras y compuestos del propio corpus para decidir guiones."""
    vocab = set()
    for t in textos:
        for w in re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)*(?:-[A-Za-z]+)*", t):
            vocab.add(w.lower())
    return vocab


def _es_titulo(p):
    """¿Es un encabezado que el PDF trae todo en mayúsculas?"""
    if len(p) > 130 or not p.isupper():
        return False
    if re.search(r'\d', p):
        return False
    palabras = re.findall(r"[A-Za-z][A-Za-z'’]*", p)
    if len(palabras) < 2:
        return False
    if any(len(w) <= 1 for w in palabras if w.upper() not in ('A', 'I')):
        return False
    return True


def _titulo(p):
    palabras = p.split(' ')
    salida = []
    for i, w in enumerate(palabras):
        nucleo = w.strip('.,;:!?')
        if nucleo.upper() in MESES and i > 0:
            salida.append(w.capitalize())
            continue
        if re.fullmatch(r"[IVXLC]+[.,;:!?]*", nucleo):
            salida.append(w.upper())
            continue
        minus = w.lower()
        if i > 0 and nucleo.lower() in MENORES:
            salida.append(minus)
        else:
            cabeza = w[:len(w) - len(w.lstrip('“”\"‘(('))]
            salida.append(cabeza + w[len(cabeza):len(cabeza)+1].upper() + w[len(cabeza)+1:].lower())
    return ' '.join(salida)


def _comillas(p):
    """Comillas tipográficas y apóstrofos correctos."""
    out = []
    n = len(p)
    for i, ch in enumerate(p):
        ant = p[i - 1] if i else ''
        sig = p[i + 1] if i + 1 < n else ''
        if ch == '"':
            if (not ant or ant.isspace() or ant in '([—–-') and sig and not sig.isspace():
                out.append('“')
            else:
                out.append('”')
        elif ch == "'":
            if ant.isalnum() and sig.isalnum():
                out.append('’')
            elif not ant or ant.isspace() or ant in '([—–-“”':
                out.append('‘')
            elif not sig or sig.isspace() or sig in '.,;:!?)]—–-”':
                out.append('’')
            else:
                out.append('’')
        else:
            out.append(ch)
    return ''.join(out)


def _guiones(p, vocab):
    def arreglo(m):
        completo = m.group(0)
        unido = (m.group(1) + m.group(2)).lower()
        con = (m.group(1) + '-' + m.group(2)).lower()
        if con in vocab and unido not in vocab:
            return m.group(1) + '-' + m.group(2)
        if unido in vocab:
            return m.group(1) + m.group(2)
        if m.group(2).lower().startswith(SUFIJOS):
            return m.group(1) + m.group(2)
        return m.group(1) + '-' + m.group(2)
    return GUION.sub(arreglo, p)


def pulir(texto, vocab=None):
    vocab = vocab or set()
    parrafos = []

    for bruto in texto.split('\n\n'):
        p = re.sub(r'\s+', ' ', bruto).strip()
        if not p:
            continue
        # separadores y marcas de página
        p = SEPARADOR.sub('', p).strip()
        p = PAGINA.sub(' ', p).strip()
        p = re.sub(r'\s{2,}', ' ', p)
        if not p or BASURA.match(p):
            continue
        # unir fragmentos de un mismo título centrado
        if parrafos and len(p) < 100 and len(parrafos[-1]) < 100:
            prev = parrafos[-1]
            if (prev.isupper() and p.isupper() and not re.search(r'[.!?:;]$', prev)
                    and not p.startswith(('—', '–'))):
                parrafos[-1] = prev + ' ' + p
                continue
        # unir párrafos cortados por cambio de página
        if parrafos:
            prev = parrafos[-1]
            final = re.sub(r'[”’"\']+$', '', prev).rstrip()
            continua = (not re.search(r'[.!?;:]$', final) or final.endswith(','))
            arranque = p[:1].islower() or re.match(
                r'(and|but|or|for|that|which|who|whom|whose|where|when|while|'
                r'as|in|of|to|with|from|by|on|at|it|this|these|those)\b', p)
            if continua and arranque:
                parrafos[-1] = prev + ' ' + p
                continue
        parrafos.append(p)

    finales = []
    for p in parrafos:
        p = _guiones(p, vocab)
        # comillas sueltas al final de un título corto
        if len(p) < 140 and p.endswith('"') and p.count('"') % 2:
            p = p[:-1].rstrip()
        if _es_titulo(p) and not p.startswith(('—', '–')):
            p = _titulo(p)
        p = p.replace('...', '…').replace('--', '—')
        p = re.sub(r'(?<=\d)-(?=\d)', '–', p)
        p = _comillas(p)
        p = re.sub(r'\s+([,;:.!?])', r'\1', p)
        p = re.sub(r'([“‘])\s+', r'\1', p)
        p = re.sub(r'\s{2,}', ' ', p).strip()
        if not p or BASURA.match(p):
            continue
        finales.append(p)

    return '\n\n'.join(finales)
