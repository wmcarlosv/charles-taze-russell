# Audio de la Biblia en la biblioteca

## Qué se añadió

En la vista de cada capítulo de la Biblia aparece una tarjeta de audio:

- Botón de reproducir/pausar.
- Barra de progreso con búsqueda (se puede pulsar o usar las flechas del teclado).
- Tiempo transcurrido y duración.
- Velocidad de reproducción: 1×, 1,25×, 1,5× y 2× (se recuerda en el navegador).
- Rótulo de la versión: **«Audio · Reina-Valera 1960»**.

El reproductor se coloca entre la cabecera del capítulo («Santiago 3») y el versículo 1.

## De dónde salen los archivos

- Origen: `Escritorio/RV-1960`, con una carpeta numerada por libro y un MP3 por capítulo.
- Destino: `biblioteca-ia/audio/<libro>/<capítulo>.mp3`.
- Total: **1.189 capítulos**, **2,8 GB**, un archivo por capítulo. Están todos los libros, incluido Marcos.

Los nombres de carpeta son los del texto, sin acentos y con guiones:

```
audio/genesis/1.mp3
audio/1-corintios/13.mp3
audio/salmos/150.mp3
```

## Por qué no pesa más la biblioteca

- El audio **no se guarda en SQLite** ni en los respaldos `sistema-*.tar.gz`.
- La base sigue pesando 36 MB y los respaldos unos 8 MB.
- El servidor entrega cada capítulo con **Range**, así que el navegador puede empezar a sonar sin descargar el archivo completo y puede saltar a cualquier minuto.
- El service worker **no cachea** `/audio/`; así no se llenan gigabytes en el navegador.

## Formatos

- En la biblioteca local se conservan los **MP3 originales** (2,9 GB).
- Los instaladores para Linux y Windows llevan el audio en **Opus 32 kbps mono**
  (alrededor de 1,1 GB), pensado para voz.
- El reproductor intenta primero `.opus` y, si no existe, usa `.mp3`; por eso
  funciona igual en la biblioteca local y en la instalada.

## Regenerar la carpeta de audio

```bash
cd /home/carlos/Programas/biblioteca-ia
python3 preparar-audio.py
```

El script es idempotente: copia solo lo que falta, toma el número de capítulo del
final del nombre del archivo y comprueba que cada libro tenga todos sus capítulos.

## Cambiar de versión o de narración

1. Copiar los archivos a `audio/<libro>/<capítulo>.mp3` con los mismos nombres.
2. Cambiar en `app.html` el rótulo `Audio · Reina-Valera 1960` por el de la nueva versión.
3. Si los archivos vienen por libro y no por capítulo, habrá que separarlos o
   crear una tabla de tiempos; el reproductor actual espera un MP3 por capítulo.
