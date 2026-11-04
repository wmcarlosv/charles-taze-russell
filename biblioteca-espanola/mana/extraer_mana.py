#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrae el contenido de «Maná Diario Celestial para la Familia de la Fe»
(PDF en español) y genera los datos estructurados que se guardan en esta
carpeta: maná de los 366 días, devociones matutinas y suplemento.

Uso:
    python3 extraer_mana.py [ruta/al/ManaDiario.pdf]

Requiere el programa pdftotext (paquete poppler-utils).
"""
import html
import json
import os
import re
import subprocess
import sys
import unicodedata
from datetime import date

# El analizador de referencias de la biblioteca (para enlazar las citas del maná)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from asistente import parsea_ref
except Exception:
    parsea_ref = None

BASE = os.path.dirname(os.path.abspath(__file__))
PDF = (sys.argv[1] if len(sys.argv) > 1 else
       os.path.join(BASE, 'ManaDiario.pdf') if os.path.isfile(os.path.join(BASE, 'ManaDiario.pdf'))
       else '/home/carlos/Desktop/ManaDiario.pdf')

MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
         'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
MES_NUM = {m: i + 1 for i, m in enumerate(MESES)}
MES_NUM['setiembre'] = 9

SUP_TITULOS = [
    'Oración', 'Paciencia', 'Liberalidad', 'Pureza', 'Alabanza', 'Socorro',
    'Testimonio del Evangelio', 'Consuelo en el Desamparo',
    'Vencer los Malos Hábitos',
    'Vencer el Sentimiento de Abandono y de Desaliento',
]

DIAS = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']

# Citas del tipo Z. '03-3, Z.’00- 11, Z. ’04 37, 38, Z. 99-167…
SRC_RE = re.compile(
    r"Z\.?\s*[‘’'´`]?\s*\d{2,4}\s*(?:[-–]|\s)\s*\d{1,3}"
    r"(?:\s*,\s*\d{1,3})?\s*\.?", re.I)

# Fuentes de las devociones: R2205:6; 2234:5; 2240:1 / A191; R612:6
DEV_SRC_RE = re.compile(r'((?:A|R)\d{2,}[A-Za-z0-9:,\-; ]*)\s*$')

PRIVADOS = re.compile(r'[\ue000-\uf8ff]')


def leer_pdf(pdf=PDF, paginas=None):
    cmd = ['pdftotext', '-layout']
    if paginas:
        cmd += ['-f', str(paginas[0]), '-l', str(paginas[1])]
    cmd += [pdf, '-']
    try:
        salida = subprocess.check_output(cmd)
    except FileNotFoundError:
        raise SystemExit('Falta pdftotext (instala poppler-utils).')
    return salida.decode('utf-8', 'replace').replace('\f', '')


def espacios(s):
    return re.sub(r'\s+', ' ', s or '').strip()


def a_parrafos(lineas):
    """Une las líneas del PDF en párrafos, conservando los saltos en blanco."""
    out, buf = [], []
    for linea in lineas:
        s = linea.strip()
        if not s:
            if buf:
                out.append(' '.join(buf))
                buf = []
        else:
            # palabra partida al final de la línea: «re-» + «formadas»
            if buf and buf[-1].endswith('-') and s[:1].islower():
                buf[-1] += s
            else:
                buf.append(s)
    if buf:
        out.append(' '.join(buf))
    return [espacios(p) for p in out if p.strip()]


def separar_cita(p0):
    """Devuelve (texto de la cita, texto de la referencia) del primer párrafo."""
    a = p0.find('“')
    if a < 0:
        a = p0.find('"')
    if a < 0:
        return '', p0.strip()

    marcas = [i for i, c in enumerate(p0) if '\ue000' <= c <= '\uf8ff']
    if marcas:
        mk = marcas[0]
        q = p0.rfind('”', a, mk)
        if q < 0:
            q = p0.rfind('"', a, mk)
        cita = p0[a + 1:q if q >= 0 else mk]
        resto = p0[mk:]
    else:
        q = p0.rfind('”')
        if q < 0:
            q = p0.rfind('"')
        if q < 0:
            cita, resto = p0[a + 1:], ''
        else:
            cita, resto = p0[a + 1:q], p0[q + 1:]

    cita = espacios(PRIVADOS.sub('', cita)).strip(' “”"')
    resto = espacios(PRIVADOS.sub('', resto))
    return cita, resto


def normalizar_referencia(r):
    """Versión útil para enlazar después con la Biblia de la biblioteca."""
    r = re.sub(r'^(I{1,3})\s+', lambda m: str(len(m.group(1))) + ' ', r)
    r = re.sub(r'^Salmo\s+', 'Salmos ', r)
    r = re.sub(r'^(Judas|Filemón|Filemon|Obadías|Obadias)\s+(\d{1,3})(?!\s*:)',
               r'\1 1:\2', r)
    return r


def limpiar_ref(r):
    r = espacios(PRIVADOS.sub('', r or ''))
    r = re.sub(r'\s*:\s*', ':', r)
    r = re.sub(r'\s*([,;])\s*', r'\1 ', r)
    r = re.sub(r'^[”"\'…\s]+', '', r)
    r = re.sub(r'[.;\s]+$', '', r)
    return r.strip()


def normalizar_fuente(s):
    s = s.replace('‘', "'").replace('’', "'").replace('´', "'").replace('`', "'")
    s = s.replace('–', '-')
    s = re.sub(r'\s*-\s*', '-', s)
    s = espacios(s)
    s = re.sub(r'^Z\.?\s*', 'Z. ', s)
    s = re.sub(r"^Z\.\s*'\s*", "Z. '", s)
    # «Z. '04 37, 38» → «Z. '04-37, 38»
    s = re.sub(r"^(Z\.\s*'\s*\d{2,4})\s+(\d{1,3})", r'\1-\2', s)
    s = s.rstrip(' .')
    return s


def limpiar_cuerpo(c):
    c = c.replace('\uf0be', '—').replace('\u00ad', '')
    c = PRIVADOS.sub('—', c)
    c = re.sub(r'\(\s*\)', '', c)
    c = re.sub(r'[ \t]+', ' ', c)
    c = re.sub(r'\s+([.,;:])', r'\1', c)
    c = re.sub(r'\n{3,}', '\n\n', c)
    parrafos = [p.strip() for p in c.split('\n\n') if p.strip()]
    return '\n\n'.join(parrafos), parrafos


ROMANOS = {'I': '1', 'II': '2', 'III': '3'}

REF_TXT = re.compile(
    r'(?<![\wÁÉÍÓÚÑáéíóúñ])'
    r'((?:I{1,3}|[1-3])?\s*[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\.?)\s*'
    r'(\d{1,3})\s*:\s*(\d{1,3})'
    r'(?:\s*[-–]\s*(\d{1,3}))?'
    r'(?:\s*,\s*(\d{1,3}))?')


def romanizar(ref):
    m = re.match(r'^(I{1,3})\s+', ref)
    if m:
        ref = ROMANOS[m.group(1)] + ' ' + ref[m.end():]
    return ref


SINGLE = {'Judas', 'Filemón', 'Filemon', '2 Juan', '3 Juan', 'Obadías', 'Obadias'}


def _enlace(ref, parsed):
    libro = parsed['libro']
    cap = parsed['capitulo']
    v1, v2 = parsed['v_ini'], parsed['v_fin']
    # «Judas 21» es capítulo 1, versículo 21
    if libro in SINGLE and v1 is None and cap > 1:
        v1 = v2 = cap
        cap = 1
    attrs = ['class="ref"', 'href="#"',
             'data-libro="%s"' % html.escape(libro, quote=True),
             'data-cap="%d"' % cap]
    if v1 is not None:
        attrs.append('data-v1="%d"' % v1)
        if v2 and v2 != v1:
            attrs.append('data-v2="%d"' % v2)
    return '<a %s>%s</a>' % (' '.join(attrs), html.escape(ref))


def enlazar(texto):
    """Convierte las referencias bíblicas del texto en enlaces de la biblioteca."""
    if not texto or not parsea_ref:
        return html.escape(texto or '')
    salida, ultimo = [], 0
    for m in REF_TXT.finditer(texto):
        ref = m.group(0)
        ini = m.start()
        while ref[:1].isspace():
            ref = ref[1:]
            ini += 1
        parsed = parsea_ref(romanizar(ref))
        if not parsed:
            continue
        salida.append(html.escape(texto[ultimo:ini]))
        salida.append(_enlace(ref, parsed))
        ultimo = m.end()
    salida.append(html.escape(texto[ultimo:]))
    return ''.join(salida)


def enlace_referencia(ref):
    """Enlaza la referencia principal completa (incluye casos como «Judas 21»)."""
    if not ref or not parsea_ref:
        return html.escape(ref or '')
    normal = normalizar_referencia(romanizar(ref))
    # Si el detector general no encontró nada, intentar con la referencia completa.
    if '<a ' not in enlazar(ref):
        parsed = parsea_ref(normal)
        if parsed:
            return _enlace(ref, parsed)
    return enlazar(ref)


def extraer_parte(lineas):
    """Extrae cita, referencia, cuerpo y fuentes de un bloque de líneas."""
    ps = a_parrafos(lineas)
    if not ps:
        return None
    cita, referencia = separar_cita(ps[0])
    cuerpo_lineas = ps[1:]

    # Referencia que quedó en el párrafo siguiente (raro, pero posible)
    if (not referencia or not re.search(r'\d', referencia)) and cuerpo_lineas:
        posible = limpiar_ref(cuerpo_lineas[0])
        if len(posible) < 90 and re.search(r'\d', posible):
            referencia = posible
            cuerpo_lineas = cuerpo_lineas[1:]

    cuerpo = '\n\n'.join(cuerpo_lineas)
    fuentes = [normalizar_fuente(m.group(0)) for m in SRC_RE.finditer(cuerpo)]
    if fuentes:
        cuerpo = SRC_RE.sub('', cuerpo)
    cuerpo, parrafos = limpiar_cuerpo(cuerpo)

    # quitar fuentes duplicadas conservando el orden
    vistas = set()
    fuentes = [f for f in fuentes if not (f in vistas or vistas.add(f))]

    ref = limpiar_ref(referencia)
    return {
        'cita': cita,
        'cita_html': enlazar(cita),
        'referencia': ref,
        'referencia_normal': normalizar_referencia(ref),
        'referencia_html': enlace_referencia(ref),
        'texto': cuerpo,
        'parrafos': parrafos,
        'parrafos_html': [enlazar(p) for p in parrafos],
        'fuente': fuentes[-1] if fuentes else None,
        'fuentes': fuentes,
    }


def extraer_diario(raw):
    lineas = raw.split('\n')
    fecha_re = re.compile(
        r'^\s*(\d{1,2})\s+de\s+(' + '|'.join(MESES) + r'|setiembre)\s*$', re.I)
    fechas = [(i, int(m.group(1)), m.group(2).lower())
              for i, l in enumerate(lineas) for m in [fecha_re.match(l)] if m]

    if not fechas:
        raise SystemExit('No se encontraron las fechas del maná diario.')

    # comienzo del suplemento (primera voz después del 31 de diciembre)
    sup_start = None
    for i in range(fechas[-1][0] + 1, len(lineas)):
        if lineas[i].strip() in SUP_TITULOS:
            sup_start = i
            break
    if sup_start is None:
        raise SystemExit('No se encontró el comienzo del suplemento.')

    salida = []
    for k, (i, dia, mes_nombre) in enumerate(fechas):
        fin = fechas[k + 1][0] if k + 1 < len(fechas) else sup_start
        parte = extraer_parte(lineas[i + 1:fin])
        if not parte:
            raise SystemExit('Entrada vacía: %d de %s' % (dia, mes_nombre))
        mes = MES_NUM[mes_nombre]
        parte.update({
            'orden': k + 1,
            'dia': dia,
            'mes': mes,
            'mes_nombre': MESES[mes - 1],
            'clave': '%02d-%02d' % (mes, dia),
        })
        salida.append(parte)
    return salida, lineas, fechas[-1][0], sup_start


def extraer_suplemento(lineas, sup_start):
    indice = next((i for i, l in enumerate(lineas) if 'Índice Temático' in l), None)
    if indice is None:
        raise SystemExit('No se encontró el índice temático.')
    posiciones = []
    for titulo in SUP_TITULOS:
        for i in range(sup_start, indice):
            if lineas[i].strip() == titulo:
                posiciones.append((i, titulo))
                break
    posiciones.sort()
    salida = []
    for k, (i, titulo) in enumerate(posiciones):
        fin = posiciones[k + 1][0] if k + 1 < len(posiciones) else indice
        parte = extraer_parte(lineas[i + 1:fin])
        if not parte:
            continue
        parte.update({'orden': k + 1, 'titulo': titulo})
        salida.append(parte)
    return salida


def extraer_devociones():
    salida = []
    for n, pagina in enumerate(range(204, 211), 1):
        raw = leer_pdf(paginas=(pagina, pagina))
        ps = a_parrafos(raw.split('\n'))
        if len(ps) < 3:
            raise SystemExit('Devoción incompleta en la página %d.' % pagina)
        dia, titulo = ps[0], ps[1]
        cuerpo = '\n\n'.join(ps[2:])

        fuente = None
        m = DEV_SRC_RE.search(cuerpo)
        if m:
            fuente = espacios(m.group(1))
            cuerpo = (cuerpo[:m.start()] + cuerpo[m.end():]).strip()

        cuerpo, parrafos = limpiar_cuerpo(cuerpo)
        if parrafos:
            # letra capital separada en el PDF: «S i» → «Si», «E l» → «El»
            parrafos[0] = re.sub(r'^([A-ZÁÉÍÓÚÑ])\s+([a-záéíóúñ])',
                                 r'\1\2', parrafos[0])
            cuerpo = '\n\n'.join(parrafos)

        salida.append({
            'orden': n,
            'dia_semana': dia,
            'titulo': titulo,
            'titulo_html': enlazar(titulo),
            'texto': cuerpo,
            'parrafos': parrafos,
            'parrafos_html': [enlazar(p) for p in parrafos],
            'fuente': fuente,
            'fuentes': [fuente] if fuente else [],
            'pagina_pdf': pagina,
        })
    return salida


def meta(pdf, diario, devociones, suplemento):
    titulo = 'Maná Diario Celestial para la Familia de la Fe'
    return {
        'titulo': titulo,
        'edicion': 'Spanish Edition',
        'editorial': 'Asociación de los Estudiantes de la Biblia el Alba',
        'pdf': os.path.abspath(pdf),
        'extraido': date.today().isoformat(),
        'dias': len(diario),
        'devociones': len(devociones),
        'suplemento': len(suplemento),
        'nota': ('El año incluye el 29 de febrero (366 entradas). '
                 'Las fechas se guardan como mes y día, sin año. '
                 'Dos entradas no traen fuente impresa en el PDF '
                 '(13 de junio y 17 de octubre).'),
    }


def escribir_json(nombre, datos):
    ruta = os.path.join(BASE, nombre)
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=1)
    return ruta


def generar_vista(completo):
    datos = json.dumps(completo, ensure_ascii=False).replace('</', '<\\/')
    plantilla = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Maná Diario Celestial — vista previa</title>
<style>
  :root{--papel:#fbf8f1;--papel2:#fffdf8;--tinta:#1c2430;--gris:#6b6459;
        --azul:#1d3a6b;--azul2:#2b5390;--oro:#b8892b;--linea:#ded5c3}
  *{box-sizing:border-box}
  body{margin:0;background:var(--papel);color:var(--tinta);
       font-family:Georgia,"Times New Roman",serif;font-size:16.5px;line-height:1.55}
  header{background:linear-gradient(180deg,#14243f,#1d3a6b);color:#f6f1e4;
         padding:18px 22px 16px;border-bottom:4px solid var(--oro)}
  header h1{margin:0;text-align:center;font-size:1.45em;letter-spacing:.03em}
  header p{margin:5px 0 0;text-align:center;color:#e6d4a0;font-style:italic;font-size:.9em}
  .contenedor{max-width:1100px;margin:0 auto;padding:18px 20px 50px}
  .aviso{font-size:.8em;color:var(--gris);margin:0 0 14px}
  .tabs{display:flex;gap:9px;flex-wrap:wrap;position:sticky;top:0;z-index:10;
        background:var(--papel);padding:10px 0;border-bottom:1px solid var(--linea)}
  .tab{border:1px solid var(--linea);background:var(--papel2);color:var(--azul);
       border-radius:20px;padding:8px 15px;font:inherit;font-size:.9em;cursor:pointer}
  .tab.activo{background:var(--azul);color:#fff;border-color:var(--azul)}
  .barra{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:12px 0}
  .barra input{flex:1;min-width:220px;padding:10px 14px;border:1px solid var(--linea);
               border-radius:8px;font:inherit;background:#fff}
  .barra select{padding:9px 12px;border:1px solid var(--linea);border-radius:8px;
                font:inherit;background:#fff}
  .cuenta{font-size:.82em;color:var(--gris)}
  .dos{display:grid;grid-template-columns:260px minmax(0,1fr);gap:20px;align-items:start}
  .lista{background:#fff;border:1px solid var(--linea);border-radius:8px;
         max-height:70vh;overflow:auto;padding:6px}
  .lista button{display:block;width:100%;text-align:left;border:0;background:none;
        border-bottom:1px solid #f0eadf;padding:7px 9px;font:inherit;font-size:.88em;
        color:var(--tinta);cursor:pointer;border-radius:5px}
  .lista button:hover{background:#f6efe2}
  .lista button.activo{background:#f3e7c9;color:var(--azul);font-weight:700}
  .lista .ref{display:block;color:var(--gris);font-size:.8em;font-weight:400;margin-top:2px}
  .detalle{background:var(--papel2);border:1px solid var(--linea);border-radius:8px;
           padding:26px 30px;min-height:55vh}
  .detalle .fecha{margin:0 0 6px;color:var(--oro);font-size:.8em;letter-spacing:.12em;
                  text-transform:uppercase;font-weight:700}
  .detalle h2{margin:0 0 12px;color:var(--azul);font-size:1.35em}
  .cita{margin:0 0 4px;font-style:italic;color:#3d4a5e;font-size:1.02em}
  .referencia{margin:0 0 16px;color:var(--azul);font-style:italic;font-size:.92em}
  .detalle p.texto{margin:0 0 .9em;text-align:justify;hyphens:auto;text-indent:1.4em}
  .detalle p.texto:first-of-type{text-indent:0}
  .fuente{margin:18px 0 0;padding-top:10px;border-top:1px solid var(--linea);
          color:var(--gris);font-size:.8em}
  .nav{display:flex;justify-content:space-between;gap:10px;margin:16px 0 0;
       border-top:1px solid var(--linea);padding-top:12px}
  .nav button{border:1px solid var(--linea);background:#fff;color:var(--azul);
       border-radius:16px;padding:6px 13px;font:inherit;font-size:.85em;cursor:pointer}
  .nav button:hover{background:var(--azul);color:#fff}
  .vacio{padding:30px;text-align:center;color:var(--gris)}
  .nota{font-size:.8em;color:var(--gris);border-top:1px solid var(--linea);
        margin-top:26px;padding-top:10px}
  @media(max-width:760px){
    .dos{grid-template-columns:1fr}
    .lista{max-height:35vh}
    .detalle{padding:20px 18px}
    header h1{font-size:1.15em}
  }
</style>
</head>
<body>
<header>
  <h1>Maná Diario Celestial</h1>
  <p>para la Familia de la Fe · vista previa de la extracción</p>
</header>
<div class="contenedor">
  <p class="aviso">Contenido extraído del PDF «ManaDiario.pdf»: 366 días, 7 devociones matutinas y 10 voces del suplemento. La biblioteca lo muestra en la pestaña «Hoy»; esta página es una vista de consulta.</p>
  <nav class="tabs">
    <button class="tab activo" data-vista="diario">Maná diario (366)</button>
    <button class="tab" data-vista="devociones">Devociones matutinas (7)</button>
    <button class="tab" data-vista="suplemento">Suplemento (10)</button>
  </nav>

  <section id="vista-diario">
    <div class="barra">
      <select id="mes"><option value="">Todos los meses</option></select>
      <input id="buscar" type="search" placeholder="Buscar por fecha, referencia o texto…">
      <span class="cuenta" id="cuenta"></span>
    </div>
    <div class="dos">
      <aside class="lista" id="lista-diario"></aside>
      <article class="detalle" id="detalle-diario"></article>
    </div>
  </section>

  <section id="vista-devociones" hidden>
    <div class="dos">
      <aside class="lista" id="lista-dev"></aside>
      <article class="detalle" id="detalle-dev"></article>
    </div>
  </section>

  <section id="vista-suplemento" hidden>
    <div class="dos">
      <aside class="lista" id="lista-sup"></aside>
      <article class="detalle" id="detalle-sup"></article>
    </div>
  </section>

  <p class="nota">Fuente: «Maná Diario Celestial para la Familia de la Fe», edición en español, 210 páginas. Los días 13 de junio y 17 de octubre no traen fuente impresa en el PDF.</p>
</div>
<script>
const DATA = __DATOS__;
const MESES = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
let idxDiario = 0, filtroMes = '', filtroTexto = '';
let idxDev = 0, idxSup = 0;

function norm(s){
  return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
}
function etiqueta(d){ return d.dia + ' de ' + MESES[d.mes-1]; }

function crearListaDiario(){
  const cont = document.getElementById('lista-diario');
  const q = norm(filtroTexto);
  const items = DATA.mana_diario.filter(d => {
    if(filtroMes && String(d.mes) !== filtroMes) return false;
    if(!q) return true;
    return norm(d.clave + ' ' + etiqueta(d) + ' ' + d.referencia + ' ' + d.cita + ' ' + d.texto).includes(q);
  });
  document.getElementById('cuenta').textContent = items.length + ' de ' + DATA.mana_diario.length + ' días';
  cont.innerHTML = '';
  if(!items.length){ cont.innerHTML = '<p class="vacio">Sin coincidencias.</p>'; return; }
  items.forEach(d => {
    const b = document.createElement('button');
    b.innerHTML = '<span>' + etiqueta(d) + '</span><span class="ref">' + esc(d.referencia) + '</span>';
    if(d.orden - 1 === idxDiario) b.classList.add('activo');
    b.onclick = () => { idxDiario = d.orden - 1; crearListaDiario(); mostrarDiario(); };
    cont.appendChild(b);
  });
}

function esc(s){ return String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }

function mostrarDiario(){
  const d = DATA.mana_diario[idxDiario];
  const c = document.getElementById('detalle-diario');
  if(!d){ c.innerHTML = '<p class="vacio">Sin datos.</p>'; return; }
  c.innerHTML = '<p class="fecha">' + etiqueta(d) + '</p>' +
    '<h2>' + esc(d.referencia) + '</h2>' +
    '<p class="cita">“' + esc(d.cita) + '”</p>' +
    (d.parrafos.length ? d.parrafos.map(p => '<p class="texto">' + esc(p) + '</p>').join('') : '<p class="texto">' + esc(d.texto) + '</p>') +
    '<p class="fuente">' + (d.fuente ? 'Fuente: ' + esc(d.fuente) : 'El PDF no imprime fuente para este día.') + '</p>' +
    '<div class="nav"><button id="ant">← Día anterior</button><button id="sig">Día siguiente →</button></div>';
  c.querySelector('#ant').onclick = () => { idxDiario = (idxDiario + DATA.mana_diario.length - 1) % DATA.mana_diario.length; crearListaDiario(); mostrarDiario(); };
  c.querySelector('#sig').onclick = () => { idxDiario = (idxDiario + 1) % DATA.mana_diario.length; crearListaDiario(); mostrarDiario(); };
}

function crearListaDev(){
  const cont = document.getElementById('lista-dev'); cont.innerHTML = '';
  DATA.devociones_matutinas.forEach((d, i) => {
    const b = document.createElement('button');
    b.innerHTML = '<span>' + esc(d.dia_semana) + '</span><span class="ref">' + esc(d.titulo) + '</span>';
    if(i === idxDev) b.classList.add('activo');
    b.onclick = () => { idxDev = i; crearListaDev(); mostrarDev(); };
    cont.appendChild(b);
  });
}
function mostrarDev(){
  const d = DATA.devociones_matutinas[idxDev];
  const c = document.getElementById('detalle-dev');
  c.innerHTML = '<p class="fecha">Devociones matutinas</p><h2>' + esc(d.dia_semana) + ' — ' + esc(d.titulo) + '</h2>' +
    d.parrafos.map(p => '<p class="texto">' + esc(p) + '</p>').join('') +
    '<p class="fuente">' + (d.fuente ? 'Fuente: ' + esc(d.fuente) : '') + '</p>';
}

function crearListaSup(){
  const cont = document.getElementById('lista-sup'); cont.innerHTML = '';
  DATA.suplemento.forEach((d, i) => {
    const b = document.createElement('button');
    b.innerHTML = '<span>' + esc(d.titulo) + '</span><span class="ref">' + esc(d.referencia) + '</span>';
    if(i === idxSup) b.classList.add('activo');
    b.onclick = () => { idxSup = i; crearListaSup(); mostrarSup(); };
    cont.appendChild(b);
  });
}
function mostrarSup(){
  const d = DATA.suplemento[idxSup];
  const c = document.getElementById('detalle-sup');
  c.innerHTML = '<p class="fecha">Suplemento</p><h2>' + esc(d.titulo) + '</h2>' +
    '<p class="cita">“' + esc(d.cita) + '”</p><p class="referencia">— ' + esc(d.referencia) + '</p>' +
    d.parrafos.map(p => '<p class="texto">' + esc(p) + '</p>').join('') +
    '<p class="fuente">' + (d.fuente ? 'Fuente: ' + esc(d.fuente) : '') + '</p>';
}

document.querySelectorAll('.tab').forEach(t => {
  t.onclick = () => {
    document.querySelectorAll('.tab').forEach(x => x.classList.remove('activo'));
    t.classList.add('activo');
    document.querySelectorAll('section[id^="vista-"]').forEach(s => s.hidden = true);
    document.getElementById('vista-' + t.dataset.vista).hidden = false;
  };
});

const sel = document.getElementById('mes');
MESES.forEach((m, i) => { const o = document.createElement('option'); o.value = i+1; o.textContent = m; sel.appendChild(o); });
sel.onchange = () => {
  filtroMes = sel.value;
  if(filtroMes){
    const primero = DATA.mana_diario.find(d => String(d.mes) === filtroMes);
    if(primero) idxDiario = primero.orden - 1;
  }
  crearListaDiario(); mostrarDiario();
};
document.getElementById('buscar').oninput = e => { filtroTexto = e.target.value; crearListaDiario(); };

crearListaDiario(); mostrarDiario(); crearListaDev(); mostrarDev(); crearListaSup(); mostrarSup();
</script>
</body>
</html>'''
    plantilla = plantilla.replace('__DATOS__', datos)
    plantilla = plantilla.replace('__FECHA__', date.today().isoformat())
    ruta = os.path.join(BASE, 'vista-previa.html')
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(plantilla)
    return ruta


def escribir_leeme(meta_datos, diario):
    sin_fuente = ['%02d-%02d' % (d['mes'], d['dia']) for d in diario if not d['fuente']]
    multi = ['%02d-%02d' % (d['mes'], d['dia']) for d in diario if len(d['fuentes']) > 1]
    texto = f'''# Maná Diario Celestial — datos extraídos

Contenido extraído del PDF `ManaDiario.pdf` (210 páginas), copiado en esta carpeta.

## Archivos

- `mana-diario.json` — 366 días (incluye el 29 de febrero), de enero a diciembre.
- `devociones-matutinas.json` — las 7 devociones semanales (Domingo a Sábado).
- `suplemento.json` — las 10 voces finales del libro (Oración, Paciencia, etc.).
- `mana-completo.json` — todo junto con los datos de la edición.
- `vista-previa.html` — página para leer y buscar el contenido (abrir con el navegador).
- `ManaDiario.pdf` — copia del PDF original dentro del sistema.
- También se puede consultar desde la biblioteca: `http://127.0.0.1:8099/mana`.
- `extraer_mana.py` — script que regenera todo desde el PDF.

## Formato de cada día

```json
{{
  "orden": 1,
  "dia": 1, "mes": 1, "mes_nombre": "enero", "clave": "01-01",
  "cita": "texto del versículo",
  "referencia": "Salmo 66:8, 9",
  "referencia_normal": "Salmos 66:8, 9",
  "texto": "párrafo 1\\n\\npárrafo 2",
  "parrafos": ["párrafo 1", "párrafo 2"],
  "fuente": "Z. '03-3",
  "fuentes": ["Z. '03-3"]
}}
```

## Notas

- El libro trae **366** entradas: incluye el 29 de febrero, por lo que sirve para años bisiestos. Las fechas se guardan como mes y día, sin año.
- **{len(sin_fuente)} días no traen fuente impresa** en el PDF: {', '.join(sin_fuente) or '—'}.
- **{len(multi)} días traen dos citas Z.** (se conservan ambas en `fuentes`): {', '.join(multi) or '—'}.
- Las devociones matutinas son 7 lecturas semanales; se conservan con su día, título, texto y fuente.
- El suplemento son las 10 voces que el libro incluye después del 31 de diciembre, antes del índice temático.
- Al texto se le quitaron los saltos de línea del PDF, se corrigieron las letras capitales separadas de las devociones y se conservaron los párrafos. Las citas y referencias se conservan tal como aparecen, con ligeras normalizaciones de espacios.
- La portada **Hoy** de la biblioteca ya muestra el maná y la devoción del día. Los archivos quedan en esta carpeta para futuras ampliaciones.
- Los campos `cita_html`, `referencia_html` y `parrafos_html` contienen las referencias bíblicas ya enlazadas para la portada de la biblioteca.

## Regenerar

```bash
python3 extraer_mana.py /ruta/al/ManaDiario.pdf
```

Requiere `pdftotext` (paquete `poppler-utils`).
'''
    with open(os.path.join(BASE, 'LEEME.md'), 'w', encoding='utf-8') as f:
        f.write(texto)


def main():
    if not os.path.isfile(PDF):
        raise SystemExit('No se encuentra el PDF: ' + PDF)
    raw = leer_pdf()
    diario, lineas, _ultima_fecha, sup_start = extraer_diario(raw)
    suplemento = extraer_suplemento(lineas, sup_start)
    devociones = extraer_devociones()

    # validaciones
    if len(diario) != 366:
        raise SystemExit('Se esperaban 366 días y se obtuvieron %d.' % len(diario))
    claves = {(d['mes'], d['dia']) for d in diario}
    for mes in range(1, 13):
        import calendar
        for dia in range(1, calendar.monthrange(2024, mes)[1] + 1):
            if (mes, dia) not in claves:
                raise SystemExit('Falta el día %02d-%02d.' % (mes, dia))
    if len(devociones) != 7:
        raise SystemExit('Se esperaban 7 devociones y se obtuvieron %d.' % len(devociones))
    if len(suplemento) != 10:
        raise SystemExit('Se esperaban 10 voces del suplemento y se obtuvieron %d.' % len(suplemento))

    m = meta(PDF, diario, devociones, suplemento)
    escribir_json('mana-diario.json', diario)
    escribir_json('devociones-matutinas.json', devociones)
    escribir_json('suplemento.json', suplemento)
    completo = {'meta': m, 'mana_diario': diario,
                'devociones_matutinas': devociones, 'suplemento': suplemento}
    escribir_json('mana-completo.json', completo)
    generar_vista(completo)
    escribir_leeme(m, diario)

    sin_fuente = [d['clave'] for d in diario if not d['fuente']]
    multi = [d['clave'] for d in diario if len(d['fuentes']) > 1]
    print('Días:', len(diario))
    print('Devociones:', len(devociones))
    print('Suplemento:', len(suplemento))
    print('Sin fuente:', ', '.join(sin_fuente) or 'ninguno')
    print('Con dos fuentes:', ', '.join(multi) or 'ninguno')
    print('Carpeta:', BASE)


if __name__ == '__main__':
    main()
