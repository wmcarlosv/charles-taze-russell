import json, re, sqlite3, subprocess, sys, unicodedata

DB = '/home/carlos/Programas/biblioteca-ia/biblioteca.db'
LIB = {'genesis':'Génesis','exodo':'Éxodo','levitico':'Levítico','numeros':'Números','deuteronomio':'Deuteronomio','josue':'Josué',
 'jueces':'Jueces','rut':'Rut','1samuel':'1 Samuel','2samuel':'2 Samuel','1reyes':'1 Reyes','2reyes':'2 Reyes','1cronicas':'1 Crónicas',
 '2cronicas':'2 Crónicas','esdras':'Esdras','nehemias':'Nehemías','ester':'Ester','job':'Job','salmos':'Salmos','salmo':'Salmos','sal':'Salmos',
 'proverbios':'Proverbios','pro':'Proverbios','prov':'Proverbios','eclesiastes':'Eclesiastés','ecl':'Eclesiastés','cantares':'Cantares','isaias':'Isaías',
 'isa':'Isaías','jeremias':'Jeremías','jer':'Jeremías','lamentaciones':'Lamentaciones','lam':'Lamentaciones','ezequiel':'Ezequiel','ezeq':'Ezequiel',
 'daniel':'Daniel','dan':'Daniel','oseas':'Oseas','joel':'Joel','amos':'Amós','abdias':'Abdías','jonas':'Jonás','miqueas':'Miqueas','nahum':'Nahúm',
 'habacuc':'Habacuc','sofonias':'Sofonías','ageo':'Hageo','zacarias':'Zacarías','zac':'Zacarías','malaquias':'Malaquías','mal':'Malaquías',
 'mateo':'Mateo','mat':'Mateo','mt':'Mateo','marcos':'Marcos','mar':'Marcos','lucas':'Lucas','luc':'Lucas','juan':'Juan','jn':'Juan',
 'hechos':'Hechos','hech':'Hechos','romanos':'Romanos','rom':'Romanos','ro':'Romanos','1corintios':'1 Corintios','2corintios':'2 Corintios',
 '1cor':'1 Corintios','2cor':'2 Corintios','galatas':'Gálatas','gal':'Gálatas','ga':'Gálatas','efesios':'Efesios','efe':'Efesios','ef':'Efesios',
 'filipenses':'Filipenses','fil':'Filipenses','colosenses':'Colosenses','col':'Colosenses','1tesalonicenses':'1 Tesalonicenses','2tesalonicenses':'2 Tesalonicenses',
 '1tes':'1 Tesalonicenses','2tes':'2 Tesalonicenses','1timoteo':'1 Timoteo','2timoteo':'2 Timoteo','1tim':'1 Timoteo','2tim':'2 Timoteo','tito':'Tito',
 'filemon':'Filemón','flm':'Filemón','hebreos':'Hebreos','heb':'Hebreos','he':'Hebreos','santiago':'Santiago','sant':'Santiago','jas':'Santiago',
 '1pedro':'1 Pedro','2pedro':'2 Pedro','1ped':'1 Pedro','2ped':'2 Pedro','1juan':'1 Juan','2juan':'2 Juan','3juan':'3 Juan','judas':'Judas','jud':'Judas',
 'apocalipsis':'Apocalipsis','apoc':'Apocalipsis','apo':'Apocalipsis','rev':'Apocalipsis'}

LIB.update({
 'gen':'Génesis','is':'Isaías','deut':'Deuteronomio','deu':'Deuteronomio','ex':'Éxodo','exo':'Éxodo','lev':'Levítico',
 'num':'Números','nu':'Números','jos':'Josué','jue':'Jueces','jc':'Jueces',
 '1rey':'1 Reyes','2rey':'2 Reyes','1sam':'1 Samuel','2sam':'2 Samuel','1re':'1 Reyes','2re':'2 Reyes','1co':'1 Corintios','2co':'2 Corintios','1cr':'1 Crónicas','2cr':'2 Crónicas','1pet':'1 Pedro','2pet':'2 Pedro','ose':'Oseas','1jn':'1 Juan','2jn':'2 Juan','3jn':'3 Juan','1cron':'1 Crónicas','2cron':'2 Crónicas','1cro':'1 Crónicas','2cro':'2 Crónicas',
 'esd':'Esdras','neh':'Nehemías','est':'Ester','cant':'Cantares','os':'Oseas','hos':'Oseas',
 'abd':'Abdías','jon':'Jonás','miq':'Miqueas','hab':'Habacuc','sof':'Sofonías','hag':'Hageo',
 'matt':'Mateo','mr':'Marcos','mc':'Marcos','fili':'Filipenses','flp':'Filipenses',
 'matthew':'Mateo','mark':'Marcos','luke':'Lucas','john':'Juan','acts':'Hechos',
 'romans':'Romanos','revelation':'Apocalipsis','psalm':'Salmos',
 '1ts':'1 Tesalonicenses','2ts':'2 Tesalonicenses','1ti':'1 Timoteo','2ti':'2 Timoteo','tit':'Tito',
 'stg':'Santiago','1p':'1 Pedro','2p':'2 Pedro','1j':'1 Juan','2j':'2 Juan','3j':'3 Juan','ap':'Apocalipsis',
})



