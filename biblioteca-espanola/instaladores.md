# Instaladores de la biblioteca (Linux y Windows)

## Qué se entrega

| Sistema | Archivo | Instala en |
|---|---|---|
| Linux | `Libreria-Estudios-Instalador-Linux.run` | `~/.local/share/Libreria estudios de las escrituras` |
| Windows | `Libreria-Estudios-Setup-Windows.exe` | `%LOCALAPPDATA%\Libreria estudios de las escrituras` |

Ambos instalan en el **disco del sistema**, crean acceso en el escritorio y en el
menú de aplicaciones, y funcionan **sin conexión a internet**. El servidor local
escucha solo en `127.0.0.1:8099`.

**Icono:** el acceso del escritorio usa el retrato del pastor Russell, el mismo
icono del instalador.

**Versión 1.2.8:** incluye el **Foto-Drama de la Creación** con sus 102
capítulos y 378 ilustraciones, además de los versículos comentados. Sus citas
están enlazadas con la RVR1960, sus versículos aparecen con círculo en la
Biblia y se integró en el índice temático, las búsquedas y «Preguntar a la
biblioteca». Incorpora la voz neural **Jorge (edge-tts)**; en Windows va
incluida y en Linux es opcional. La interfaz estrena la estética de
**biblioteca-museo**: lector editorial con progreso y minutos de lectura,
galería de las 378 láminas, Biblia visual con versículo del día, índice
temático con riel A–Z y miniaturas, y rutas y curiosidades. Añade un control
de **volumen de la narración** (50–300 %) en el botón «🔊 Volumen» y en el
reproductor de la Biblia. Todos los capítulos de los tomos, de *Sombras del
Tabernáculo* y del Foto-Drama se pueden **escuchar completos**, por tramos en
los capítulos largos. La cabecera se alinea en dos filas parejas, sin pestañas
que sobresalgan. Incluye la **revisión del Tomo 3** (pasajes restaurados,
fecha de las 95 tesis corregida y duplicaciones y referencias reparadas), la
optimización de la base (WAL, caché, índices y galería en memoria) y la guía de
uso actualizada con la consulta sin conexión de la Biblia y sus comentarios.

**Instalación por usuario, sin contraseñas.** Cada cuenta de Windows o Linux
instala su propia copia en su carpeta y no necesita permisos de administrador.
Si varias personas usan cuentas distintas en el mismo equipo, cada una ejecuta
el instalador en la suya.

## Linux

1. Dar permiso de ejecución al archivo (clic derecho → Propiedades → Permitir ejecutar).
2. Doble clic, o desde una terminal:
   ```bash
   chmod +x Libreria-Estudios-Instalador-Linux.run
   ./Libreria-Estudios-Instalador-Linux.run
   ```
3. Abre la biblioteca desde el acceso del escritorio o del menú.

No pide contraseña: instala en la carpeta personal. Requiere `python3` con
`sqlite3`, que Debian/Ubuntu ya traen.

Para desinstalar: ejecutar `desinstalar.sh` dentro de la carpeta instalada, o
borrar esa carpeta y los dos accesos directos.

## Windows

1. Doble clic en `Libreria-Estudios-Setup-Windows.exe`: empieza a instalar de
   inmediato, sin páginas de bienvenida.
2. Se instala para el usuario actual, sin pedir permisos de administrador.
3. Al terminar, puede abrir la biblioteca desde el acceso del escritorio o del
   menú Inicio.

Windows SmartScreen puede avisar que el instalador no está firmado. Es normal en
un programa artesanal sin certificado comercial: pulsar «Más información» →
«Ejecutar de todas formas». El instalador no descarga nada ni modifica el sistema
fuera de su carpeta y sus accesos.

Para desinstalar: Panel de control → Aplicaciones → «Librería Estudios de las
Escrituras», o el acceso «Desinstalar» del menú Inicio.

## Audio

El audio va dentro del instalador en formato **Opus** (32 kbps mono), pensado
para voz. Ocupa alrededor de **1,1 GB** en lugar de los 2,9 GB de los MP3
originales, y se oye igual de bien para narración. El texto y las funciones son
los mismos.

La voz neural **edge-tts** (Jorge) es opcional: se usa si el equipo tiene el
paquete `edge-tts` instalado y conexión a internet. Si no, «Escuchar» utiliza
automáticamente las voces del navegador.

## Datos personales

El cuaderno, la fuente, el tamaño y el tema se guardan en el navegador
(`localStorage`). No se borran al desinstalar la biblioteca. La base, el audio y
los respaldos van dentro de la carpeta de instalación.

## Comprobación de la versión 1.2.6

- **Linux**: instalación limpia con `HOME` y `TMPDIR` en disco; copia completa, accesos creados y servidor respondiendo.
- **Windows**: instalación limpia bajo Wine 11.21. Se copiaron 1,2 GB, el `LEEME.txt` indica 1.2.6, el Python incluido abrió la base (217 páginas) y el servidor respondió en `/api/estado`, `/api/galeria` (378 láminas), `/api/pagina`, `/api/biblia/capitulo`, las imágenes y el audio Opus. El entorno de prueba se borró después.

## Requisitos

- **Linux**: Python 3.8 o superior con `sqlite3`; un navegador (Chrome, Chromium,
  Edge o el predeterminado).
- **Windows**: Windows 10 u 11 de 64 bits; Edge ya viene instalado. No hace falta
  instalar Python.
