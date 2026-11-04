# Maná Diario Celestial — datos extraídos

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
{
  "orden": 1,
  "dia": 1, "mes": 1, "mes_nombre": "enero", "clave": "01-01",
  "cita": "texto del versículo",
  "referencia": "Salmo 66:8, 9",
  "referencia_normal": "Salmos 66:8, 9",
  "texto": "párrafo 1\n\npárrafo 2",
  "parrafos": ["párrafo 1", "párrafo 2"],
  "fuente": "Z. '03-3",
  "fuentes": ["Z. '03-3"]
}
```

## Notas

- El libro trae **366** entradas: incluye el 29 de febrero, por lo que sirve para años bisiestos. Las fechas se guardan como mes y día, sin año.
- **2 días no traen fuente impresa** en el PDF: 06-13, 10-17.
- **3 días traen dos citas Z.** (se conservan ambas en `fuentes`): 09-28, 11-02, 11-26.
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
