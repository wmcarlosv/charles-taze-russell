# Audio — lectura hablada de referencias bíblicas

## Qué se cambió

La función `escucharTexto` de `app.html` convierte las referencias bíblicas a su forma hablada antes de enviarlas al sintetizador de voz:

- `Santiago 3:2` → **«Santiago capítulo 3 versículo 2»**.
- `Santiago 3:2-4` → **«Santiago capítulo 3 versículos 2 al 4»**.
- `Santiago 3:2, 4 y 6` → **«Santiago capítulo 3 versículos 2, 4 y 6»**.
- `Santiago 3` → **«Santiago capítulo 3»**.
- `Judas 21` → **«Judas capítulo 1 versículo 21»** (libros de un solo capítulo).
- `1 Cor. 5:7` → **«Primera de Corintios capítulo 5 versículo 7»**.
- `I Corintios 13:5` → **«Primera de Corintios capítulo 13 versículo 5»**.
- `II Timoteo 2:15` → **«Segunda de Timoteo capítulo 2 versículo 15»**.
- `Proverbios 15:23; 25:11` → **«Proverbios capítulo 15 versículo 23; Proverbios capítulo 25 versículo 11»**.
- `Daniel (12:4, 9, 10)` → **«Daniel capítulo 12 versículos 4, 9 y 10»**.

## Dónde se aplica

- **Maná diario**: el audio empieza con la referencia del día, por ejemplo «Salmos capítulo 141 versículo 3», y sigue con la cita, el comentario y las Devociones Matutinas.
- **Devociones Matutinas**: el título, que suele ser una referencia como «1 Corintios 13», se lee «Primera de Corintios capítulo 13».
- **Lector de la biblioteca**: el botón «Escuchar capítulo» también convierte las referencias que aparecen en el texto.

## Voces del sistema

- El lanzador (`lanzador.sh`) inicia `speech-dispatcher` y abre Chrome con el perfil propio de la biblioteca.
- **Importante**: ya no se usa la marca `--enable-speech-dispatcher`. Las versiones actuales de Chrome la consideran una marca no admitida y muestran el aviso «Esto afectará la estabilidad y la seguridad». Al quitarla, el navegador arranca limpio y sin advertencias.
- Si Chrome no encuentra voces, la aplicación espera un momento a que se carguen y, si siguen sin aparecer, muestra el aviso correspondiente.
- Para voces en español hace falta tener instalado un motor de voz del sistema (por ejemplo, `speech-dispatcher` con el módulo `espeak-ng` y sus datos en español).

## Voz neural edge-tts

La aplicación usa primero **edge-tts** (voces neuronales de Microsoft Edge) y, si no está disponible o no hay internet, vuelve automáticamente a la voz del navegador.

- Voces masculinas, en orden: **Jorge (México)**, Álvaro (España), Tomás (Argentina), Gonzalo (Colombia), Alonso (EE. UU.) y Sebastián (Venezuela).
- Ritmo: `-10 %`; tono: `-10 Hz`, para una lectura pausada y grave.
- El servidor expone `POST /api/tts` con `{"texto": "..."}` y devuelve el MP3.
- Los MP3 se guardan en `tts-cache/` y se reutilizan; no se incluyen en los respaldos.
- Requiere el paquete de Python y conexión a internet. Instalación:
  ```bash
  python3 -m pip install --user edge-tts
  ```
  Si el sistema no tiene `pip`, se instala antes con `get-pip.py` de PyPA.
- En los instaladores: en **Windows** edge-tts va incluido; en **Linux** es opcional y se instala con el comando anterior. Si no está, «Escuchar» sigue funcionando con las voces del navegador.
- Funciona en **Chrome, Chromium, Edge y Firefox**: la voz se genera en el servidor y el navegador solo reproduce el MP3. Si el navegador bloquea la reproducción automática, muestra un reproductor para pulsar «Play».

## Audio grabado de la Biblia

Además de la voz del sistema, la vista de cada capítulo de la Biblia incluye una
tarjeta con la **narración grabada** de la Reina-Valera 1960: reproducir, barra
de avance, tiempo y velocidad. Se sirve desde la carpeta `audio/`, no desde la
base de datos.

Los detalles técnicos y el procedimiento para cambiar de versión están en
`audio-biblia.md`.
