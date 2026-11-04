# Auditoría de contenido — Biblioteca de Estudios

Fecha: 2026-11-01

## Foto-Drama de la Creación (añadido el 2026-11-02)

- 102 capítulos, 378 ilustraciones y 259 citas bíblicas.
- Origen: `SpanishPhotoDrama.pdf` (202 páginas), con el texto y las láminas originales.
- 0 citas desalineadas y 0 posiciones fuera de rango.
- Se muestra después de *Sombras del Tabernáculo* en «Obras».

## Índice temático y Foto-Drama

- **666 voces** del índice temático enlazan con el Foto-Drama.
- **1.472 enlaces** a capítulos del Foto-Drama, mostrados al final de cada voz.

## Optimización final (2026-11-02)

- Base de datos compactada (`VACUUM`): **34,1 MB**, sin páginas libres.
- Estadísticas recalculadas (`ANALYZE`), índice de búsqueda optimizado y nuevo
  índice por obra (`paginas(titulo_obra, pagina)`).
- **217 páginas**, **5.628 citas**, **1.472 enlaces** del índice al Foto-Drama.
- **0 citas inválidas**, **0 desalineadas** y **0 enlaces temáticos fuera de rango**.
- Presentación y «Derechos y propósito» del Foto-Drama corregidas de mayúsculas
  y palabras pegadas; referencia de Apocalipsis 22:1,2 corregida.
- Respaldos iniciales en segundo plano y sin las 378 ilustraciones estáticas;
  el servidor arranca de inmediato.
- Los enlaces abren el capítulo y resaltan la frase donde aparece el término.

## Maná diario

- Días: 366 (incluye 29 de febrero).
- Sin fuente impresa: 06-13, 10-17.
- Con dos citas Z.: 3 (09-28; 11-02; 11-26).

## Índice temático

- Referencias distintas en el índice: 2904.
- Enlazadas por refmap/tmap: 2864.
- Sin enlace: 40 (J/K externas: 25; años/erratas: 15).
  - J/K: J1, J10, J11, J12, J13, J14, J15, J16, J2, J258, J267, J3, J4, J5, J552, J6, J635, J7, J8, J9, K1, K2, K3, K4, K5
  - Años/erratas: B1260, B1873, B1878, B2500, B470, B597, C1290, C1335, C533, C689, D1858, D1893, E515, E633, E771

## Marcas de página

- Referencias cuya marca [A…]/[T…] no aparece literalmente en el texto: 394.
  - **312 del índice general** con `aprox=1`: abren el párrafo por contexto (`refctx`), no por una marca literal.
  - **5 del Tabernáculo** con `aprox=1`.
  - **77 del Tabernáculo** con `aprox=0`: son referencias de página (T18–T24, T28–T45, etc.) que abren el capítulo o la página correspondiente, aunque el texto no conserve el corchete `[T…]`.
  - Ejemplos: F40, F69, E421, F552, F142, C277, B196, F242, F36, D329, E249, C292, E456, D413, F285, B185, F519, B164, A37, A89, F70, E214, D14, F664, C281, F709, C121, D421, F47, D469

## Traducción del índice

- **Términos españoles repetidos: 0**. Se desambiguaron las 39 parejas/grupos que compartían etiqueta. Ejemplos:
  - ENFERMEDADES → Afecciones, Enfermedades, Dolencias.
  - ESPÍRITU → Licor, Espíritu, Espíritus.
  - CARNE → Carne, Comida.
  - CASTIGO → Corrección, Castigo.
  - ESCLAVITUD → Cautiverio, Servidumbre, Esclavitud.
  - HERENCIA → Descendencia, Herencia.
  - HIJO → Hijo, Filiación.
  - JUSTICIA → Justicia, Rectitud.
  - TIERRA → Tierra, Territorio.
  - VOLUNTAD → Voluntad, Disposición.
- Se actualizaron también `tnorm` y `letra`, por lo que la búsqueda y las letras del índice usan las etiquetas nuevas.

## Revisión editorial 2026-11-01

