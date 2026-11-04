# Pastor Russell Library

Biblioteca digital bilingüe de las obras de Charles Taze Russell:

- **Estudios de las Escrituras**, seis tomos.
- **Sombras del Tabernáculo**.
- **The Watch Tower / La Torre del Vigía**, 432 números de julio de 1879 a diciembre de 1916, sólo con los artículos de estudio.
- **Daily Heavenly Manna**, 366 lecturas diarias.
- Biblia **King James** en inglés y **Reina-Valera 1960** en la biblioteca española.
- Referencias bíblicas pulsables y traducción al español bajo demanda.

## Estructura

| Archivo | Para qué sirve |
| --- | --- |
| `app.html` | Interfaz: biblioteca, lector, Biblia, buscador y traducción. |
| `asistente.py` | Servidor local (puerto 8100) y API de traducción con caché. |
| `importar.py` | Genera `biblioteca.db` desde los PDFs, descarga la KJV y detecta citas. |
| `revistas.py` | Selecciona sólo los artículos de estudio de The Watch Tower. |
| `pulir.py` | Limpieza editorial del texto extraído de los PDFs. |
| `traducir_torre.py` | Traduce los 432 números al español y los guarda en caché. |
| `insertar_torre_es.py` | Copia los números traducidos y sus citas a la biblioteca española. |
| `sincronizar_torre.sh` | Sincronización periódica con la biblioteca española. |
| `despliegue-web/` | Configuración de Caddy y systemd para publicarla. |

## Requisitos

- Python 3 y SQLite.
- `pdftotext` (poppler-utils) para extraer el texto de los PDFs.
- Los PDFs originales de las obras y de las revistas.

## Crear la base de datos

Los PDFs se leen de las rutas indicadas al principio de `importar.py`
(`TOWERS`, `MANNA`, `TXT`). Ajusta esas rutas y ejecuta:

```bash
python3 importar.py
```

Genera `biblioteca.db` con las obras, las páginas, las citas y la Biblia.
La base no se guarda en el repositorio porque ocupa más de 100 MB.

## Abrir la biblioteca

```bash
python3 asistente.py
```

Luego abre `http://127.0.0.1:8100/`.

En el escritorio, `iniciar.sh` arranca el servidor y abre el navegador.

## Traducción al español

- El servidor traduce por párrafos y guarda el resultado en la tabla
  `traducciones` (caché por hash del texto).
- Si existe el archivo `deepl.key` con una clave de DeepL, se usa DeepL;
  si no, Google Translate. Si DeepL falla, vuelve a Google.
- `traducir_torre.py` traduce los 432 números completos, con reanudación
  automática: lo ya traducido no se repite.

```bash
python3 traducir_torre.py
```

## Biblioteca española

`insertar_torre_es.py` copia los números traducidos a la base de la
biblioteca española (`biblioteca-ia`), con sus referencias a la
Reina-Valera 1960 para que se puedan pulsar. `sincronizar_torre.sh` lo
repite cada cinco minutos mientras la traducción avanza.

## Créditos

Textos originales de Charles Taze Russell (1879–1916), de dominio público.
Las citas bíblicas en español proceden de la Reina-Valera 1960.