def sinac(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()


CLAVES = sorted(LIB, key=len, reverse=True)
VOC = {'a': '[aá]', 'e': '[eé]', 'i': '[ií]', 'o': '[oó]', 'u': '[uú]', 'n': '[nñ]'}
def _pat_clave(k):
    if k[:1].isdigit():
        return re.escape(k[0]) + r'\s*' + ''.join(VOC.get(c, re.escape(c)) for c in k[1:])
    return ''.join(VOC.get(c, re.escape(c)) for c in k)

VS = r'(?:\s*[-–]\s*\d{1,3})?(?:\s*(?:,\s*\d{1,3}(?:\s*[-–]\s*\d{1,3})?|y\s+\d{1,3}(?!\d)(?!\s*[:.])(?:\s*[-–]\s*\d{1,3})?))*'
PAT = re.compile(r'(?<![\wÁÉÍÓÚÑáéíóúñ])(' + '|'.join(_pat_clave(k) for k in CLAVES) +
                 r')\.?\s*(\d{1,3})\s*[:.]\s*(\d{1,3})(' + VS + r')', re.I)
RESTO = re.compile(r'(?:\s*[;,]\s*|\s+y\s+)(\d{1,3})\s*[:.]\s*(\d{1,3})(' + VS + r')')
PAT_PAREN = re.compile(r'(?<![\wÁÉÍÓÚÑáéíóúñ])(' + '|'.join(_pat_clave(k) for k in CLAVES) +
                 r')\.?\s*\(\s*(\d{1,3})\s*[:.]\s*(\d{1,3})(' + VS + r')\s*\)', re.I)


def _versos(txt):
    return [int(x) for x in re.findall(r'\d{1,3}', txt)]


UN_CAPITULO = {'Abdías', 'Filemón', '2 Juan', '3 Juan', 'Judas'}
PAT_CAP = re.compile(r'(?<![\wÁÉÍÓÚÑáéíóúñ])([1-3]?\s?[A-Za-zÁÉÍÓÚÑáéíóúñ]{2,15})\.?'
                     r'\s+(\d{1,4})(?!\d)(?!\s*[:.]\s*\d)')
_LIMITES = None


def _limites():
    global _LIMITES
    if _LIMITES is not None:
        return _LIMITES
    con = sqlite3.connect(DB)
    maxcap = {r[0]: r[1] for r in con.execute('select libro,max(capitulo) from biblia group by libro')}
    maxvers = {}
    for libro, cap, mx in con.execute('select libro,capitulo,max(versiculo) from biblia group by libro,capitulo'):
        maxvers.setdefault(libro, {})[cap] = mx
    con.close()
    _LIMITES = (maxcap, maxvers)
    return _LIMITES


def cita_valida(libro, cap, v1, v2):
    maxcap, maxvers = _limites()
    mx = maxvers.get(libro, {}).get(cap)
    return mx is not None and 1 <= v1 <= v2 <= mx


def ajustar_cap(libro, n):
    maxcap, maxvers = _limites()
    if libro in UN_CAPITULO:
        return (1, n) if 1 <= n <= maxvers.get(libro, {}).get(1, 0) else None
    if 1 <= n <= maxcap.get(libro, 0):
        return (n, 1)
    candidatos = []
    for div in (10, 100, 1000):
        c, v = divmod(n, div)
        if 1 <= c <= maxcap.get(libro, 0) and 1 <= v <= maxvers.get(libro, {}).get(c, 0):
            candidatos.append((c, v))
    if not candidatos:
        return None
    candidatos.sort(key=lambda x: (-x[0], -x[1]))
    return candidatos[0]


def citas_validas(texto):
    out, previo = [], -1
    for (a, b, ref, libro, cap, v1, v2) in extrae(texto):
        if a < previo or '\n\n' in texto[a:b]:
            continue
        if not cita_valida(libro, cap, v1, v2):
            continue
        out.append((a, b, ref, libro, cap, v1, v2))
        previo = b
    for m in PAT_CAP.finditer(texto):
        libro = LIB.get(sinac(m.group(1)).replace(' ', ''))
        if not libro:
            continue
        a, b = m.start(), m.end()
        if '\n\n' in texto[a:b] or any(not (b <= c[0] or a >= c[1]) for c in out):
            continue
        ajuste = ajustar_cap(libro, int(m.group(2)))
        if not ajuste:
            continue
        cap, v = ajuste
        if not cita_valida(libro, cap, v, v):
            continue
        out.append((a, b, m.group(0), libro, cap, v, v))
    out.sort(key=lambda c: c[0])
    return out


def extrae(t):
    out = []
    for m in PAT.finditer(t):
        libro = LIB.get(sinac(m.group(1)).replace(' ', ''))
        if not libro:
            continue
        cap, v1 = int(m.group(2)), int(m.group(3))
        nums = [v1] + _versos(m.group(4) or '')
        v2 = max(nums)
        if 1 <= cap <= 150 and 1 <= v1 <= 176:
            out.append((m.start(), m.end(), m.group(0), libro, cap, v1, v2))
        # referencias encadenadas del mismo libro: "Jn. 5:21; 6:44; 7:37"
        pos = m.end()
        for _ in range(8):
            r = RESTO.match(t, pos)
            if not r:
                break
            sep = t[pos:r.start(1)]
            if ';' not in sep and not re.search(r'\by\b', sep):
                break
            cap2, w1 = int(r.group(1)), int(r.group(2))
            nums2 = [w1] + _versos(r.group(3) or '')
            if not (1 <= cap2 <= 150 and 1 <= w1 <= 176):
                break
            out.append((r.start(1), r.end(), t[r.start(1):r.end()].strip(), libro, cap2, w1, max(nums2)))
            pos = r.end()
    # Referencias con el capítulo entre paréntesis: «Daniel (12:4, 9, 10)»
    for m in PAT_PAREN.finditer(t):
        libro = LIB.get(sinac(m.group(1)).replace(' ', ''))
        if not libro:
            continue
        cap, v1 = int(m.group(2)), int(m.group(3))
        nums = [v1] + _versos(m.group(4) or '')
        v2 = max(nums)
        if 1 <= cap <= 150 and 1 <= v1 <= 176:
            out.append((m.start(), m.end(), m.group(0), libro, cap, v1, v2))
    out.sort(key=lambda x: x[0])
    return out


def main():
    pdf, vol, titulo = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    pages = subprocess.run(['pdftotext', pdf, '-'], capture_output=True).stdout.decode('utf-8', 'replace').split('\f')
    est = {}
    actual = None
    for p in pages:
        m = re.search(r'Estudio\s*(\d+)\s*-\s*(\d+)', p, re.I) or re.search(r'Estudio\s*(\d+)\b', p[:400], re.I)
        if m:
            actual = int(m.group(1))
        if not actual:
            continue
        n = actual
        ls = [l.strip() for l in p.split('\n')]
        ls = [l for l in ls if l and not re.search(r'Estudio\s*\d+', l, re.I)]
        if ls and 'Plan Divino' in ls[0]:
            ls = ls[1:]
        t = re.sub(r'\s*\(\d{1,3}\)\s*', ' ', ' '.join(ls))
        t = re.sub(r'\s+', ' ', t).strip()
        if len(t.split()) > 20:
            est.setdefault(n, []).append(t)
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    titulos = [r['titulo'] for r in con.execute("select titulo from paginas where volumen=? and titulo not like 'Prólogo%' order by pagina", (vol,))]
    bases = []
    for t in titulos:
        b = re.sub(r'^Estudio \d+ — ', '', t)
        b = re.sub(r'\s+—\s+Parte \d+/\d+$', '', b)
        if b not in bases:
            bases.append(b)
    for pid in [r[0] for r in con.execute("select id from paginas where volumen=? and titulo not like 'Prólogo%'", (vol,))]:
        con.execute('delete from citas where pagina_id=?', (pid,))
        con.execute('delete from busqueda where rowid=?', (pid,))
        con.execute('delete from paginas where id=?', (pid,))
    con.commit()
    for n in sorted(est):
        texto = ' '.join(est[n])
        fr = re.split(r'(?<=[.!?»"])\s+', texto)
        ps, buf = [], []
        for s in fr:
            buf.append(s)
            if len(buf) >= 5:
                ps.append(' '.join(buf)); buf = []
        if buf: ps.append(' '.join(buf))
        texto = '\n\n'.join(ps)
        tit = bases[n - 1] if n - 1 < len(bases) else 'Estudio %d' % n
        tit = 'Estudio %d — %s' % (n, tit)
        cur = con.execute('insert into paginas (obra,volumen,titulo_obra,pagina,pagina_pdf,titulo,texto,idioma,indice,original,resumen) values (?,?,?,?,?,?,?,?,?,?,?)',
                          (titulo, vol, titulo, n, n, tit, texto, 'es', 0, '', '[]'))
        pid = cur.lastrowid
        con.execute('insert into busqueda(rowid,texto,titulo) values (?,?,?)', (pid, texto, tit))
        for (a, b, ref, libro, cap, v1, v2) in extrae(texto):
            con.execute('insert into citas (pagina_id,inicio,fin,ref_texto,libro,capitulo,v_ini,v_fin) values (?,?,?,?,?,?,?,?)', (pid, a, b, ref, libro, cap, v1, v2))
        print('ok', n, tit[:50], len(texto.split()), flush=True)
    con.commit(); con.close()
    print('FIN', len(est), flush=True)


if __name__ == '__main__':
    main()