- **Tomos 2–6 revisados** con el mismo método: títulos, arranques, comillas, tablas, citas, marcas y bloques sin traducir.
- **Tomos 3, 4, 5 y 6**: 54 páginas editadas, 38 títulos corregidos y 7 bloques en inglés traducidos (Tomo 4, págs. 10–11; Tomo 5, págs. 9 y 16; Tomo 6, pág. 14; Tomo 3, pág. 1).
- **Citas**: 5.362 en toda la biblioteca; 721 en el Tomo 2, 406 en el Tomo 3, 665 en el Tomo 4, 1.417 en el Tomo 5 y 1.055 en el Tomo 6. Todas alineadas con su texto.
- **Tomo 2 — Daniel 12:4, 9, 10**: la frase «Daniel (12:4, 9, 10)» del Estudio 1 quedó subrayada y enlazada; abre Daniel 12 y destaca el pasaje 4–10.
- **Referencias con paréntesis**: el extractor reconoce ahora «Libro (capítulo:versículos)». Se añadieron enlaces en 29 páginas de los tomos 0–6 (por ejemplo, «Daniel (12:1)», «Apocalipsis (18:4)», «Lucas (21:25,26)»).
- **Tomo 6 — Estudio 1 completado**: se añadieron los días quinto, sexto y séptimo, el período de descanso, el relato de Génesis, la creación gradual, el hombre creado y no evolucionado y el apéndice sobre las aptitudes humanas.
- **Tomo 6 — estructura**: 141 encabezados de sección, párrafos largos divididos en bloques legibles, comillas normalizadas a «» y títulos internos corregidos.
- **Índice de secciones**: el lector y la pestaña «Leer» muestran «En este capítulo (N)» con enlaces a cada encabezado y desplazamiento directo al tema.
- **Limpieza global final**: corregidos los cortes «d.⏎C.» del Tomo 2, «vol. Yo», comillas invertidas, comillas vacías y guiones sueltos. Se normalizaron las comillas curvas de los tomos 3–5 y se corrigieron mayúsculas indebidas como «y Los nestorianos», «en Este nuestro país» o «parábola de La Vid». El escaneo final no encuentra caracteres de control, comillas rectas, dobles espacios ni referencias con espacios internos.
- **Integridad**: 0 citas inválidas, 0 citas desalineadas, 0 posiciones de `refctx` fuera de rango y 0 marcas desalineadas. Índice de búsqueda reconstruido.
- Informes por tomo: `tomo3-revision.md`, `tomo4-revision.md`, `tomo5-revision.md`, `tomo6-revision.md` y `tomo2-revision.md`.

## Pendientes detectados

- **Marcas globales**: las 394 referencias sin corchete literal siguen abriendo el párrafo o la página correctos por contexto; no impiden la consulta del índice. Comprobadas: 0 posiciones fuera de rango. Las 77 referencias de página del Tabernáculo son exactas; las demás son aproximadas por diseño.
- **Lectura fina del Tomo 3**: completada una pasada de los Estudios 3–10 (detalle en `tomo3-revision.md`). Se restauraron dos pasajes del Estudio 4 que faltaban (la explicación de 381/539 y la cuenta de 1810 años hasta 1846), se corrigió la fecha de las 95 tesis (31 de octubre de 1517) y se repararon duplicaciones, fechas `A.D.`, corchetes y comillas. Queda una revisión frase por frase más profunda de los Estudios 6, 8 y 10, los más extensos.
- **Tomo 3, Estudio 8 — restauración importante**: la página tenía solo 3.609 palabras de las 21.150 del PDF. Se añadieron 16.907 palabras que faltaban (secciones desde «Afirman que errar es humano…» hasta el párrafo 164). Quedó en 20.494 palabras, 121.607 caracteres y 108 citas. Continúa estudio por estudio.
- **Completitud por estudio**: se compararon las palabras de los tomos 3–6 con sus PDFs. No aparecieron otras truncaciones graves; las diferencias restantes corresponden a índices de textos bíblicos, notas al pie y estudios muy breves.
- **Tomo 3, Estudios 4–7, 9 y 10**: verificados inicio, final y conteo. El Estudio 10 recuperó el cierre «¡Amén! ¡Amén! ¡Venga tu reino!…» y se corrigió «Pozo del olvido».
- **Tomos 4–6**: finales y conteos revisados; sin vacíos equivalentes al Estudio 8.
- **Tomo 4, Estudio 1**: corregidos «el día ardedor» → «el día que arderá», «serán hojarasca» → «serán como paja» (Malaquías 4:1) y «en donde» → «respecto al cual».
- **Estilo V4–6**: sin comillas invertidas, curvas residuales, espacios antes de puntuación, palabras repetidas ni puntos dobles.
- **Tomo 5, Estudio 1**: «discernir», «detalles de la fe», «edificio de la fe», «Que el hombre», «multiforme sabiduría», «alabándole» y la cita de 2 Tesalonicenses 1:9 («lejos de la presencia del Señor»).
- **Tomo 5 cerrado**: 17 páginas, 163.706 palabras y 1.417 citas. Inicios y finales completos, sin truncaciones ni defectos de comillas, puntuación o espacios. La diferencia del Estudio 16 corresponde al índice de textos bíblicos.
- **Tomo 6, Estudio 2**: «confusa y complicada», «significado real», «unos ayudantes», «retroceder varios años», «siglo IV», «Este extravío», «vía libre», «para nuestra instrucción» y «discípulo del Señor y andar por la luz».
- **Tomo 6 cerrado**: 18 páginas, 250.924 palabras y 1.055 citas. Revisados los 17 estudios y el prólogo; se corrigieron frases dañadas, más de sesenta duplicaciones («daño y daño», «pruebas y pruebas», «balanzas o balanzas», «juicio o juicio»…), calcos, referencias incompletas y citas sin cierre. Sin truncaciones ni comillas de cierre huérfanas.
- **Tomo 6 — detalles**: reconstruidos Génesis 1:2 («sin forma (sin orden) y vacía, desolada y oscura»), la nota de «1 pie = 30 cm», 2 Tesalonicenses 2, Hebreos 4, Efesios 5, 1 Corintios 7 y Santiago 5; aclarada la sección sobre *Easter* / Pascua; traducidos *return/depart*; cerrada la referencia 2 Ped. 1:10,11.

