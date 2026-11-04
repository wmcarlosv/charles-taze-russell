# Estudios de las Escrituras de C. T. Russell

Biblioteca digital en español de las obras de Charles Taze Russell:

- **Estudios de las Escrituras**, seis tomos.
- **Sombras del Tabernáculo**.
- **Foto-Drama de la Creación**: 102 capítulos y 378 láminas.
- **Biblia Reina-Valera 1960** con referencias y comentarios.
- **Maná diario** y **Devociones Matutinas**.
- **Audio narrado** de la Biblia: 1.189 capítulos.

Sitio público: <https://charlestazerussell.online/>

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

## Despliegue web

En el servidor, la aplicación escucha solo en `127.0.0.1:8099` y Apache la
publica con HTTPS en la raíz del dominio. El servicio systemd es
`biblioteca-espanola.service`.

## Créditos

Textos originales de Charles Taze Russell (1879–1916), de dominio público.
Las citas bíblicas en español proceden de la Reina-Valera 1960.
