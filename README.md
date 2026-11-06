# Estudios de las Escrituras de C. T. Russell

Biblioteca digital en español de las obras de Charles Taze Russell:

- **Estudios de las Escrituras**, seis tomos.
- **Sombras del Tabernáculo**.
- **Foto-Drama de la Creación**: 102 capítulos y 378 láminas.
- **Escritos del pastor Russell para Overland Monthly**: 98 artículos (1909-1916), con la numeración original **OV1–OV449** visible en el texto, buscable e integrado en el índice temático.
- **Lo que dijo el pastor Russell**: 1.394 temas en orden alfabético, con preguntas y respuestas de 1905–1916, las marcas originales **Q5–Q853** y la numeración de preguntas **Q5:1, Q5:2…** visibles y buscables, referencias bíblicas enlazadas, presencia en el índice temático y audio bajo demanda.
- **Biblia Reina-Valera 1960** con referencias y comentarios.
- **Maná diario** y **Devociones Matutinas**.
- **Audio narrado** de la Biblia: 1.189 capítulos.

Sitio público: <https://charlestazerussell.online/>

## Herramientas de lectura

- **Reportar error** desde el lector: guarda obra, artículo, página, párrafo y comentario.
- **Panel de reportes** para revisar, marcar como resueltos o borrar los errores enviados.
- **Copiar enlace** al párrafo exacto (el enlace abre el lector y resalta ese párrafo), **copiar cita** con obra, artículo, página y marca Q cuando existe, y **compartir** con el móvil.
- **Ver original**: página escaneada de Overland Monthly y PDF de revistas y tomos.
- **Continuar donde lo dejé**: recupera el último capítulo y la posición de lectura.
- **Etiquetas y filtro** en los marcadores del cuaderno.
- **Controles de lectura**: fuente, tamaño, interlineado y ancho de columna.
- **Búsquedas guardadas** y filtro por año para repetir consultas frecuentes.
- **Panel de progreso** con páginas, citas y temas por obra.
- **Audio** con velocidad ajustable (0,8×–1,5×), temporizador, reproducción continua y reanudación de la posición.
- **Uso sin conexión**: la aplicación se instala como PWA, avisa de actualizaciones y muestra cuándo está sin conexión.

## Estructura

| Archivo | Para qué sirve |
| --- | --- |
| `biblioteca-espanola/app.html` | Interfaz: lector, Biblia, Foto-Drama, buscador, Maná y audio. |
| `biblioteca-espanola/asistente.py` | Servidor local (puerto 8099) y API. |
| `biblioteca-espanola/manifest.json` | Manifiesto PWA. |
| `datos/biblioteca-espanola.db.gz` | Base de datos comprimida. |
| `biblioteca-espanola/audio/` | Audio narrado (no incluido en git). |
| `subir.sh` | Publica los cambios del repositorio. |
| `subir_audio.py` | Publica el audio como adjuntos del release. |

## Requisitos

- Python 3.8 o superior con SQLite.
- Para el audio, los archivos MP3 del release `audio-v1`.
- Para narrar texto nuevo, `edge-tts` (ver más abajo).

## Base de datos

```bash
gunzip -c datos/biblioteca-espanola.db.gz > biblioteca-espanola/biblioteca.db
```

## Abrir la biblioteca

```bash
cd biblioteca-espanola
python3 asistente.py
```

Abre <http://127.0.0.1:8099/>.

## Audio

El audio no se guarda en el repositorio. Descarga las dos partes del release:

<https://github.com/wmcarlosv/charles-taze-russell/releases/tag/audio-v1>

y descomprímelas dentro de `biblioteca-espanola/`:

```bash
tar -xf audio-parte1.tar
tar -xf audio-parte2.tar
```

Quedan en `biblioteca-espanola/audio/` (1.189 archivos, 66 libros, 2,9 GB).

## Texto a voz (edge-tts)

La narración de cualquier texto usa **edge-tts**, las voces neuronales de
Microsoft. Se instala con:

```bash
pip install edge-tts
```

o, si el sistema lo bloquea:

```bash
pip install --user --break-system-packages edge-tts
```

Cómo funciona:

- El botón **«Escuchar capítulo»** envía el texto a `POST /api/tts`.
- El servidor genera el MP3 con la voz `es-MX-JorgeNeural` y, si no está,
  con `es-ES-AlvaroNeural`, `es-AR-TomasNeural`, etc.
- El MP3 se guarda en `tts-cache/`, identificado por un hash del texto y
  de la voz: al repetir el mismo texto se sirve al instante.
- Los capítulos largos se parten en tramos y el reproductor precarga el
  siguiente.
- El volumen se ajusta entre el 50 % y el 300 % en el reproductor; el
  volumen del sistema sigue mandando.
- Si falta `edge-tts` o no hay conexión, la biblioteca sigue funcionando
  y el lector muestra el aviso correspondiente.

## Despliegue web

En el servidor, la aplicación escucha solo en `127.0.0.1:8099` y Apache la
publica con HTTPS en la raíz del dominio. El servicio systemd es
`biblioteca-espanola.service`.

## Revisión del texto

La biblioteca se revisó a fondo para que el investigador encuentre términos,
referencias y párrafos exactos:

- 40.316 referencias bíblicas validadas contra el texto bíblico, sin citas fuera
  de capítulo o versículo.
- 849 marcas originales **Q5–Q853** conservadas y buscables, y 1.408 preguntas
  con numeración **Q5:1, Q5:2…** sin duplicados.
- Corrección de términos y erratas en los textos, el índice temático y las
  tablas de contexto: por ejemplo, «colalso» → «colirio», «Dignoes» → «Dignos»,
  «miesca» → «mies», «dócilidad» → «docilidad», «ENIMIDAD» → «ENEMISTAD».
- Normalización de nombres bíblicos en 2.433 ocurrencias: «mascotas» → «Pedro»,
  «Galón» → «Gálatas», «Memoria de sólo lectura» → «Romanos», «Trabajo» → «Job»,
  «Bruja» → «Hageo», «Columna» → «Colosenses», entre otros. La lista completa de
  ubicaciones está en `biblioteca-espanola/auditoria-nombres-biblicos.csv` y
  `biblioteca-espanola/auditoria-nombres-biblicos.md`.
- Normalización de referencias de libros de un solo capítulo y expresiones que
  habían quedado en inglés.

## Créditos

Textos originales de Charles Taze Russell (1879–1916), de dominio público.
Las citas bíblicas en español proceden de la Reina-Valera 1960.

## Preguntar a la biblioteca

La pestaña **Preguntar** responde con los propios textos de la biblioteca:

- Busca en todo el contenido (tomos, libros y revistas) con el índice interno.
- Devuelve hasta cuatro pasajes literales, cada uno con su cita:
  obra, capítulo, página y marca R si es una revista.
- Permite filtrar por obra y por año de las revistas.
- Cada fuente abre la obra en el punto exacto y resalta el pasaje.
- Sugiere temas del índice temático y permite copiar la cita.
- **Funciona sin internet**: todo se calcula en el equipo.


## Copias de seguridad

`biblioteca-espanola/backup-biblioteca.sh` guarda una copia comprimida diaria de la base en
`~/Copias/Biblioteca` y conserva las 14 más recientes. Se puede programar con un timer de systemd:

```ini
# ~/.config/systemd/user/biblioteca-backup.timer
[Timer]
OnCalendar=daily
Persistent=true
```