## Optimización (versión 1.2.8)

- Base de datos en **modo WAL**, `synchronous=NORMAL`, caché de 64 MB, `temp_store=MEMORY` y `mmap_size` de 128 MB.
- El índice temático usa la columna `letra` y el índice `ix_temas_letra`.
- La galería del Foto-Drama se calcula una vez y queda en memoria.
- Mejoras medidas con la biblioteca en marcha:
  - Índice temático por letra: 10,8 ms → 2,2 ms.
  - Galería: 6,4 ms → 2,6 ms.
  - Capítulo largo: 8,9 ms → 6,6 ms.
  - Estado: 2,8 ms → 1,9 ms.
  - Búsqueda: ~40 ms.
- Comprobado en el navegador: capítulo de 263 párrafos, galería de 378 láminas e índice de 500 voces, sin errores de consola.

## Calidad de la interfaz

- Lighthouse: **Accesibilidad 100**, **Buenas prácticas 100** y **SEO 100**.
- Se corrigió la estructura ARIA de las pestañas, el contraste del dorado y se añadió la descripción de la página.

## Estética «biblioteca-museo» (fase 2)

- **Lector editorial**: cabecera de capítulo con palabras, minutos de lectura y citas; entradilla destacada; figuras con marco y pie; barra dorada de progreso; botón flotante «↑ Índice»; columna de lectura centrada y modo noche.
- **Galería**: nueva pestaña con las **378 láminas** del Foto-Drama, filtro por título/capítulo y visor con anterior, siguiente y «Leer el capítulo». También hay tarjeta de acceso en Obras.
- **Biblia visual**: cabecera de testamento, libro y capítulo con recuento de versículos y comentados; tarjeta del versículo del día; audio rediseñado; círculos animados en los versículos comentados; «Ver contexto y comentarios» abre directamente el cuadro del pasaje.
- **Índice temático visual**: riel A–Z desplazable, voces en tarjetas con letra y número de referencias, y miniaturas de los capítulos del Foto-Drama dentro de cada voz.
- **Rutas y curiosidades**: seis itinerarios en tarjetas con pasos numerados (incluidos el Foto-Drama y los seis tomos) y ocho datos del corpus calculados en vivo: palabras, citas, versículo y voz más comentados, láminas y enlaces al Foto-Drama.
- **Cabecera ordenada**: rejilla de siete columnas que coloca las catorce pestañas en dos filas parejas; «Cronología», «Volumen» y «Fuente» quedan dentro de la misma retícula, sin sobresalir. Los iconos de volumen y auriculares son SVG, no emojis, para que se vean igual en cualquier equipo.
- Sin errores de consola; probado en escritorio y en la copia instalada.

## Audio

- El Maná diario, las Devociones Matutinas y el lector leen las referencias como «Santiago capítulo 3 versículo 2». Se admiten rangos, listas, abreviaturas, números romanos y libros de un solo capítulo. Detalle en `audio-versiculos.md`.
- **Volumen de la narración**: ganancia de Web Audio con limitador, del 50 al 300 %, aplicada a la Biblia y a las voces de edge-tts. El valor inicial es 180 % y se guarda en el navegador. Se ajusta desde el botón «🔊 Volumen» de la cabecera o desde el deslizador del reproductor bíblico; el volumen general del sistema sigue siendo el mando principal.
- **Capítulo completo en audio**: el lector principal y la ventana de lectura ofrecen «🎧 Escuchar capítulo» en todos los tomos, *Sombras del Tabernáculo*, el Foto-Drama, el Maná y las devociones. El texto se limpia de marcas y se divide en tramos de 3.200 caracteres; cada tramo se sintetiza y se reproduce en cadena, con el siguiente preparado mientras suena el actual. El botón muestra «Detener · 3/45» y el capítulo largo ya no se corta a los 12.000 caracteres.

## Notas

- Las referencias J/K pertenecen a obras que no están en la biblioteca; se muestran como texto.
- Los años del índice original se muestran como texto, no como referencias.
- La revisión de la traducción de los tomos 2–6 requiere lectura comparada con los PDFs; este informe solo detecta patrones.
- «Buscar palabra» incluye el botón **Exportar resultados**, que descarga un Markdown con la consulta, el total y cada página encontrada.
