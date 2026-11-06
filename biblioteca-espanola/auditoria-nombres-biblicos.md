# Auditoría de nombres bíblicos

Fecha: 2026-11-06

Se revisaron las 2.141 páginas de la biblioteca y se corrigieron **2433 ocurrencias** de nombres bíblicos en **440 páginas** de **10 obras**. La lista completa de ubicaciones está en `auditoria-nombres-biblicos.csv`.

Además se normalizaron **140 entradas del índice temático** y **81 contextos asociados** (`temaobras`, `temafoto`, `refctx`). La lista del índice temático está al final de este documento y en `reporte_temas_biblicos.csv`.

## Resumen por libro corregido

| Libro | Correcciones | Páginas | Obras |
| --- | ---: | ---: | ---: |
| Romanos | 446 | 203 | 5 |
| Mateo | 407 | 203 | 3 |
| 1 Corintios | 301 | 129 | 2 |
| 1 Pedro | 218 | 137 | 2 |
| Ezequiel | 139 | 101 | 5 |
| Gálatas | 134 | 97 | 3 |
| 2 Pedro | 94 | 77 | 2 |
| 1 Timoteo | 72 | 49 | 1 |
| Apocalipsis | 63 | 44 | 2 |
| Juan | 59 | 33 | 1 |
| Salmos | 49 | 37 | 4 |
| Job | 42 | 28 | 3 |
| 1 Tesalonicenses | 38 | 23 | 1 |
| Isaías | 29 | 27 | 5 |
| Daniel | 23 | 21 | 4 |
| Colosenses | 21 | 18 | 1 |
| Zacarías | 20 | 17 | 3 |
| Efesios | 19 | 18 | 3 |
| Filipenses | 15 | 15 | 2 |
| Hageo | 15 | 14 | 2 |
| Sofonías | 15 | 13 | 2 |
| 2 Corintios | 14 | 14 | 1 |
| Marcos | 13 | 12 | 1 |
| 1 Samuel | 12 | 11 | 1 |
| Hebreos | 12 | 12 | 1 |
| Santiago | 12 | 10 | 1 |
| Génesis | 11 | 7 | 1 |
| 1 Juan | 10 | 7 | 1 |
| Corintios | 10 | 7 | 1 |
| Éxodo | 10 | 7 | 2 |
| Eclesiastés | 9 | 8 | 2 |
| Tito | 9 | 7 | 2 |
| 2 Tesalonicenses | 8 | 7 | 1 |
| 2 Timoteo | 5 | 5 | 1 |
| Cantares | 5 | 5 | 1 |
| Levítico | 5 | 5 | 2 |
| Lucas | 5 | 4 | 2 |
| Malaquías | 5 | 5 | 2 |
| Rut | 5 | 3 | 1 |
| Deuteronomio | 4 | 4 | 2 |
| 1 Crónicas | 3 | 3 | 1 |
| Jeremías | 3 | 2 | 1 |
| Joel | 3 | 2 | 1 |
| Josué | 3 | 3 | 1 |
| Nahúm | 3 | 3 | 2 |
| Números | 3 | 1 | 1 |
| Proverbios | 3 | 3 | 2 |
| Timoteo | 3 | 3 | 1 |
| Crónicas | 2 | 2 | 1 |
| Esdras | 2 | 1 | 1 |
| Habacuc | 2 | 2 | 1 |
| Pedro | 2 | 2 | 1 |
| 1 Reyes | 1 | 1 | 1 |
| 2 Crónicas | 1 | 1 | 1 |
| Eclesiástico | 1 | 1 | 1 |
| Filemón | 1 | 1 | 1 |
| Lamentaciones | 1 | 1 | 1 |
| Miqueas | 1 | 1 | 1 |
| Nehemías | 1 | 1 | 1 |
| Samuel | 1 | 1 | 1 |
| Tesalonicenses | 1 | 1 | 1 |

## Resumen por obra

| Obra | Correcciones |
| --- | ---: |
| La Torre del Vigía | 2357 |
| Lo que dijo el pastor Russell | 32 |
| El Plan Divino de las Edades | 11 |
| El Tiempo Está a la Mano | 8 |
| Escritos del pastor Russell para Overland Monthly | 7 |
| La Batalla de Armagedón | 5 |
| Foto-Drama de la Creación | 4 |
| La Nueva Creación | 3 |
| Venga Tu Reino | 3 |
| La Expiación entre Dios y el Hombre | 3 |

## Casos especiales documentados

| Original | Corrección | Motivo |
| --- | --- | --- |
| 1 mascota / 2 mascotas | 1 Pedro / 2 Pedro | «Pet.» se tradujo como «mascota»; el número indica la epístola. |
| Galón. | Gálatas | «Gal.» se tradujo como «galón»; solo se corrigió en contexto de cita. |
| Memoria de sólo lectura | Romanos | «Rom.» se interpretó como «read-only memory» (ROM). |
| 1 TIEMPO. | 1 Timoteo | «Tim.» se tradujo como «tiempo». |
| Columna. | Colosenses | «Col.» se tradujo como «columna»; se excluyó el uso literal de «columna». |
| Coronel. | Colosenses | «Col.» se tradujo como «coronel»; se excluyó el rango militar. |
| Trabajo | Job | «Job» se tradujo como «trabajo»; se excluyó el uso común. |
| Bruja. | Hageo | «Hag.» se tradujo como «bruja»; se excluyó el uso literal. |
| Sofo. | Sofonías | «Sof.» se tradujo como «sofo». |
| Teta. | Tito | «Tit.» se tradujo como «teta»; se excluyó el nombre propio. |
| Zaca. | Zacarías | «Zac.» se tradujo como «zaca». |
| Repo. | Apocalipsis | «Rev.» se tradujo como «repo». |
| Micrófono. | Miqueas | «Mic.» se tradujo como «micrófono». |
| NO PUEDO. 2:14 | Cantares 2:14 | «Cant.» se interpretó como «can’t» → «no puedo». |
| SANTA. 5:1 | Santiago 5:1 | «Sant.» se tradujo como «santa». |
| FILE. 2:1–11 | Filipenses 2:1–11 | «Fil.» se tradujo como «file»; el pasaje es Filipenses 2. |
| Eclus. | Eclesiástico | Abreviatura de Eclesiástico (Sirácides). |
| Es. 54:13 | Isaías 54:13 | «Is.» se tradujo como «es». |
| Song / Solomons Song | Cantares | Título inglés del Cantar de los Cantares. |
| General 24:67 | Génesis 24:67 | «Gen.» se tradujo como «general». |
| No. 1:3 | Nahúm 1:3 | «Nah.» se tradujo como «No.». |
| Ej. | Éxodo | «Ex.» se tradujo como «Ej.». |
| PD. | Salmos | «Ps.» se tradujo como «PD.». |
| Zech. | Zacarías | «Zech.» se tradujo como «Zech.»; se excluyó el apellido Zech. |
| José. 26:19-22 | Josué 24:19-22 | El original inglés dice Josh. 26:19-22; el pasaje citado es Josué 24:19-22. |
| José. 10:3 | Josué 10:3 | «Josh.» se tradujo como «José». |
| Dios. 18:10–12 | Deuteronomio 18:10–12 | «Deut.» se tradujo como «Dios». |
| d. 17:6) | d. C. (Apocalipsis 17:6) | El original inglés dice «A.D. 1799 ... (Rev. 17:6)». |
| Filemón 4:7 | Filemón 1:7 | Filemón tiene un solo capítulo. |
| Estera. 13:10–15,35 | Mateo 13:10–15,35 | El pasaje citado es Mateo 13. |
| Justicia. 3:26 | Lamentaciones 3:26 | El pasaje citado es Lamentaciones 3:26. |

## Detalle de ubicaciones

### 1 Corintios (301)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Nueva Creación | Estudio 5 — La organización de la nueva creación | 6 | 123 | Cor. | Corintios | 1 |
| La Nueva Creación | Estudio 6 — Orden y disciplina de la nueva creación | 7 | 145 | Cor. | Corintios | 1 |
| La Nueva Creación | Estudio 9 — El juicio de la nueva creación | 10 | 55 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 96 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1880 | 7 | 12 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1880 | 7 | 64 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1880 | 10 | 85 | Cor. | Corintios | 3 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 3 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 86 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 112 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 19 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 74 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1882 | 33 | 47 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1882 | 34 | 77 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 24 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1883 | 39 | 136 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1883 | 40 | 137 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1883 | 48 | 110 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1884 | 52 | 147 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 65 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 109 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1884 | 60 | 120 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1885 | 69 | 89 | Cor. | Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1886 | 77 | 33 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1887 | 86 | 123 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1888 | 95 | 95 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1890 | 113 | 69 | 1 Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1890 | 117 | 33 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1892 | 140 | 16 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1892 | 141 | 79 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1892 | 142 | 32 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1893 | 151 | 39 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1893 | 152 | 32 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1893 | 152 | 60 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1893 | 154 | 57 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1893 | 154 | 83 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1893 | 154 | 194 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1893 | 156 | 66 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1894 | 163 | 15 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1894 | 163 | 24 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1895 | 179 | 177 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1895 | 182 | 92 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1896 | 189 | 149 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1897 | 198 | 172 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1897 | 200 | 71 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1897 | 202 | 114 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1899 | 220 | 84 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 204 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1901 | 248 | 172 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1902 | 253 | 41 | I Cor. | 1 Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — enero de 1902 | 253 | 82 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 19 | I Cor. | 1 Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 45 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 92 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 185 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 221 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 234 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 160 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 227 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 233 | I Cor. | 1 Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 247 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 255 | I Cor. | 1 Corintios | 3 |
| La Torre del Vigía | La Torre del Vigía — abril de 1902 | 256 | 24 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1902 | 256 | 25 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1902 | 256 | 29 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1902 | 256 | 91 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1902 | 256 | 100 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1902 | 256 | 241 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 74 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 82 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 160 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 237 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 273 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 12 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 76 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 84 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 107 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 181 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 197 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 198 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 247 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1902 | 259 | 20 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1902 | 259 | 62 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1902 | 259 | 194 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 88 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 112 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 225 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 230 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 26 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 57 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 87 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 163 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 164 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 233 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1902 | 262 | 32 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1902 | 262 | 55 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1902 | 262 | 162 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 126 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 187 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1902 | 264 | 14 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1902 | 264 | 45 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1903 | 272 | 92 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1904 | 277 | 165 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1904 | 277 | 169 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1904 | 278 | 113 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1904 | 280 | 71 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1904 | 282 | 45 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1904 | 282 | 46 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1904 | 282 | 76 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1904 | 283 | 48 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1904 | 284 | 31 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1904 | 287 | 86 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1904 | 288 | 136 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1904 | 288 | 223 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1904 | 288 | 243 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1906 | 301 | 57 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1906 | 301 | 251 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1906 | 301 | 279 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1906 | 301 | 285 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1906 | 302 | 124 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1906 | 302 | 132 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1906 | 304 | 9 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1906 | 304 | 61 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1906 | 305 | 29 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1906 | 305 | 145 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1906 | 305 | 186 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 21 | I Cor. | 1 Corintios | 10 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 112 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 131 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 171 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 306 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 337 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 397 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1906 | 308 | 38 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1906 | 308 | 197 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1906 | 309 | 32 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1906 | 311 | 63 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1907 | 313 | 17 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1907 | 313 | 39 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1907 | 313 | 142 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 31 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 55 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 62 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1907 | 317 | 21 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1907 | 317 | 28 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1907 | 317 | 30 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1907 | 318 | 54 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1907 | 320 | 30 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1907 | 321 | 46 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1907 | 321 | 84 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1907 | 321 | 151 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1907 | 321 | 247 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 56 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 90 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 92 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 115 | I Cor. | 1 Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 232 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1907 | 323 | 50 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1907 | 323 | 111 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1907 | 324 | 55 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1907 | 324 | 71 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1908 | 326 | 28 | I COR. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1908 | 326 | 30 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1908 | 328 | 74 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1908 | 328 | 107 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1908 | 328 | 118 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1908 | 329 | 39 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1908 | 329 | 59 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1908 | 330 | 127 | Yo Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1908 | 334 | 33 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1908 | 335 | 41 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1908 | 336 | 58 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1909 | 337 | 84 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1909 | 340 | 38 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1909 | 340 | 83 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1909 | 344 | 37 | YO COR. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1909 | 348 | 59 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1910 | 349 | 106 | I Cor. | 1 Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1910 | 350 | 43 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1910 | 350 | 65 | I Cor. | 1 Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1910 | 351 | 85 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1910 | 351 | 86 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1910 | 352 | 16 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1910 | 352 | 33 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1910 | 353 | 7 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1910 | 354 | 59 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1910 | 354 | 99 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1910 | 354 | 109 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1910 | 356 | 26 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1910 | 356 | 107 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1910 | 357 | 63 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1910 | 357 | 67 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 42 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 49 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 50 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1911 | 363 | 48 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1911 | 363 | 51 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1911 | 364 | 7 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1911 | 364 | 22 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1911 | 364 | 50 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1911 | 364 | 131 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1911 | 365 | 55 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1911 | 365 | 59 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1911 | 365 | 62 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1911 | 365 | 66 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1911 | 365 | 77 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1911 | 366 | 71 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1911 | 366 | 92 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1911 | 366 | 102 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1911 | 366 | 155 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1911 | 369 | 12 | I Cor. | 1 Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1911 | 369 | 42 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1911 | 370 | 42 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1911 | 371 | 22 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1911 | 371 | 53 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1911 | 371 | 73 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1911 | 371 | 123 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1911 | 371 | 127 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1912 | 373 | 23 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1912 | 374 | 44 | I Cor. | 1 Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1912 | 374 | 47 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1912 | 374 | 70 | I Cor. | 1 Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1912 | 374 | 107 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1912 | 374 | 136 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1912 | 375 | 58 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1912 | 375 | 93 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1912 | 376 | 13 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1912 | 377 | 115 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1912 | 378 | 27 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1912 | 379 | 38 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1912 | 379 | 50 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1912 | 379 | 66 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1912 | 379 | 123 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1912 | 379 | 141 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1912 | 379 | 143 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1912 | 380 | 56 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1912 | 380 | 59 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1912 | 380 | 129 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1912 | 381 | 19 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1912 | 381 | 91 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1912 | 381 | 107 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 51 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 62 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 66 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 196 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 223 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 235 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 236 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 21 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 22 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 23 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 31 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 70 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1912 | 384 | 18 | I Cor. | 1 Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1912 | 384 | 80 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1913 | 385 | 23 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1913 | 385 | 48 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1913 | 385 | 60 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1913 | 385 | 64 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1913 | 385 | 75 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1913 | 386 | 12 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1913 | 386 | 23 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1913 | 387 | 13 | I Cor. | 1 Corintios | 2 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1913 | 387 | 20 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1913 | 387 | 26 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1913 | 387 | 27 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1913 | 387 | 35 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1913 | 387 | 94 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1913 | 389 | 117 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1913 | 390 | 57 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1913 | 391 | 7 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1913 | 392 | 14 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1913 | 393 | 68 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1913 | 395 | 19 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1913 | 395 | 73 | I Cor. | 1 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1916 | 430 | 24 | Cor. | Corintios | 1 |

### 1 Crónicas (3)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 206 | Yo Crónica. | 1 Crónicas | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 48 | I Crón. | 1 Crónicas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1908 | 333 | 95 | I Crón. | 1 Crónicas | 1 |

### 1 Juan (10)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — marzo de 1885 | 64 | 73 | 1 Jno. | 1 Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1887 | 91 | 49 | 1 Jno. | 1 Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1887 | 93 | 103 | 1 Jno. | 1 Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 234 | Yo Jno. | 1 Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 23 | Yo Jno. | 1 Juan | 2 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 164 | I Jno. | 1 Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1906 | 302 | 25 | Yo Jno. | 1 Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1906 | 302 | 26 | Yo Jno. | 1 Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1906 | 309 | 31 | Yo Jno. | 1 Juan | 1 |

### 1 Pedro (218)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — julio de 1879 | 1 | 102 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1879 | 1 | 111 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 26 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 30 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 31 | 1 mascota. | 1 Pedro | 3 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 32 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 68 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1879 | 4 | 64 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 29 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 45 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 65 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 25 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 53 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1880 | 7 | 54 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1880 | 8 | 63 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1880 | 8 | 93 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 84 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 33 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 73 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 69 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 27 | 1 mascota. | 1 Pedro | 2 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 93 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 16 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 20 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 29 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 16 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 81 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 6 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 71 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1881 | 24 | 66 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1882 | 31 | 53 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1882 | 34 | 16 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1882 | 34 | 35 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1882 | 36 | 115 | 1 mascota. | 1 Pedro | 2 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 28 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 62 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 125 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 32 | 1 mascota. | 1 Pedro | 5 |
| La Torre del Vigía | La Torre del Vigía — enero de 1883 | 39 | 115 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1884 | 54 | 44 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1884 | 57 | 85 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 47 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 54 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 68 | 1 mascota. | 1 Pedro | 4 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1884 | 59 | 94 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1884 | 59 | 139 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1885 | 62 | 169 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 46 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1885 | 64 | 71 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1885 | 64 | 107 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1885 | 65 | 53 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1885 | 65 | 56 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1885 | 65 | 100 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1885 | 67 | 44 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 38 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 51 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 148 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1885 | 69 | 64 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1885 | 72 | 78 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1886 | 73 | 8 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1886 | 80 | 111 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1886 | 80 | 113 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1887 | 83 | 89 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1887 | 87 | 109 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1887 | 89 | 125 | 1 Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1888 | 95 | 43 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1888 | 95 | 58 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1888 | 100 | 25 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1888 | 100 | 41 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1888 | 104 | 111 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1890 | 117 | 61 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1890 | 118 | 45 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1890 | 119 | 66 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1890 | 119 | 76 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1890 | 124 | 106 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 17 | 1 MASCOTA. 18,19 | 1 Pedro 1:18,19 | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1891 | 126 | 60 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1891 | 127 | 114 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1891 | 127 | 117 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1891 | 131 | 58 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1892 | 136 | 76 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1892 | 143 | 34 | 1 Mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1892 | 145 | 167 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1893 | 151 | 53 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1893 | 152 | 22 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1893 | 152 | 174 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1893 | 153 | 38 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1893 | 154 | 113 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1893 | 157 | 3 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1893 | 157 | 138 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1893 | 159 | 82 | 1 MASCOTA. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1894 | 161 | 0 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1894 | 161 | 173 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1894 | 168 | 28 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1895 | 174 | 107 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 169 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1895 | 180 | 20 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 159 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1895 | 182 | 113 | 1 Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1895 | 182 | 154 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1895 | 182 | 163 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1896 | 185 | 0 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1896 | 185 | 54 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1896 | 187 | 67 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1896 | 188 | 13 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1896 | 189 | 59 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1896 | 189 | 197 | 1 Pe. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1896 | 190 | 140 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1896 | 193 | 127 | 1 mascota. | 1 Pedro | 2 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1897 | 197 | 143 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1897 | 197 | 156 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1897 | 198 | 165 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1897 | 198 | 200 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1897 | 198 | 204 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1897 | 200 | 246 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1897 | 201 | 38 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1898 | 214 | 176 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1898 | 216 | 91 | 1 mascota. | 1 Pedro | 2 |
| La Torre del Vigía | La Torre del Vigía — enero de 1899 | 220 | 14 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1899 | 220 | 19 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1899 | 220 | 210 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1899 | 220 | 212 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1899 | 221 | 63 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 50 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 101 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 105 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 142 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 169 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1899 | 224 | 62 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1899 | 226 | 39 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1899 | 228 | 99 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1900 | 229 | 72 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1900 | 237 | 34 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1900 | 240 | 79 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 348 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1901 | 243 | 96 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1901 | 244 | 67 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1901 | 244 | 94 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1901 | 247 | 86 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1901 | 248 | 45 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1901 | 250 | 15 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1901 | 252 | 232 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 160 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 233 | I Ped. | 1 Pedro | 5 |
| La Torre del Vigía | La Torre del Vigía — abril de 1902 | 256 | 50 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 26 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 228 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 100 | I Pet. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 126 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 158 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1903 | 265 | 69 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1903 | 266 | 67 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1903 | 267 | 171 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1903 | 269 | 134 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1903 | 270 | 14 | 1 Mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1903 | 271 | 35 | 1 Mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1903 | 273 | 174 | 1 MASCOTA. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1904 | 280 | 124 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1905 | 291 | 22 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1905 | 292 | 95 | 1 mascota. | 1 Pedro | 3 |
| La Torre del Vigía | La Torre del Vigía — julio de 1905 | 295 | 24 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1905 | 295 | 27 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1905 | 296 | 38 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1905 | 297 | 113 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1905 | 299 | 54 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1906 | 305 | 184 | I Ped. | 1 Pedro | 2 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1906 | 305 | 197 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1906 | 306 | 27 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1906 | 308 | 0 | 1 mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1907 | 313 | 8 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1907 | 313 | 39 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 53 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 55 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 63 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1907 | 323 | 36 | Yo mascota. | 1 Pedro | 2 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1907 | 324 | 70 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1908 | 325 | 122 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1908 | 328 | 122 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1908 | 332 | 11 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1909 | 340 | 38 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1909 | 348 | 5 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1909 | 348 | 119 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1910 | 350 | 18 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1910 | 351 | 53 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1910 | 352 | 61 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1910 | 354 | 108 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1910 | 355 | 101 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 20 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 40 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 129 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1911 | 363 | 143 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1912 | 376 | 88 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1912 | 379 | 73 | I Ped. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 26 | Yo mascota. | 1 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1913 | 392 | 48 | I Ped. | 1 Pedro | 1 |
| Lo que dijo el pastor Russell | IRRESPONSABLES — ¿Qué será de ellos? | 788 | 2 | Ped. | Pedro | 1 |
| Lo que dijo el pastor Russell | NATURALEZA — La naturaleza de Cristo | 808 | 0 | 1 mascota. | 1 Pedro | 1 |

### 1 Reyes (1)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — febrero de 1886 | 74 | 58 | 1 Kings  | 1 Reyes  | 1 |

### 1 Samuel (12)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 6 | Sam. | Samuel | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1885 | 66 | 76 | Sam. | Samuel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1896 | 193 | 23 | Sam. | Samuel | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1902 | 259 | 175 | I Sam. | 1 Samuel | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 206 | Yo Sam. | 1 Samuel | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 66 | Sam. | Samuel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1903 | 274 | 56 | Sam. | Samuel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1906 | 301 | 273 | I Sam. | 1 Samuel | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 48 | Yo Sam. | 1 Samuel | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1908 | 331 | 36 | YO SAM. | 1 Samuel | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1908 | 331 | 66 | YO SAM. | 1 Samuel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1912 | 384 | 36 | I Sam. | 1 Samuel | 1 |

### 1 Tesalonicenses (38)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 59 | Tes. | Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1899 | 220 | 11 | Tes. | Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 19 | Yo Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 145 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 155 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 227 | I Tes. | 1 Tesalonicenses | 4 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 236 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 265 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 273 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 198 | I Tes. | 1 Tesalonicenses | 2 |
| La Torre del Vigía | La Torre del Vigía — julio de 1902 | 259 | 33 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 95 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 228 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 126 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1902 | 264 | 162 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1902 | 264 | 211 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1904 | 286 | 12 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1904 | 286 | 33 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1904 | 286 | 40 | Yo Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1906 | 304 | 286 | Tes. | Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1906 | 306 | 45 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 111 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 328 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1908 | 328 | 44 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1908 | 330 | 118 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1909 | 348 | 119 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1911 | 363 | 10 | 1 TESS. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1911 | 364 | 50 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1912 | 376 | 78 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 26 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 50 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 104 | YO TESSA. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 113 | I Tes. | 1 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1913 | 390 | 57 | I Tes. | 1 Tesalonicenses | 1 |

### 1 Timoteo (72)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1881 | 26 | 248 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 130 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1884 | 60 | 83 | 1 TIEMPO. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1886 | 78 | 109 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1886 | 79 | 41 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1887 | 88 | 16 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1888 | 97 | 75 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1890 | 124 | 109 | 1 Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 17 | 1 TIEMPO. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1891 | 130 | 95 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1893 | 156 | 10 | 1 TIEMPO. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 131 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 193 | 1 Timoteo justifica su uso limitado con fines medicinales. 5:23. | 1 Timoteo 5:23 justifica su uso limitado con fines medicinales. | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 193 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 121 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 19 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 92 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 231 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 283 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1902 | 256 | 198 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 21 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 214 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 26 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 118 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 170 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 177 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 227 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 164 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1902 | 262 | 32 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 10 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 54 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 126 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1902 | 264 | 45 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1902 | 264 | 157 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1902 | 264 | 238 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1904 | 288 | 239 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1906 | 301 | 32 | YO TIM. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1906 | 302 | 26 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1906 | 305 | 148 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1906 | 305 | 154 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 371 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1906 | 308 | 22 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1907 | 314 | 128 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1907 | 318 | 56 | Yo Tim. | 1 Timoteo | 3 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 45 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 65 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 67 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1907 | 320 | 17 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1907 | 320 | 30 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1907 | 321 | 98 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 102 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 115 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1907 | 323 | 26 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1908 | 328 | 29 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1908 | 329 | 34 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1909 | 339 | 38 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1909 | 340 | 47 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1910 | 352 | 65 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1910 | 354 | 115 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1911 | 363 | 146 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1911 | 368 | 85 | I Tim. | 1 Timoteo | 2 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1911 | 368 | 130 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1912 | 381 | 41 | Yo Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 172 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 258 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 11 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 29 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1912 | 384 | 22 | I Tim. | 1 Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1913 | 393 | 16 | I Tim. | 1 Timoteo | 1 |

### 2 Corintios (14)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 84 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1880 | 7 | 52 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1882 | 34 | 38 | 2 Cor. | 2 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1887 | 92 | 32 | 2 Cor. | 2 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1888 | 97 | 27 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1891 | 132 | 56 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1893 | 155 | 128 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1896 | 189 | 197 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1897 | 196 | 46 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1897 | 199 | 156 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1898 | 218 | 188 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1908 | 330 | 110 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1909 | 348 | 83 | II COR. | 2 Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1911 | 371 | 71 | Cor. | Corintios | 1 |

### 2 Crónicas (1)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — octubre de 1911 | 370 | 20 | II Crón. | 2 Crónicas | 1 |

### 2 Pedro (94)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — agosto de 1879 | 2 | 76 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1879 | 2 | 99 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 78 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 51 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 59 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1880 | 8 | 72 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1880 | 10 | 52 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1880 | 10 | 53 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 43 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 68 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 56 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 72 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 41 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 78 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 41 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 16 | 2 mascota. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 33 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 76 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 87 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 6 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 20 | 2 mascotas.  | 2 Pedro  | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 61 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 61 | 2 mascotas.  | 2 Pedro  | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1881 | 23 | 59 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1882 | 31 | 68 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1882 | 35 | 66 | 2 Ped. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1882 | 35 | 113 | 2 Ped. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1883 | 44 | 76 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1885 | 69 | 45 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1886 | 80 | 85 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1888 | 104 | 105 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1889 | 108 | 50 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1890 | 119 | 76 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1890 | 123 | 91 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 17 | 2 MASCOTAS. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1891 | 126 | 10 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1891 | 134 | 86 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1892 | 144 | 40 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1893 | 148 | 100 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1893 | 148 | 266 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 138 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1893 | 151 | 33 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1893 | 152 | 145 | 2 MASCOTAS. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1893 | 157 | 138 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1894 | 160 | 129 | 2 mascota. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1894 | 161 | 173 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 155 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 149 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1894 | 168 | 40 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1894 | 169 | 144 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1894 | 171 | 152 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1895 | 176 | 69 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1895 | 176 | 146 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1895 | 182 | 116 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1895 | 183 | 44 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1896 | 188 | 175 | 2 mascota. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1896 | 191 | 12 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1897 | 197 | 156 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1897 | 198 | 165 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1897 | 200 | 246 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1897 | 201 | 156 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1897 | 204 | 38 | 2 mascota. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1898 | 216 | 137 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 81 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 218 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 50 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1899 | 228 | 60 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1900 | 234 | 104 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1900 | 237 | 85 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 172 | 2 mascota. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1901 | 247 | 86 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 278 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1902 | 256 | 106 | 2 mascota. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 211 | II Ped. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1903 | 266 | 29 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1903 | 267 | 127 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1905 | 293 | 48 | 2 mascotas. | 2 Pedro | 2 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1905 | 293 | 50 | 2 mascotas. | 2 Pedro | 2 |
| La Torre del Vigía | La Torre del Vigía — julio de 1905 | 295 | 24 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1906 | 303 | 283 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1907 | 316 | 39 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 38 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1907 | 321 | 32 | Ped. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1908 | 331 | 45 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1909 | 338 | 70 | 2 mascota. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1909 | 346 | 15 | 2 mascota. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 50 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1911 | 362 | 53 | 2 mascota. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1911 | 371 | 24 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1912 | 374 | 29 | 2 mascotas. | 2 Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1912 | 382 | 190 | 2 mascotas. | 2 Pedro | 1 |
| Lo que dijo el pastor Russell | FUEGO — ¿Será destruida la Tierra por fuego literal? | 777 | 3 | Ped. | Pedro | 1 |

### 2 Tesalonicenses (8)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 3 | Tes. | Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1884 | 54 | 109 | Tes. | Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1885 | 69 | 52 | Tes. | Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1890 | 114 | 75 | Tes. | Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1894 | 163 | 106 | Tes. | Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1896 | 188 | 110 | Tes. | Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1902 | 259 | 6 | II Tes. | 2 Tesalonicenses | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1902 | 259 | 36 | Tes. | Tesalonicenses | 1 |

### 2 Timoteo (5)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1894 | 168 | 173 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1898 | 208 | 14 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1900 | 240 | 96 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1901 | 244 | 13 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1912 | 381 | 105 | Tim. | Timoteo | 1 |

### Apocalipsis (63)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Batalla de Armagedón | Estudio 12 — La gran profecía de nuestro Señor | 13 | 69 | d. 17:6) | d. C. (Apocalipsis 17:6) | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1880 | 14 | 110 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 22 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 19 | Rdo.  | Apocalipsis  | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 64 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 76 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 80 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 89 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 90 | Rdo. | Apocalipsis | 2 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 29 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 84 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 90 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1881 | 27 | 0 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 82 | RDO. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 82 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 85 | RDO. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 97 | RDO. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 102 | RDO. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 109 | RDO. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1882 | 31 | 15 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 51 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 52 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 55 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 9 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1886 | 82 | 100 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1887 | 90 | 126 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1888 | 94 | 64 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1888 | 104 | 117 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1890 | 118 | 54 | Repo.  | Apocalipsis  | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1890 | 123 | 117 | Repo.  | Apocalipsis  | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 0 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 17 | RDO. | Apocalipsis | 3 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1892 | 140 | 39 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1892 | 142 | 171 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1892 | 145 | 50 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1893 | 148 | 60 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 122 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 155 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1895 | 176 | 31 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1896 | 193 | 39 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1897 | 201 | 4 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1898 | 209 | 20 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1898 | 217 | 169 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 140 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1899 | 228 | 212 | Repo.  | Apocalipsis  | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1900 | 230 | 43 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1900 | 240 | 63 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 270 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 294 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 304 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1901 | 248 | 206 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 139 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1903 | 265 | 0 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1903 | 267 | 43 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1905 | 300 | 292 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 139 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1908 | 335 | 113 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1910 | 350 | 77 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1913 | 386 | 117 | Rdo. | Apocalipsis | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1914 | 401 | 13 | Revelación  | Apocalipsis  | 1 |

### Cantares (5)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 66 | Canción de Sol. | Cantares | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1883 | 45 | 91 | Solomons Song  | Cantares  | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1888 | 94 | 58 | Canción de Sol. | Cantares | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1906 | 304 | 184 | NO PUEDO.  | Cantares  | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1910 | 350 | 141 | Cnt. | Cantares | 1 |

### Colosenses (21)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — julio de 1879 | 1 | 82 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1879 | 2 | 73 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 19 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 67 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1882 | 31 | 0 | Coronel. | Colosenses | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 36 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1884 | 54 | 44 | Coronel.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1884 | 57 | 0 | Col. | Colosenses | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1884 | 57 | 80 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1887 | 90 | 97 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1887 | 93 | 93 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1888 | 101 | 109 | en el año 93 d. 2:8; 1 Timoteo 6:20. | en el año 93 d. C. —Colosenses 2:8; 1 Timoteo 6:20. | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1891 | 135 | 4 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1893 | 153 | 0 | Columna. | Colosenses | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1894 | 166 | 178 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1898 | 210 | 26 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1899 | 224 | 0 | Coronel. | Colosenses | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 322 | en el año 93 d. 2:8; 1 Timoteo 6:20. | en el año 93 d. C. —Colosenses 2:8; 1 Timoteo 6:20. | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1910 | 349 | 65 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1910 | 349 | 107 | Columna.  | Colosenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1914 | 397 | 150 | Columna.  | Colosenses  | 1 |

### Corintios (10)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — octubre de 1881 | 27 | 108 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 65 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1891 | 127 | 105 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1900 | 236 | 108 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 234 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1909 | 343 | 60 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1909 | 343 | 75 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1909 | 343 | 81 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1909 | 343 | 83 | Cor. | Corintios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1912 | 377 | 5 | Cor. | Corintios | 1 |

### Crónicas (2)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — octubre de 1881 | 27 | 50 | Crón. | Crónicas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1903 | 274 | 71 | Crón. | Crónicas | 1 |

### Daniel (23)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| El Plan Divino de las Edades | Estudio 22 — El día de Jehová — Parte 1/2 | 23 | 3 | Dan. | Daniel | 1 |
| El Tiempo Está a la Mano | Estudio 3 — El cumplimiento de la profecía del tiempo en el primer advenimiento de Cristo | 4 | 2 | Dan. | Daniel | 1 |
| El Tiempo Está a la Mano | Estudio 7 — La manera del regreso y aparición de nuestro Señor — Parte 3/4 | 8 | 15 | Dan. | Daniel | 1 |
| El Tiempo Está a la Mano | Estudio 8 — La manera del regreso y aparición de nuestro Señor — Parte 4/4 | 9 | 13 | Dan. | Daniel | 1 |
| Venga Tu Reino | Estudio 5 — El tiempo de la cosecha | 6 | 16 | Dan. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 0 | Dan? 12? | Daniel 12? | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 30 | Danl. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1881 | 28 | 0 | Dan? 12? | Daniel 12? | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1882 | 29 | 59 | Dn. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1882 | 29 | 91 | Danl. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1882 | 29 | 134 | Danl. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 63 | Danl. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1885 | 62 | 64 | Danl. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1885 | 66 | 5 | Danl. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1885 | 71 | 46 | Dan. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1887 | 87 | 0 | Dan? 7:13,14? | Daniel 7:13,14? | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1890 | 113 | 108 | Dn. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1890 | 115 | 110 | Dn. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1890 | 122 | 3 | Dn. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1893 | 159 | 86 | Dn. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1894 | 166 | 86 | Dan. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1898 | 213 | 34 | Dan. | Daniel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1898 | 217 | 203 | Dan. | Daniel | 1 |

### Deuteronomio (4)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| El Plan Divino de las Edades | Estudio 3 — La Biblia como revelación divina — Parte 1/2 | 4 | 40 | Deut. | Deuteronomio | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1885 | 66 | 64 | Dios. 18:10–12 | Deuteronomio 18:10–12 | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1893 | 157 | 116 | Deut. | Deuteronomio | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 75 | Deut. | Deuteronomio | 1 |

### Eclesiastés (9)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — abril de 1883 | 42 | 31 | Eccles. | Eclesiastés | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1885 | 62 | 120 | Ecl. | Eclesiastés | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1885 | 71 | 93 | Eccles. | Eclesiastés | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1886 | 74 | 58 | Eccl. | Eclesiastés | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1886 | 79 | 43 | Eccles. | Eclesiastés | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1893 | 152 | 164 | ECCL. | Eclesiastés | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1893 | 152 | 177 | ECCL. | Eclesiastés | 1 |
| Lo que dijo el pastor Russell | MUERTO — Apocalipsis 14:13: ¿Cómo pueden los muertos seguir obrando? | 760 | 1 | Ecc. | Eclesiastés | 1 |
| Lo que dijo el pastor Russell | MUERTE — Sobre el árbol que cae | 767 | 1 | Ecc. | Eclesiastés | 1 |

### Eclesiástico (1)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 40 | Eclus.  | Eclesiástico  | 1 |

### Efesios (19)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| Foto-Drama de la Creación | ABEL, EL PRIMER MÁRTIR | 16 | 4 | Efesos | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1880 | 7 | 63 | Ef. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 87 | Ef. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1883 | 45 | 57 | EPH. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1884 | 59 | 97 | EPH. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 17 | EPH. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 122 | Ef. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1892 | 141 | 87 | Efe. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1893 | 157 | 60 | Efe. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1893 | 158 | 180 | EPH. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1894 | 166 | 176 | Efe. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 140 | Efe. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1897 | 203 | 66 | Efe. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1899 | 223 | 22 | Efe. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1900 | 231 | 84 | Efe. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 49 | EPH. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1903 | 267 | 141 | EPH. | Efesios | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1904 | 288 | 227 | EPH. | Efesios | 1 |
| Lo que dijo el pastor Russell | HOMBRE — Su relación con Dios y con la mujer | 803 | 2 | Efe. | Efesios | 1 |

### Esdras (2)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — octubre de 1905 | 298 | 115 | ESDRA | Esdras | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1905 | 298 | 228 | ESDRA | Esdras | 1 |

### Ezequiel (139)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| El Plan Divino de las Edades | Estudio 22 — El día de Jehová — Parte 1/2 | 23 | 9 | Ezeq. | Ezequiel | 1 |
| El Plan Divino de las Edades | Estudio 23 — El día de Jehová — Parte 2/2 | 24 | 25 | Ezeq. | Ezequiel | 1 |
| La Batalla de Armagedón | Estudio 7 — Las naciones reunidas y la preparación de los elementos para el gran fuego de la indignación de Dios | 8 | 201 | Ezeq. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1879 | 1 | 64 | Ezek. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 86 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 41 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 43 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 44 | Ezek. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 46 | Ezeq. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 78 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1880 | 14 | 102 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1881 | 26 | 141 | Ezek. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1881 | 26 | 396 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1881 | 26 | 464 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1882 | 32 | 65 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1882 | 33 | 47 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1882 | 33 | 59 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1883 | 42 | 32 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1883 | 43 | 24 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1883 | 44 | 69 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1883 | 48 | 144 | Ezek. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1884 | 61 | 147 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 41 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1885 | 64 | 82 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1885 | 65 | 135 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1885 | 66 | 111 | Ezk. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 62 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1886 | 73 | 103 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1886 | 76 | 11 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1887 | 83 | 68 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1887 | 84 | 65 | Ezek. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1887 | 84 | 90 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1887 | 85 | 115 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1888 | 94 | 53 | Eze. | Ezequiel | 2 |
| La Torre del Vigía | La Torre del Vigía — abril de 1888 | 97 | 73 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1889 | 105 | 80 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1890 | 119 | 151 | Ezek. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1890 | 120 | 44 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1890 | 122 | 21 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1890 | 122 | 65 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1890 | 124 | 70 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1890 | 124 | 70 | Ezek. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1890 | 124 | 111 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1891 | 126 | 48 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1891 | 128 | 30 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1891 | 135 | 27 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1892 | 137 | 202 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1892 | 137 | 210 | EZEK. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1892 | 137 | 211 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1892 | 137 | 219 | Ezec. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1892 | 138 | 55 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1892 | 142 | 30 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1892 | 144 | 170 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1892 | 144 | 173 | Ezek. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1892 | 147 | 137 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 41 | Eze. | Ezequiel | 3 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 142 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 197 | Ezek. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1894 | 160 | 135 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1894 | 161 | 87 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1894 | 161 | 114 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1894 | 163 | 184 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 48 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1894 | 168 | 51 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1894 | 169 | 123 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1894 | 170 | 54 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1894 | 170 | 142 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1894 | 171 | 170 | Eze. | Ezequiel | 2 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1895 | 173 | 139 | Eze. | Ezequiel | 2 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1895 | 174 | 45 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1895 | 174 | 86 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 71 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1895 | 178 | 35 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1895 | 179 | 33 | Ezek. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1895 | 180 | 188 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 132 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1896 | 191 | 72 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1896 | 193 | 89 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1897 | 198 | 70 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1897 | 201 | 179 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1898 | 211 | 62 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1898 | 217 | 27 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1898 | 218 | 119 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 81 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 115 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1899 | 226 | 7 | EZEC. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1899 | 226 | 37 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1900 | 234 | 11 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 188 | Eze. | Ezequiel | 3 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 293 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 296 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 344 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 346 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1901 | 251 | 93 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 199 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 175 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1902 | 262 | 36 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1903 | 265 | 121 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1903 | 265 | 183 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1903 | 268 | 84 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1903 | 275 | 123 | Ezek. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1904 | 287 | 62 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1905 | 296 | 263 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1905 | 297 | 93 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1905 | 297 | 219 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 274 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1909 | 340 | 151 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1909 | 340 | 152 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1910 | 351 | 48 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1910 | 352 | 65 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1912 | 374 | 132 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1912 | 374 | 133 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1912 | 379 | 88 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1912 | 384 | 22 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1913 | 392 | 21 | Eze. | Ezequiel | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1914 | 397 | 29 | Eze. | Ezequiel | 1 |
| Escritos del pastor Russell para Overland Monthly | El pueblo escogido de Dios — Los «siete tiempos» de castigo: 2520 años | 79 | 10 | Eze. | Ezequiel | 2 |
| Escritos del pastor Russell para Overland Monthly | El regreso de nuestro Señor | 224 | 20 | Eze. | Ezequiel | 1 |
| Lo que dijo el pastor Russell | GRACIA — Una vez en gracia, siempre en gracia | 288 | 1 | Eze. | Ezequiel | 1 |
| Lo que dijo el pastor Russell | SATANÁS — La atadura de Satanás y la muerte | 622 | 4 | Eze. | Ezequiel | 1 |
| Lo que dijo el pastor Russell | CREACIÓN — ¿Cuánto duraron los días de la creación? | 758 | 4 | Eze. | Ezequiel | 1 |
| Lo que dijo el pastor Russell | JUDÍOS — El regreso a Palestina | 792 | 2 | Eze. | Ezequiel | 2 |
| Lo que dijo el pastor Russell | JOB — ¿Real o alegórico? | 793 | 2 | Eze. | Ezequiel | 1 |
| Lo que dijo el pastor Russell | RESURRECCIÓN — ¿Qué es el cuerpo celestial? | 820 | 3 | Eze. | Ezequiel | 1 |
| Lo que dijo el pastor Russell | SATANÁS — ¿Creó Dios a Satanás? | 826 | 2 | Eze. | Ezequiel | 1 |
| Lo que dijo el pastor Russell | ALMA — ¿Puede morir? | 834 | 1 | Eze. | Ezequiel | 1 |
| Lo que dijo el pastor Russell | ALMA — ¿Qué le sucede al morir? | 837 | 3 | Eze. | Ezequiel | 1 |
| Lo que dijo el pastor Russell | ESPÍRITU — «Volverá a Dios que lo dio» | 838 | 3 | Eze. | Ezequiel | 1 |
| Lo que dijo el pastor Russell | LADRÓN EN LA CRUZ — Diferencia entre el Paraíso y el cielo | 845 | 2 | Eze. | Ezequiel | 1 |
| Lo que dijo el pastor Russell | TIEMPO — ¿Cuánto duraba un tiempo? | 846 | 2 | Eze. | Ezequiel | 1 |

### Filemón (1)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1910 | 360 | 138 | Filemón 4:7 | Filemón 1:7 | 1 |

### Filipenses (15)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — julio de 1881 | 25 | 114 | Phil. | Filipenses | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1881 | 26 | 403 | Filip. | Filipenses | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1882 | 29 | 61 | Phil. | Filipenses | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1882 | 33 | 101 | Phil. | Filipenses | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1885 | 71 | 96 | Phil. | Filipenses | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1887 | 86 | 75 | Fil. | Filipenses | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1891 | 128 | 62 | Phil. | Filipenses | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 296 | Phil. | Filipenses | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1894 | 171 | 39 | PHIL. | Filipenses | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1897 | 207 | 53 | FILE.  | Filipenses  | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1901 | 246 | 186 | Fil. | Filipenses | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 78 | PHIL. | Filipenses | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1903 | 270 | 116 | Phil. | Filipenses | 1 |
| Lo que dijo el pastor Russell | JESÚS — Nuestro Señor, la imagen expresa del Padre | 367 | 2 | Fil. | Filipenses | 1 |
| Lo que dijo el pastor Russell | VOTACIÓN — Las elecciones seculares | 850 | 0 | (Fil?  3:13,14) | (Filipenses 3:13,14) | 1 |

### Gálatas (134)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| Venga Tu Reino | Estudio 10 — El testimonio del testigo de piedra y profeta de Dios: la gran pirámide de Egipto | 11 | 136 | Gál. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1879 | 1 | 43 | Galón.  | Gálatas  | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1879 | 2 | 114 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1879 | 2 | 115 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 38 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 54 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 62 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1880 | 8 | 7 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 28 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 30 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 74 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 88 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1880 | 10 | 52 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 43 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 49 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 53 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 18 | Galón. | Gálatas | 2 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 68 | Galón.  | Gálatas  | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 99 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 22 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1880 | 17 | 93 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 51 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 54 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 74 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1881 | 23 | 5 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1881 | 27 | 56 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 32 | Galón. | Gálatas | 2 |
| La Torre del Vigía | La Torre del Vigía — julio de 1882 | 34 | 57 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 30 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 32 | Galón. | Gálatas | 5 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1883 | 40 | 26 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 68 | Galón. | Gálatas | 5 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1884 | 60 | 64 | Gál. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1885 | 66 | 24 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 70 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1885 | 69 | 45 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1885 | 69 | 46 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1886 | 74 | 47 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1887 | 83 | 89 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1887 | 86 | 144 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1887 | 89 | 99 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1887 | 90 | 79 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1887 | 92 | 51 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1889 | 105 | 42 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1889 | 108 | 101 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1889 | 112 | 26 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1889 | 112 | 59 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1890 | 118 | 10 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1890 | 119 | 76 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1890 | 122 | 122 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 17 | GALÓN. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1891 | 131 | 62 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1891 | 135 | 24 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1892 | 141 | 63 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1892 | 144 | 81 | GALÓN. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1892 | 145 | 92 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1892 | 145 | 122 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1892 | 146 | 32 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1893 | 148 | 158 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 110 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1893 | 152 | 34 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1893 | 152 | 71 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1893 | 153 | 184 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1893 | 156 | 11 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1893 | 156 | 65 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1894 | 162 | 136 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1894 | 163 | 149 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1894 | 164 | 87 | Gál. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 80 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1894 | 166 | 74 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 151 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1894 | 168 | 10 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1894 | 169 | 39 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1894 | 169 | 144 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1894 | 170 | 78 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1894 | 171 | 21 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1895 | 174 | 21 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 61 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1895 | 180 | 81 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1895 | 180 | 83 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 116 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 158 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1895 | 183 | 178 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1896 | 187 | 47 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1896 | 195 | 52 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1897 | 197 | 156 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1897 | 198 | 157 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1897 | 200 | 63 | Gál. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1897 | 200 | 64 | Gál. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1897 | 201 | 162 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1898 | 214 | 121 | Gál. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 235 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1899 | 220 | 51 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1899 | 220 | 54 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1899 | 221 | 208 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1900 | 232 | 110 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 87 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 256 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1901 | 248 | 90 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1901 | 251 | 154 | Gál. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 49 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 159 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1903 | 272 | 47 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1905 | 291 | 23 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1905 | 295 | 190 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 362 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 34 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1907 | 316 | 37 | Galón. | Gálatas | 2 |
| La Torre del Vigía | La Torre del Vigía — junio de 1907 | 318 | 52 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 45 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1907 | 320 | 30 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 92 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 115 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 117 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1909 | 348 | 122 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1911 | 365 | 1 | Gál. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1912 | 376 | 41 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 11 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 27 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 80 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1913 | 390 | 32 | Galón. | Gálatas | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1913 | 395 | 11 | Galón. | Gálatas | 1 |
| Escritos del pastor Russell para Overland Monthly | La destrucción de los credos, necesaria para la federación — Congregacionales, presbiterianos y metodistas | 234 | 25 | Gál. | Gálatas | 1 |

### Génesis (11)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1880 | 17 | 96 | Gén. | Génesis | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1893 | 155 | 151 | Gn. | Génesis | 2 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1893 | 155 | 151 | Gn. | Génesis | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1894 | 162 | 194 | Gén. | Génesis | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1894 | 164 | 77 | Gén. | Génesis | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1896 | 188 | 145 | Gn. | Génesis | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1905 | 297 | 80 | Gn. | Génesis | 2 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1905 | 297 | 80 | Gn. | Génesis | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1912 | 379 | 123 | Gén. | Génesis | 1 |

### Habacuc (2)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1892 | 144 | 87 | HABAKKUK | Habacuc | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1904 | 280 | 46 | Hab. | Habacuc | 1 |

### Hageo (15)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| Foto-Drama de la Creación | LA TIERRA RESTAURADA, PERFECTA | 98 | 4 | Aggeo | Hageo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 5 | Bruja.  | Hageo  | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 90 | Bruja.  | Hageo  | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 68 | Bruja.  | Hageo  | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 106 | Bruja.  | Hageo  | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1883 | 49 | 0 | Bruja. | Hageo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1889 | 105 | 33 | Bruja.  | Hageo  | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 0 | Bruja. | Hageo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1893 | 155 | 0 | Bruja. | Hageo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1896 | 193 | 0 | Bruja. | Hageo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1904 | 278 | 0 | Bruja. | Hageo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1906 | 308 | 0 | Bruja. | Hageo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1907 | 318 | 52 | Bruja.  | Hageo  | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1909 | 341 | 72 | Ag. | Hageo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1914 | 405 | 11 | Ag. | Hageo | 1 |

### Hebreos (12)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 0 | Heb. Creemos que 9:29 | Creemos que Hebreos 9:29 | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 0 | Heb. | Hebreos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1886 | 74 | 0 | Heb. | Hebreos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1887 | 92 | 0 | Heb. | Hebreos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1892 | 139 | 0 | Heb. | Hebreos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1894 | 161 | 0 | Heb. | Hebreos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1894 | 163 | 0 | en Heb. El 11 de enero | en Hebreos 11. El 11 de enero | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1895 | 177 | 0 | Heb. | Hebreos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 0 | Heb. | Hebreos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1897 | 197 | 0 | Heb. | Hebreos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 0 | Heb. | Hebreos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1904 | 282 | 0 | Heb. | Hebreos | 1 |

### Isaías (29)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| El Plan Divino de las Edades | Estudio 21 — El reino de Dios — Parte 2/2 | 22 | 22 | Isa. | Isaías | 1 |
| El Tiempo Está a la Mano | Estudio 1 — Tiempos y sazones especiales divinamente señalados | 2 | 48 | Isa. | Isaías | 1 |
| La Batalla de Armagedón | Estudio 7 — Las naciones reunidas y la preparación de los elementos para el gran fuego de la indignación de Dios | 8 | 365 | Isa. | Isaías | 1 |
| La Batalla de Armagedón | Estudio 11 — La batalla del Armagedón | 12 | 47 | Isa. | Isaías | 1 |
| Foto-Drama de la Creación | MELQUISEDEC, SACERDOTE Y REY | 28 | 8 | ISAIAS | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 86 | Es.  | Isaías  | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 46 | Is. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 39 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 0 | En Isa se encuentra | En Isaías se encuentra | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1886 | 76 | 89 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1887 | 89 | 116 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1889 | 105 | 65 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1890 | 122 | 62 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1892 | 144 | 24 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1893 | 156 | 33 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1895 | 180 | 146 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1896 | 194 | 82 | Isa indica | Isaías indica | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1897 | 200 | 48 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1897 | 201 | 162 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 233 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1899 | 223 | 51 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1901 | 244 | 0 | de Isa? 5:8 | de Isaías 5:8 | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1901 | 246 | 199 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 63 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1903 | 268 | 82 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1903 | 268 | 98 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1903 | 268 | 98 | Pregunta.—¿A qué o quién dice Isaías ¿Se refiere 42:19–21? | Pregunta.—¿A qué o a quién se refiere Isaías 42:19–21? | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1904 | 278 | 20 | Isa. | Isaías | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1910 | 357 | 63 | Isa. | Isaías | 1 |

### Jeremías (3)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 58 | Jer. | Jeremías | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 40 | Jer. | Jeremías | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 46 | Jer. | Jeremías | 1 |

### Job (42)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Expiación entre Dios y el Hombre | Estudio 12 — El objeto de la expiación: el hombre | 13 | 305 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 62 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 5 | Trabajo  | Job  | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1881 | 20 | 0 | Trabajo | Job | 2 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1881 | 20 | 106 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 108 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1883 | 41 | 33 | Job. | Job | 2 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1885 | 69 | 35 | JOB | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1887 | 87 | 0 | Trabajo | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1890 | 124 | 80 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1892 | 144 | 0 | Trabajo | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 195 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 196 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 209 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 217 | JOB | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 220 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 221 | JOB | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 224 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 225 | JOB | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1893 | 151 | 0 | Trabajo | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 0 | Trabajo | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 22 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1895 | 174 | 54 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 124 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 127 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1895 | 176 | 150 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 0 | Trabajo | Job | 2 |
| La Torre del Vigía | La Torre del Vigía — junio de 1897 | 201 | 0 | Trabajo | Job | 2 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1898 | 215 | 41 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 0 | Trabajo | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1905 | 297 | 219 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 130 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1910 | 351 | 77 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1911 | 364 | 0 | Trabajo | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1916 | 424 | 27 | Job. | Job | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1916 | 424 | 34 | Job. | Job | 1 |
| Lo que dijo el pastor Russell | DEMONIOS — Hora de juzgar | 222 | 3 | Job. | Job | 1 |
| Lo que dijo el pastor Russell | SACERDOCIO — ¿Por qué Job y otros no fueron sacerdotes? | 553 | 2 | Job. | Job | 1 |

### Joel (3)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — mayo de 1908 | 329 | 65 | Joel. | Joel | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1909 | 345 | 26 | Joel. | Joel | 2 |

### Josué (3)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1885 | 72 | 62 | José. 26:19-22 | Josué 24:19-22 | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1896 | 189 | 169 | José. 10:3; y 11 | Josué 10:3; y 11 | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1901 | 249 | 0 | José. 24:15 | Josué 24:15 | 1 |

### Juan (59)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — julio de 1879 | 1 | 100 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1879 | 2 | 21 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1879 | 2 | 33 | Jnúm. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1879 | 4 | 74 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 30 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 72 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 73 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 100 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 29 | Jno. | Juan | 3 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 46 | Jnú. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1884 | 54 | 40 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1884 | 54 | 44 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 54 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 56 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1887 | 84 | 37 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1887 | 89 | 63 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1887 | 90 | 124 | Jnú. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1890 | 120 | 24 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1894 | 170 | 37 | Jno. | Juan | 2 |
| La Torre del Vigía | La Torre del Vigía — julio de 1896 | 190 | 203 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1897 | 202 | 102 | Jnú. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1897 | 203 | 81 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1897 | 203 | 102 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1898 | 217 | 167 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1899 | 224 | 26 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 234 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 178 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 168 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 170 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 171 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 172 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1903 | 267 | 125 | Jnúm. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1905 | 291 | 21 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1905 | 293 | 47 | Jno. | Juan | 3 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1905 | 293 | 48 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1905 | 293 | 50 | Jno. | Juan | 2 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1905 | 293 | 52 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1905 | 296 | 38 | Jno. | Juan | 3 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1905 | 298 | 187 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1906 | 301 | 57 | Jno. | Juan | 2 |
| La Torre del Vigía | La Torre del Vigía — enero de 1906 | 301 | 57 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1906 | 302 | 25 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1906 | 302 | 26 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1906 | 303 | 38 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 55 | Jno. | Juan | 2 |
| La Torre del Vigía | La Torre del Vigía — junio de 1907 | 318 | 54 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1907 | 318 | 56 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 40 | Jno. | Juan | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1907 | 324 | 68 | Jno. | Juan | 1 |

### Lamentaciones (1)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 67 | Justicia.  | Lamentaciones  | 1 |

### Levítico (5)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| El Tiempo Está a la Mano | Estudio 9 — El gran jubileo de la tierra | 10 | 21 | Lev. | Levítico | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 36 | Lev. | Levítico | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1890 | 121 | 52 | Lev. | Levítico | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1907 | 320 | 22 | Lev. | Levítico | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1912 | 380 | 42 | Levítico 185; | Levítico 18:5; | 1 |

### Lucas (5)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — enero de 1906 | 301 | 57 | Lu. | Lucas | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1906 | 302 | 26 | Lu. | Lucas | 2 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1912 | 380 | 42 | Lucas 1028. | Lucas 10:28. | 1 |
| Lo que dijo el pastor Russell | FE — Cuando venga el Hijo del Hombre, ¿hallará fe? | 775 | 1 | ucas | Lucas | 1 |

### Malaquías (5)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| Foto-Drama de la Creación | EVA ENGAÑADA | 13 | 4 | Mal. | Malaquías | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1881 | 26 | 384 | Mal. | Malaquías | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1895 | 172 | 162 | Mal. | Malaquías | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1901 | 246 | 158 | Mal. | Malaquías | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1916 | 425 | 80 | Mal. | Malaquías | 1 |

### Marcos (13)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — abril de 1882 | 31 | 90 | Marco  | Marcos  | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1883 | 41 | 60 | Marco | Marcos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1885 | 64 | 57 | Marco | Marcos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1892 | 142 | 59 | Marco | Marcos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 70 | Marco | Marcos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1896 | 195 | 217 | Marco | Marcos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 74 | Marco | Marcos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1904 | 277 | 264 | Marco | Marcos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1904 | 278 | 217 | Marco | Marcos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1906 | 304 | 121 | Marco | Marcos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1908 | 328 | 84 | Marco | Marcos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1908 | 328 | 85 | Marco | Marcos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1914 | 401 | 76 | Marco | Marcos | 1 |

### Mateo (407)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| El Plan Divino de las Edades | Estudio 21 — El reino de Dios — Parte 2/2 | 22 | 3 | Mat. | Mateo | 1 |
| El Plan Divino de las Edades | Estudio 21 — El reino de Dios — Parte 2/2 | 22 | 13 | Mat. | Mateo | 1 |
| El Tiempo Está a la Mano | Estudio 5 — La manera del regreso y aparición de nuestro Señor — Parte 1/4 | 6 | 21 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1879 | 1 | 120 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1879 | 2 | 66 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1879 | 2 | 68 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1879 | 2 | 107 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 15 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 30 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 76 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 94 | Mate. | Mateo | 3 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1879 | 4 | 95 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 10 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 14 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 50 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 94 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 46 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 85 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 88 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 89 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 92 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1880 | 7 | 73 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1880 | 8 | 63 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 66 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 67 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1880 | 10 | 58 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1880 | 10 | 76 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1880 | 10 | 81 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 26 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 35 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 84 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 91 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 28 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 29 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 75 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 79 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 36 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 44 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1880 | 14 | 17 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1880 | 14 | 102 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 53 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 54 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 68 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 117 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 129 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 3 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 31 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 32 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 36 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 78 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 79 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 101 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 108 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 109 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1880 | 17 | 54 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1880 | 17 | 104 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 15 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 80 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 7 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 15 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 57 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 61 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1881 | 20 | 43 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1881 | 20 | 49 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 74 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 5 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 20 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 67 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 74 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1881 | 23 | 16 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1881 | 23 | 59 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — junio de 1881 | 24 | 97 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1881 | 25 | 51 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1881 | 26 | 217 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1881 | 26 | 375 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1881 | 26 | 391 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1881 | 28 | 97 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1882 | 29 | 63 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 12 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 26 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1882 | 31 | 37 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1882 | 31 | 67 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1882 | 31 | 80 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1882 | 31 | 85 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1882 | 32 | 61 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1882 | 32 | 65 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1882 | 32 | 92 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1882 | 32 | 123 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1882 | 33 | 19 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1882 | 33 | 38 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1882 | 34 | 54 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1882 | 34 | 90 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1882 | 36 | 42 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1882 | 36 | 95 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1882 | 36 | 97 | Mate. | Mateo | 3 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 130 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 22 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 32 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 47 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 77 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 82 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1883 | 40 | 69 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1883 | 48 | 65 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1884 | 52 | 92 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1884 | 52 | 120 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1884 | 56 | 21 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1884 | 57 | 100 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 63 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 68 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1884 | 61 | 42 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1884 | 61 | 51 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1884 | 61 | 98 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1885 | 62 | 57 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1885 | 62 | 66 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1885 | 62 | 86 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1885 | 62 | 104 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1885 | 62 | 167 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 26 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 39 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 46 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 73 | mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 89 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1885 | 64 | 52 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1885 | 64 | 60 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1885 | 65 | 7 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1885 | 65 | 104 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1885 | 66 | 5 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1885 | 66 | 14 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1885 | 66 | 30 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1885 | 66 | 56 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1885 | 67 | 103 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1885 | 67 | 112 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1885 | 69 | 67 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1885 | 69 | 70 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1885 | 70 | 4 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1885 | 71 | 74 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1885 | 72 | 3 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1885 | 72 | 31 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1885 | 72 | 73 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1885 | 72 | 74 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1885 | 72 | 82 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1886 | 73 | 92 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1886 | 73 | 105 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1886 | 74 | 6 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1886 | 74 | 70 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1886 | 75 | 96 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1886 | 75 | 104 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1886 | 76 | 86 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1886 | 76 | 124 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1886 | 77 | 75 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1886 | 78 | 68 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1886 | 80 | 82 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1886 | 81 | 6 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1886 | 81 | 90 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1887 | 87 | 84 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1887 | 87 | 88 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1887 | 89 | 60 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1887 | 90 | 18 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1887 | 92 | 48 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1887 | 92 | 90 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1887 | 93 | 88 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1888 | 95 | 83 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1888 | 100 | 79 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1888 | 102 | 24 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1888 | 104 | 109 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1888 | 104 | 111 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1889 | 105 | 82 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1889 | 112 | 25 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1890 | 115 | 84 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1890 | 122 | 126 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1890 | 123 | 17 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1890 | 124 | 105 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 17 | MATE. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 36 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 122 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1891 | 127 | 113 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1891 | 130 | 10 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1891 | 134 | 79 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1892 | 136 | 91 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1892 | 136 | 216 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1892 | 139 | 128 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1892 | 140 | 37 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1892 | 141 | 82 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1892 | 142 | 171 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1892 | 143 | 13 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1892 | 144 | 68 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1892 | 145 | 25 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1892 | 146 | 132 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1892 | 146 | 145 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1892 | 146 | 157 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 53 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 69 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 74 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 80 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 85 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 115 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 119 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 175 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 185 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1893 | 152 | 75 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1893 | 153 | 147 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1893 | 154 | 125 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1893 | 157 | 3 | Mate. | Mateo | 3 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1893 | 159 | 194 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1894 | 161 | 173 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1894 | 162 | 29 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 12 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 71 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 155 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 245 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1894 | 166 | 27 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1894 | 166 | 47 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1894 | 166 | 122 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1894 | 166 | 179 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1894 | 166 | 213 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 82 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 133 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 165 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1894 | 168 | 36 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1894 | 168 | 38 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1894 | 169 | 26 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1894 | 169 | 39 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1894 | 169 | 54 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1894 | 170 | 80 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1894 | 170 | 190 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1894 | 171 | 77 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1894 | 171 | 83 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1894 | 171 | 146 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1895 | 172 | 78 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1895 | 172 | 177 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1895 | 172 | 181 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1895 | 173 | 61 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1895 | 173 | 77 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1895 | 174 | 82 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 7 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 21 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 40 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 61 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 68 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 165 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1895 | 176 | 78 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1895 | 176 | 85 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1895 | 178 | 67 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1895 | 179 | 70 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1895 | 180 | 136 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 158 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 160 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 163 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1895 | 183 | 26 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1895 | 183 | 44 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1896 | 184 | 12 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1896 | 186 | 66 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1896 | 187 | 29 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1896 | 187 | 67 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1896 | 188 | 13 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1896 | 188 | 60 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1896 | 188 | 68 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1896 | 189 | 23 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1896 | 189 | 75 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1896 | 190 | 34 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1896 | 190 | 101 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1896 | 190 | 167 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1896 | 190 | 184 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1896 | 194 | 110 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1896 | 195 | 4 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1896 | 195 | 48 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1896 | 195 | 190 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1897 | 198 | 165 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1897 | 201 | 11 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1897 | 203 | 81 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — enero de 1898 | 208 | 40 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1898 | 209 | 60 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1898 | 209 | 87 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1898 | 210 | 79 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1898 | 211 | 99 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1898 | 211 | 113 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1898 | 211 | 203 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1898 | 211 | 214 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1898 | 211 | 225 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1898 | 211 | 231 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1898 | 212 | 41 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1898 | 212 | 69 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1898 | 212 | 82 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1898 | 213 | 60 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1898 | 213 | 84 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1898 | 214 | 74 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1898 | 215 | 153 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1898 | 216 | 33 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1898 | 216 | 86 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 165 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 235 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1899 | 221 | 27 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1899 | 221 | 41 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1899 | 221 | 131 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 21 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 34 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 70 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 167 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1899 | 223 | 11 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1899 | 224 | 27 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1899 | 225 | 30 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1899 | 228 | 220 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1900 | 232 | 13 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1900 | 232 | 88 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1900 | 233 | 79 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1900 | 234 | 14 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1900 | 236 | 61 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1900 | 237 | 47 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1900 | 237 | 80 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1900 | 237 | 85 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1900 | 239 | 67 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1900 | 239 | 153 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1900 | 240 | 63 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1900 | 240 | 206 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1900 | 240 | 228 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 198 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 340 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 348 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — abril de 1901 | 244 | 109 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1901 | 245 | 164 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1901 | 249 | 37 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1902 | 253 | 26 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 39 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 80 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 84 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 108 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1903 | 267 | 79 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1903 | 271 | 129 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1903 | 274 | 79 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1903 | 275 | 78 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1904 | 277 | 11 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1904 | 277 | 112 | Mat. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1904 | 279 | 69 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1904 | 281 | 34 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1904 | 287 | 62 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1905 | 290 | 300 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1905 | 292 | 95 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1905 | 292 | 96 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1905 | 293 | 47 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — julio de 1905 | 295 | 59 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1905 | 295 | 127 | Estera.  | Mateo  | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1905 | 296 | 38 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1905 | 296 | 117 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1905 | 298 | 54 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1905 | 298 | 205 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1905 | 300 | 281 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1906 | 301 | 57 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1906 | 302 | 25 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1906 | 302 | 83 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1906 | 304 | 42 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1906 | 304 | 264 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1906 | 305 | 63 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1906 | 306 | 26 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 67 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1906 | 310 | 136 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1906 | 311 | 39 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 60 | Mate. | Mateo | 2 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 62 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1907 | 317 | 46 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1907 | 318 | 50 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1907 | 318 | 54 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1907 | 320 | 14 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1907 | 321 | 23 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 244 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1907 | 324 | 71 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1909 | 348 | 69 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1910 | 350 | 108 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1910 | 352 | 42 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1910 | 352 | 56 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1910 | 352 | 65 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1910 | 356 | 71 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1910 | 357 | 116 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 20 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 32 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1911 | 362 | 59 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1911 | 364 | 119 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1912 | 373 | 8 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1912 | 374 | 80 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1912 | 376 | 103 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1912 | 377 | 32 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1912 | 377 | 57 | MATE. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1912 | 379 | 73 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1912 | 380 | 39 | Mate. | Mateo | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1912 | 381 | 50 | Mate. | Mateo | 1 |

### Miqueas (1)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — abril de 1911 | 364 | 100 | Micrófono.  | Miqueas  | 1 |

### Nahúm (3)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Batalla de Armagedón | Estudio 6 — Babilonia ante el gran tribunal: su confusión — Eclesiástica | 7 | 280 | No.  | Nahúm  | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1893 | 158 | 136 | No.  | Nahúm  | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 124 | Nah. | Nahúm | 1 |

### Nehemías (1)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — enero de 1914 | 397 | 160 | Neh. | Nehemías | 1 |

### Números (3)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 0 | Núm. | Números | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 184 | NÚMERO.  | Números  | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 234 | NÚMERO.  | Números  | 1 |

### Pedro (2)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — julio de 1884 | 56 | 54 | Mascota. | Pedro | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 50 | mascota. | Pedro | 1 |

### Proverbios (3)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1893 | 158 | 170 | Prov. | Proverbios | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1897 | 204 | 54 | Prov. | Proverbios | 1 |
| Escritos del pastor Russell para Overland Monthly | El pueblo escogido de Dios — El Jubileo de la Restauración | 84 | 16 | Prov. | Proverbios | 1 |

### Romanos (446)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| El Plan Divino de las Edades | Estudio 4 — La Biblia como revelación divina — Parte 2/2 | 5 | 14 | Rom. | Romanos | 1 |
| El Plan Divino de las Edades | Estudio 9 — El permiso del mal | 10 | 20 | Rom. | Romanos | 1 |
| El Plan Divino de las Edades | Estudio 21 — El reino de Dios — Parte 2/2 | 22 | 15 | Rom. | Romanos | 1 |
| El Tiempo Está a la Mano | Estudio 10 — Las dispensaciones paralelas — Parte 1/3 | 11 | 14 | Rom. | Romanos | 1 |
| La Expiación entre Dios y el Hombre | Estudio 14 — La necesidad de la expiación — La maldición | 15 | 43 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1879 | 1 | 48 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1879 | 1 | 83 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1879 | 1 | 100 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1879 | 1 | 123 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1879 | 2 | 100 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 18 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 22 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 25 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 35 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 40 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 51 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 56 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 63 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 64 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 66 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 72 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 77 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 87 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 89 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 90 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1879 | 4 | 21 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1879 | 4 | 25 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1879 | 4 | 76 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1879 | 4 | 83 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1879 | 4 | 86 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 29 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 33 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 38 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 56 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 61 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 62 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 69 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 25 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 75 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 94 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1880 | 7 | 33 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1880 | 7 | 60 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1880 | 7 | 68 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1880 | 8 | 38 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1880 | 8 | 46 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1880 | 8 | 56 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1880 | 8 | 63 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1880 | 8 | 93 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 19 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 30 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 66 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1880 | 10 | 53 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1880 | 10 | 56 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1880 | 10 | 63 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 16 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 47 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 49 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 53 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 57 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 77 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 87 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 33 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 38 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 46 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 47 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 55 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 91 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 92 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1880 | 13 | 99 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1880 | 15 | 22 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 9 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 37 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 41 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 43 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1880 | 16 | 44 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1880 | 17 | 50 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1880 | 17 | 55 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1880 | 17 | 63 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1880 | 17 | 82 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 10 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1881 | 19 | 93 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1881 | 20 | 99 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1881 | 20 | 100 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1881 | 20 | 101 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 51 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 53 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 62 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 64 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 65 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 70 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 80 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 81 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 82 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1881 | 21 | 84 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 66 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 72 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1881 | 22 | 75 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1881 | 23 | 3 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1881 | 23 | 37 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1881 | 23 | 52 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1881 | 23 | 53 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1881 | 23 | 91 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1881 | 24 | 114 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1881 | 25 | 12 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1881 | 26 | 314 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1881 | 26 | 474 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1881 | 27 | 54 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1881 | 27 | 55 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1881 | 28 | 40 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 35 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1882 | 31 | 35 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1882 | 32 | 69 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1882 | 34 | 22 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1882 | 34 | 67 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1882 | 35 | 86 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1882 | 36 | 13 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 27 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 33 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 41 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 43 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 57 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 124 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 125 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 32 | Memoria de sólo lectura. | Romanos | 6 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1882 | 38 | 41 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1883 | 39 | 50 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1883 | 39 | 129 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1884 | 52 | 57 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1884 | 54 | 52 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1884 | 54 | 75 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1884 | 54 | 88 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 46 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 47 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1884 | 58 | 68 | Memoria de sólo lectura. | Romanos | 6 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1884 | 59 | 71 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1884 | 59 | 91 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1884 | 61 | 41 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1884 | 61 | 135 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1885 | 62 | 43 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1885 | 62 | 120 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 46 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 92 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1885 | 63 | 111 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1885 | 65 | 98 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1885 | 66 | 6 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1885 | 67 | 27 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1885 | 67 | 67 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 7 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 65 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 75 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 82 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 105 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1885 | 68 | 131 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1885 | 69 | 42 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1885 | 72 | 40 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1886 | 73 | 7 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1886 | 73 | 8 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1886 | 74 | 55 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1886 | 75 | 54 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1886 | 75 | 88 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1886 | 78 | 69 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1886 | 78 | 79 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1886 | 79 | 14 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1886 | 82 | 42 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1886 | 82 | 50 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1887 | 84 | 11 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1887 | 84 | 144 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1887 | 85 | 95 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1887 | 87 | 86 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1887 | 88 | 122 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1887 | 89 | 68 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1887 | 92 | 58 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1887 | 93 | 82 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1887 | 93 | 88 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1888 | 95 | 43 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1888 | 95 | 75 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1888 | 97 | 24 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1888 | 97 | 121 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1888 | 102 | 20 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1888 | 102 | 54 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1888 | 102 | 73 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1888 | 102 | 86 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1888 | 103 | 17 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1888 | 104 | 119 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1889 | 105 | 47 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1889 | 106 | 24 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1889 | 108 | 47 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1889 | 108 | 101 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1890 | 118 | 15 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1890 | 119 | 46 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1890 | 122 | 122 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1890 | 123 | 94 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1890 | 124 | 17 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1891 | 125 | 17 | MEMORIA DE SÓLO LECTURA. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1891 | 126 | 10 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1891 | 127 | 122 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1891 | 127 | 125 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1891 | 131 | 58 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1891 | 135 | 24 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1891 | 135 | 38 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1892 | 141 | 46 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1892 | 142 | 151 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1892 | 145 | 162 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 110 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1893 | 151 | 37 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1893 | 151 | 43 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1893 | 151 | 53 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1893 | 151 | 54 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1893 | 153 | 184 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1893 | 155 | 151 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1893 | 156 | 65 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1893 | 156 | 113 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1893 | 156 | 116 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1893 | 156 | 145 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1893 | 156 | 175 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1893 | 157 | 13 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1893 | 157 | 78 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1894 | 160 | 130 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1894 | 160 | 230 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1894 | 161 | 42 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1894 | 161 | 78 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1894 | 161 | 173 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1894 | 162 | 33 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1894 | 162 | 52 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1894 | 162 | 139 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1894 | 163 | 38 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1894 | 163 | 132 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 27 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 245 | Memoria de sólo lectura. | Romanos | 3 |
| La Torre del Vigía | La Torre del Vigía — julio de 1894 | 166 | 122 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1894 | 166 | 179 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 38 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 66 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1894 | 168 | 195 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1894 | 169 | 39 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1894 | 169 | 55 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1894 | 169 | 55 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1894 | 169 | 81 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1894 | 170 | 103 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1894 | 170 | 152 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1894 | 171 | 77 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1895 | 172 | 55 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1895 | 172 | 82 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1895 | 172 | 164 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1895 | 172 | 181 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1895 | 174 | 38 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 50 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 61 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1895 | 177 | 33 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1895 | 178 | 30 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1895 | 180 | 61 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1895 | 180 | 139 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 156 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 158 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 160 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1895 | 182 | 25 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1896 | 188 | 175 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1896 | 189 | 184 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1896 | 190 | 108 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1896 | 194 | 110 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1897 | 196 | 139 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1897 | 197 | 12 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1897 | 198 | 102 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1897 | 198 | 160 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1897 | 200 | 246 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1897 | 201 | 31 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1897 | 201 | 68 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1897 | 203 | 39 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1897 | 204 | 74 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1897 | 204 | 74 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1898 | 211 | 71 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1898 | 211 | 83 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1898 | 215 | 196 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1898 | 216 | 137 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1898 | 216 | 141 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1898 | 217 | 120 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1898 | 217 | 167 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1898 | 218 | 27 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 78 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 125 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 152 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 235 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 239 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1898 | 219 | 246 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1899 | 220 | 29 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1899 | 220 | 212 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1899 | 221 | 40 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1899 | 221 | 88 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1899 | 221 | 151 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 6 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 7 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 16 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 40 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1899 | 222 | 169 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1899 | 223 | 24 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1899 | 223 | 78 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1899 | 223 | 102 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1899 | 226 | 47 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1899 | 227 | 58 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1899 | 228 | 52 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1899 | 228 | 174 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1900 | 229 | 58 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1900 | 231 | 36 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1900 | 231 | 78 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1900 | 231 | 86 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1900 | 233 | 75 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1900 | 236 | 22 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1900 | 237 | 38 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1900 | 237 | 216 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1900 | 238 | 85 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1900 | 238 | 164 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1900 | 238 | 213 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1900 | 239 | 20 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1900 | 239 | 45 | MEMORIA DE SÓLO LECTURA. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1900 | 239 | 66 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1900 | 239 | 151 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1900 | 240 | 72 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 87 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 256 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 259 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1901 | 241 | 348 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1901 | 243 | 167 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1901 | 244 | 67 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1901 | 244 | 110 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1901 | 245 | 21 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1901 | 246 | 24 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1901 | 246 | 29 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1901 | 247 | 59 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1901 | 247 | 145 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1901 | 248 | 47 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1901 | 248 | 125 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1901 | 252 | 122 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 19 | Memoria de sólo lectura. | Romanos | 3 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 20 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1902 | 254 | 44 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 278 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 282 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1902 | 256 | 184 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 237 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 170 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1902 | 262 | 32 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1903 | 265 | 118 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1903 | 267 | 149 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1903 | 267 | 150 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1903 | 267 | 151 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1903 | 271 | 12 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1904 | 277 | 241 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1904 | 281 | 57 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1904 | 283 | 48 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1905 | 291 | 21 | Memoria de sólo lectura. | Romanos | 3 |
| La Torre del Vigía | La Torre del Vigía — abril de 1905 | 292 | 97 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1905 | 293 | 47 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1905 | 296 | 38 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1905 | 297 | 80 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1905 | 297 | 112 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1905 | 298 | 54 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1905 | 298 | 187 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1905 | 299 | 54 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1905 | 300 | 231 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1905 | 300 | 256 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1905 | 300 | 256 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1906 | 304 | 75 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1906 | 304 | 132 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1906 | 308 | 22 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1906 | 310 | 21 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1906 | 310 | 139 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 58 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1907 | 316 | 35 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1907 | 317 | 26 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1907 | 317 | 30 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1907 | 318 | 50 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1907 | 318 | 54 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 40 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 45 | Memoria de sólo lectura. | Romanos | 2 |
| La Torre del Vigía | La Torre del Vigía — julio de 1907 | 319 | 71 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1907 | 320 | 28 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1907 | 323 | 36 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1907 | 324 | 46 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1907 | 324 | 71 | Memoria de sólo lectura. | Romanos | 6 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1909 | 338 | 146 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1909 | 340 | 23 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1909 | 344 | 33 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1909 | 345 | 69 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1909 | 347 | 46 | Rom. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 5 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 13 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1910 | 359 | 40 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1911 | 365 | 59 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1911 | 372 | 111 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1912 | 376 | 78 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1912 | 376 | 82 | MEMORIA DE SÓLO LECTURA. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1912 | 378 | 46 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1912 | 380 | 10 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1912 | 380 | 10 | Romanos 326. | Romanos 3:26. | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1912 | 380 | 42 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1912 | 380 | 42 | Romanos 105; | Romanos 10:5; | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1912 | 383 | 27 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1913 | 387 | 88 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1913 | 387 | 98 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1913 | 393 | 20 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1913 | 395 | 58 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1913 | 396 | 14 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1914 | 405 | 24 | Memoria de sólo lectura. | Romanos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1915 | 411 | 46 | Memoria de sólo lectura. | Romanos | 2 |
| Lo que dijo el pastor Russell | ISRAEL — Los «siete tiempos» de castigo como bendición | 356 | 8 | Memoria de sólo lectura. | Romanos | 1 |

### Rut (5)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 74 | Rut. | Rut | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 75 | RUT | Rut | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 200 | RUT | Rut | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 213 | Rut. | Rut | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1903 | 271 | 166 | Rut. | Rut | 1 |

### Salmos (49)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| El Plan Divino de las Edades | Estudio 4 — La Biblia como revelación divina — Parte 2/2 | 5 | 11 | Sal. | Salmos | 1 |
| Venga Tu Reino | Estudio 7 — La liberación y la exaltación de la Iglesia | 8 | 7 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1879 | 4 | 78 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1879 | 4 | 90 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 47 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1879 | 5 | 58 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 26 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 47 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1879 | 6 | 79 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 38 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 72 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 45 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1880 | 11 | 67 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1880 | 17 | 70 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1881 | 20 | 30 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1881 | 20 | 31 | PD. | Salmos | 4 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1881 | 28 | 68 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 50 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1882 | 30 | 76 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1886 | 74 | 58 | Psa. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1890 | 122 | 132 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1892 | 136 | 152 | PSA. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1892 | 147 | 126 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1893 | 150 | 211 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1893 | 155 | 13 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1893 | 155 | 33 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1894 | 162 | 177 | PSA. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 124 | PSA. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 43 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1896 | 188 | 35 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1896 | 194 | 129 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1898 | 208 | 9 | PSA. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1898 | 216 | 36 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 155 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1902 | 256 | 150 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1902 | 259 | 175 | Ps. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1903 | 267 | 25 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1904 | 278 | 209 | PSA. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1904 | 282 | 59 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1907 | 315 | 36 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1908 | 331 | 72 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1908 | 332 | 80 | Sal. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1910 | 350 | 131 | PD. | Salmos | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1913 | 387 | 100 | Sal. | Salmos | 1 |
| Escritos del pastor Russell para Overland Monthly | El Gran Trono Blanco — El Día del Juicio mal entendido | 255 | 4 | Sal. | Salmos | 1 |
| Escritos del pastor Russell para Overland Monthly | El Gran Trono Blanco — El Día del Juicio mal entendido | 311 | 4 | Sal. | Salmos | 1 |

### Samuel (1)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — febrero de 1884 | 52 | 102 | Sam. | Samuel | 1 |

### Santiago (12)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — febrero de 1891 | 126 | 50 | St. | Santiago | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1893 | 149 | 191 | St. | Santiago | 2 |
| La Torre del Vigía | La Torre del Vigía — abril de 1893 | 151 | 196 | St. | Santiago | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 54 | St. | Santiago | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1894 | 167 | 112 | Sant. | Santiago | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1896 | 190 | 104 | Sant. | Santiago | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1900 | 239 | 180 | St. | Santiago | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1903 | 266 | 67 | St. | Santiago | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1906 | 302 | 124 | St. | Santiago | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 249 | St. | Santiago | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1908 | 327 | 28 | SANTA.  | Santiago  | 1 |

### Sofonías (15)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 6 | Sofo.  | Sofonías  | 2 |
| La Torre del Vigía | La Torre del Vigía — junio de 1880 | 12 | 46 | Sof. | Sofonías | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 106 | Sofo.  | Sofonías  | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 107 | Sofo.  | Sofonías  | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1886 | 77 | 76 | Sofo.  | Sofonías  | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1895 | 175 | 21 | Sofo.  | Sofonías  | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1898 | 218 | 119 | Sofo.  | Sofonías  | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1902 | 261 | 159 | Sofo.  | Sofonías  | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1902 | 263 | 138 | Sofo.  | Sofonías  | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1905 | 292 | 95 | Sofo.  | Sofonías  | 1 |
| Lo que dijo el pastor Russell | MUERTE — ¿Debe toda la humanidad entrar en la tumba? | 216 | 5 | Zep. | Sofonías | 1 |
| Lo que dijo el pastor Russell | DESTRUCCIÓN — La montaña de la destrucción (la batalla de Armagedón) | 769 | 3 | Sofo.  | Sofonías  | 1 |
| Lo que dijo el pastor Russell | TIERRA — ¿Será quemada? | 771 | 5 | Sofo.  | Sofonías  | 1 |
| Lo que dijo el pastor Russell | ANGUSTIA — El tiempo de angustia en todo el mundo | 849 | 2 | Zep. | Sofonías | 1 |

### Tesalonicenses (1)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — octubre de 1909 | 346 | 126 | Tes. | Tesalonicenses | 1 |

### Timoteo (3)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — enero de 1902 | 253 | 39 | Tim. | Timoteo | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1902 | 258 | 0 | Pregunta.—¿Entiendes yo, Tim? 2:15 para ser literal? | Pregunta.—¿Entiendes 1 Timoteo 2:15 literalmente? | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1909 | 342 | 148 | Tim. | Timoteo | 1 |

### Tito (9)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Expiación entre Dios y el Hombre | Estudio 2 — El autor de la expiación | 3 | 6 | Teta.  | Tito  | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1892 | 146 | 45 | Tito. | Tito | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1893 | 156 | 65 | Teta.  | Tito  | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1895 | 173 | 90 | Teta.  | Tito  | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1898 | 211 | 37 | Teta.  | Tito  | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1900 | 239 | 72 | TITO | Tito | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1900 | 239 | 74 | Tito. | Tito | 1 |
| La Torre del Vigía | La Torre del Vigía — noviembre de 1900 | 239 | 86 | Tito. | Tito | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1902 | 255 | 2 | Tito. | Tito | 1 |

### Zacarías (20)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| El Tiempo Está a la Mano | Estudio 3 — El cumplimiento de la profecía del tiempo en el primer advenimiento de Cristo | 4 | 26 | Zac. | Zacarías | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 9 | Zac. | Zacarías | 1 |
| La Torre del Vigía | La Torre del Vigía — septiembre de 1879 | 3 | 11 | Zec. | Zacarías | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1880 | 9 | 50 | Zac. | Zacarías | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 112 | Zac. | Zacarías | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1882 | 37 | 113 | Zec. | Zacarías | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1888 | 95 | 85 | Zaca.  | Zacarías  | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1891 | 126 | 94 | Zac. | Zacarías | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1893 | 148 | 89 | ZECH.  | Zacarías  | 1 |
| La Torre del Vigía | La Torre del Vigía — enero de 1893 | 148 | 98 | ZECH.  | Zacarías  | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 167 | Zac. | Zacarías | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1895 | 181 | 44 | Zac. | Zacarías | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1898 | 214 | 167 | Zech. | Zacarías  | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1899 | 226 | 68 | ZECA. | Zacarías | 1 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1900 | 240 | 219 | Zac. | Zacarías | 1 |
| La Torre del Vigía | La Torre del Vigía — febrero de 1901 | 242 | 13 | Zaca.  | Zacarías  | 1 |
| La Torre del Vigía | La Torre del Vigía — abril de 1901 | 244 | 136 | Zaca.  | Zacarías  | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1901 | 246 | 126 | ZACA.  | Zacarías  | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1906 | 307 | 285 | Zech. | Zacarías  | 1 |
| Lo que dijo el pastor Russell | HERIDAS — Herido en la casa de sus amigos | 740 | 1 | Zec. | Zacarías | 1 |

### Éxodo (10)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 54 | Ej. | Éxodo  | 2 |
| La Torre del Vigía | La Torre del Vigía — diciembre de 1880 | 18 | 73 | Ej. | Éxodo  | 1 |
| La Torre del Vigía | La Torre del Vigía — junio de 1894 | 165 | 100 | ÉXOD. | Éxodo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1895 | 178 | 58 | EXOD. | Éxodo | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1902 | 259 | 0 | EJ. | Éxodo  | 2 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1902 | 260 | 0 | EJ. | Éxodo  | 1 |
| La Torre del Vigía | La Torre del Vigía — octubre de 1907 | 322 | 0 | ej. | Éxodo  | 1 |
| Lo que dijo el pastor Russell | CONSAGRACIÓN — Sobre la presentación del Señor después de 40 días | 758 | 3 | Éxo. | Éxodo | 1 |

### Dirección/esquina (no bíblico) (9)

| Obra | Artículo/capítulo | Pág. | Párr. | Original | Corrección | Rep. |
| --- | --- | ---: | ---: | --- | --- | ---: |
| La Torre del Vigía | La Torre del Vigía — octubre de 1881 | 27 | 0 | A. D. JONES, Corintios 27 y Broadway | A. D. JONES, esquina de la calle 27 y Broadway | 1 |
| La Torre del Vigía | La Torre del Vigía — marzo de 1891 | 127 | 0 | Jackson Hall, Corintios Yonge y las calles Blood | Jackson Hall, esquina de Yonge y las calles Blood | 1 |
| La Torre del Vigía | La Torre del Vigía — agosto de 1900 | 236 | 0 | “Hotel Grace”, Corintios Clark St. y Jackson Boulevard | “Hotel Grace”, esquina de Clark St. y Jackson Boulevard | 1 |
| La Torre del Vigía | La Torre del Vigía — mayo de 1902 | 257 | 0 | mundo entero. Corintios 5:7; | mundo entero. 1 Corintios 5:7; | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1909 | 343 | 0 | Auditorio, Corintios Calles 4ta y Faraón | Auditorio, esquina de las calles 4ta y Faraón | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1909 | 343 | 0 | Christensen's Hall, Corintios Broadway y Madison | Christensen's Hall, esquina de Broadway y Madison | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1909 | 343 | 0 | Iglesia Cristiana Central, Corintios Avenida 16 y calle Lincoln | Iglesia Cristiana Central, esquina de la Avenida 16 y la calle Lincoln | 1 |
| La Torre del Vigía | La Torre del Vigía — julio de 1909 | 343 | 0 | Salón Italiano, Corintios Calle 2d y Avenida Lincoln | Salón Italiano, esquina de la calle 2d y la Avenida Lincoln | 1 |
| Lo que dijo el pastor Russell | INCIENSO — Somos en Cristo un olor grato para Dios | 342 | 0 | Efesios 5:1,2, Corintios 2:15 | Efesios 5:1,2; 2 Corintios 2:15 | 1 |

## Índice temático

| Tema | Original | Corrección |
| --- | --- | --- |
| ABOMINACIÓN DE DESOLACIÓN | ; Dan. 11:31 profecía de,  | ; Daniel 11:31 profecía de,  |
| ALEJANDRO MAGNO | ; el gran y poderoso rey de Dan. 11:3,  | ; el gran y poderoso rey de Daniel 11:3,  |
| ANARQUÍA | ; profetizado en Sal. 46:1-2,  | ; profetizado en Salmos 46:1-2,  |
| ANARQUÍA |  (1912); puede ser el significado de Ezek. 7:13-24,  |  (1912); puede ser el significado de Ezequiel 7:13-24,  |
| ARMAGEDÓN |  (1912); llamada “Gran Tribulación” por Cristo (Mat. 24:21),  |  (1912); llamada “Gran Tribulación” por Cristo (Mateo 24:21),  |
| BEBÉS | ; en credos, pero demasiado corto para “hombre” (Isa. 28:20),  | ; en credos, pero demasiado corto para “hombre” (Isaías 28:20),  |
| BABILONIA | Primera bestia (león) (Dan. 7:2-7),  | Primera bestia (león) (Daniel 7:2-7),  |
| BABILONIA | ; cabeza de oro (Dan. 7:38),  | ; cabeza de oro (Daniel 7:38),  |
| BABILONIA | ; entrará en el olvido, sheol (Isa. 14:9),  | ; entrará en el olvido, sheol (Isaías 14:9),  |
| CEGUERA | ; Israel será salvo de (Rom. 11:26),  | ; Israel será salvo de (Romanos 11:26),  |
| SANGRE | ; justo, desde Abel hasta Zacarías (Mat. 23:35),  | ; justo, desde Abel hasta Zacarías (Mateo 23:35),  |
| CAPITAL(ISTAS) |  ; James en,  |  ; Santiago en,  |
| CRISTO | ; profecía de Sal. 2:12 parcialmente cumplido en,  | ; profecía de Salmos 2:12 parcialmente cumplido en,  |
| CIVIL | Autoridad, santuario de fortaleza (Dan. 11:31),  | Autoridad, santuario de fortaleza (Daniel 11:31),  |
| PACTO | ; mencionado en Isa. 54:1-8,  | ; mencionado en Isaías 54:1-8,  |
| CIRO | ; Isa. 45:13 sobre la construcción de la ciudad por,  | ; Isaías 45:13 sobre la construcción de la ciudad por,  |
| MUERTO |  ; resucitado a la vida (Heb. 11:35),  |  ; resucitado a la vida (Hebreos 11:35),  |
| MUERTE | ; miedo a, descrito (Sal. 116:3),  | ; miedo a, descrito (Salmos 116:3),  |
| LIBERACIÓN | ; nuestro Cuerpo (Rom. 8:22-23),  | ; nuestro Cuerpo (Romanos 8:22-23),  |
| COMER |  ; la glotonería (Fil. 3:19) trae sufrimientos no por justicia,  |  ; la glotonería (Filipenses 3:19) trae sufrimientos no por justicia,  |
| EGIPTO / EGIPCIOS | ; “Ay de los que descienden a” (Isa. 31:1),  | ; “Ay de los que descienden a” (Isaías 31:1),  |
| Perdurable | ; no prometido por 1 Tim. 2:4,  | ; no prometido por 1 Timoteo 2:4,  |
| PADRE | ; El Hijo no es el Padre en Jn. 14:7-10,  | ; El Hijo no es el Padre en Juan 14:7-10,  |
| PADRE | ; “Santo” (1 Jn. 2:20) el,  | ; “Santo” (1 Juan 2:20) el,  |
| MIEDO | Caer en las manos de Dios en estado imperfecto (Heb. 10:31),  | Caer en las manos de Dios en estado imperfecto (Hebreos 10:31),  |
| FIRMAMENTO | ; El Cristo (Dan. 12:3),  | ; El Cristo (Daniel 12:3),  |
| DILUVIO | ; Lo mismo que Dan. 12:5-7,  | ; Lo mismo que Daniel 12:5-7,  |
| DILUVIO | ; de Nah. 1:8 no literal,  | ; de Nahúm 1:8 no literal,  |
| PERDONAR |  ; ocurre en Col. 3:13 y Lc. 7:42, 43,  |  ; ocurre en Colosenses 3:13 y Lucas 7:42, 43,  |
| GLORIFICAR | Palabra griega para, en Rom. 8:30 significa “honrado”,  | Palabra griega para, en Romanos 8:30 significa “honrado”,  |
| EDAD DEL EVANGELIO | ; Respecto a Isa. 63:1-6,  | ; Respecto a Isaías 63:1-6,  |
| GRECIA | Cuatro divisiones de los cuatro “cuernos” de Dan. 8:8,  | Cuatro divisiones de los cuatro “cuernos” de Daniel 8:8,  |
| GRECIA | ; “rey del Norte” (Dan. 11:5-19),  | ; “rey del Norte” (Daniel 11:5-19),  |
| GRIEGO | “Presente” en Ef. 4:11, 12, significado,  | “Presente” en Efesios 4:11, 12, significado,  |
| GRIEGO | ; más antiguo, omite “espiritual” antes de “sacrificios” en 1Pedro 2:5,  | ; más antiguo, omite “espiritual” antes de “sacrificios” en 1 Pedro 2:5,  |
| COSECHA | ; respecto a Isa. 63:1-6,  | ; respecto a Isaías 63:1-6,  |
| ESPÍRITU SANTO | ; traducción del griego parakletos en Jn. 14:16, 26,  | ; traducción del griego parakletos en Juan 14:16, 26,  |
| ESPÍRITU SANTO |  ; indicado en Ef. 5:18-20,  |  ; indicado en Efesios 5:18-20,  |
| ESPÍRITU SANTO | ; en Jn. 16:13, 14 podría traducirse “él mismo” (forma neutra),  | ; en Juan 16:13, 14 podría traducirse “él mismo” (forma neutra),  |
| ESPÍRITU SANTO | ; traducido incorrectamente “él” en Jn. 14:17,  | ; traducido incorrectamente “él” en Juan 14:17,  |
| ESPÍRITU SANTO | ; “quién” y “él” están mal traducidos en Jn. 14:26,  | ; “quién” y “él” están mal traducidos en Juan 14:26,  |
| HONORES | ; El engendramiento de la Iglesia es el comienzo de (Rom. 8:30),  | ; El engendramiento de la Iglesia es el comienzo de (Romanos 8:30),  |
| CUERNO(S) | ; cuatro (Dan. 8:8),  | ; cuatro (Daniel 8:8),  |
| ISRAEL | ; ser salvo de (Rom. 11:26),  | ; ser salvo de (Romanos 11:26),  |
| JESÚS | ; siempre exceptuado en comparaciones como en 1 Tim. 6:15, 16,  | ; siempre exceptuado en comparaciones como en 1 Timoteo 6:15, 16,  |
| JESÚS | ; Que Jesús recibiera adoración no significaba que él fuera Dios, 72:1; Jn. 14:7-10 no muestra que Jesús sea Dios,  | ; Que Jesús recibiera adoración no significaba que él fuera Dios, 72:1; Juan 14:7-10 no muestra que Jesús sea Dios,  |
| JESÚS | ; no igual a Dios en Fil. 2:6, una mala traducción en King James,  | ; no igual a Dios en Filipenses 2:6, una mala traducción en King James,  |
| JESÚS | ; uno de los títulos de, en Isa. 9:6,  | ; uno de los títulos de, en Isaías 9:6,  |
| JESÚS | ; de Reyes (1 Tim. 6:15, 16),  | ; de Reyes (1 Timoteo 6:15, 16),  |
| JESÚS | ; apareció como mensajero de Jehová en Éx. 3:2,  | ; apareció como mensajero de Jehová en Éxodo 3:2,  |
| JESÚS | ; como se usa en Jn. 1:1,  | ; como se usa en Juan 1:1,  |
| JESÚS | ; descrito en Prov. 8:22-30,  | ; descrito en Proverbios 8:22-30,  |
| JESÚS | ; Isa. 53:2-3 no niega que Jesús estuviera separado de los pecadores,  | ; Isaías 53:2-3 no niega que Jesús estuviera separado de los pecadores,  |
| JESÚS | Isa. 52:14, 15, da un pensamiento erróneo respecto a,  | Isaías 52:14, 15, da un pensamiento erróneo respecto a,  |
| JESÚS | ; en Ej. 3:2 Logos apareció como mensajero de Jehová,  | ; en Éxodo 3:2 Logos apareció como mensajero de Jehová,  |
| LLAVES | ; al “misterio” (Col. 1:26),  | ; al “misterio” (Colosenses 1:26),  |
| REY |  Tim. 6:15, 16,  |  1 Timoteo 6:15, 16,  |
| REY | Ángeles de Mat. 24:31, mensajeros de lo nuevo,  | Ángeles de Mateo 24:31, mensajeros de lo nuevo,  |
| REINO | ; Reino de Jehová en Isa. 2:2-4 y Miqueas. 4:1-3,  | ; Reino de Jehová en Isaías 2:2-4 y Miqueas. 4:1-3,  |
| REINO | ; profetizado en Isa. 25:6-9,  | ; profetizado en Isaías 25:6-9,  |
| REINOS | ; Dan. 2:31-45 explicado,  | ; Daniel 2:31-45 explicado,  |
| REYES | ; La interpretación del papado de Sal. 2:12,  | ; La interpretación del papado de Salmos 2:12,  |
| VIVIENDO | Se requiere sacerdocio para convertirse en sacrificio (Ro. 12:1),  | Se requiere sacerdocio para convertirse en sacrificio (Romanos 12:1),  |
| VIVIENDO | ; Cristo resucitado es Señor de, (Rom. 14:9),  | ; Cristo resucitado es Señor de, (Romanos 14:9),  |
| HOGAZA | ; en Ej. 3:2 apareció como mensajero de Jehová,  | ; en Éxodo 3:2 apareció como mensajero de Jehová,  |
| HOGAZA | Como ocurre en Jn. 1:1,  | Como ocurre en Juan 1:1,  |
| Hombre | ; Hab. 2:5 puede referirse a  | ; Habacuc 2:5 puede referirse a  |
| MARCA | mk. 16:9-20 espurio,  | Marcos 16:9-20 espurio,  |
| EDAD MILENARIA | ; al final habrá luz (Zac. 14:6-7),  | ; al final habrá luz (Zacarías 14:6-7),  |
| EDAD MILENARIA | ; Isa. 25:6-9,  | ; Isaías 25:6-9,  |
| EDAD MILENARIA | ; Sábado de Mat. 24:20,  | ; Sábado de Mateo 24:20,  |
| EDAD MILENARIA | ; día de salvación (Sal. 118:18-27),  | ; día de salvación (Salmos 118:18-27),  |
| MISIONERO | 24:14 y Mc. 13:10,  | 24:14 y Marcos 13:10,  |
| NACIÓN | ; de hoy se puede hacer referencia en Hab. 2:5,  | ; de hoy se puede hacer referencia en Habacuc 2:5,  |
| NATURALEZA | ; “el único que tiene inmortalidad” (1 Tim. 6:14-16),  | ; “el único que tiene inmortalidad” (1 Timoteo 6:14-16),  |
| ACEITUNA | Respecto a Rom. 11:17, 24,  | Respecto a Romanos 11:17, 24,  |
| PAPADO | Firmamento del cielo (Gén. 1:16),  | Firmamento del cielo (Génesis 1:16),  |
| PAPADO | ; Sal. 2:12 según la interpretación de  | ; Salmos 2:12 según la interpretación de  |
| PERSONA | ; ese Espíritu Santo no puede ser, como se muestra en Ef. 5:18-20,  | ; ese Espíritu Santo no puede ser, como se muestra en Efesios 5:18-20,  |
| ARADOR | Alcanza al segador (Am. 9:13),  | Alcanza al segador (Amós 9:13),  |
| FUERZA | ; retratado en Sal. 139:7-8,  | ; retratado en Salmos 139:7-8,  |
| PRESBITERIO | Significado (1 Tim. 4:14),  | Significado (1 Timoteo 4:14),  |
| PRÍNCIPE | No confundir con el Mesías (Dan. 9:23-27),  | No confundir con el Mesías (Daniel 9:23-27),  |
| PROFECÍAS | ; demora de la visión (Hab. 2:2),  | ; demora de la visión (Habacuc 2:2),  |
| PROFECÍAS |  – 149:2; James, defraudando a los agricultores,  |  – 149:2; Santiago, defraudando a los agricultores,  |
| PROFECÍAS | ; James, lucha entre capital y trabajo,  | ; Santiago, lucha entre capital y trabajo,  |
| PROFECÍAS |  ; por James,  |  ; por Santiago,  |
| PROFECÍAS | ; Sal. 2:12 mal aplicado por el Anticristo,  | ; Salmos 2:12 mal aplicado por el Anticristo,  |
| PIRÁMIDE | Cleopatra: De Egipto (Dan. 11:17),  | Cleopatra: De Egipto (Daniel 11:17),  |
| VIVIFICAR | ; “vivificado” (1 Ped. 3:18),  | ; “vivificado” (1 Pedro 3:18),  |
| REPROCHE | ; no anciano (1 Tim. 5:1),  | ; no anciano (1 Timoteo 5:1),  |
| RECOMPENSA(S) | ; “año de, para la controversia de Sión” (Isa. 34:8),  | ; “año de, para la controversia de Sión” (Isaías 34:8),  |
| RECONCILIACIÓN | ; Traducido del kattalage traducido como “Expiación” en Rom. 5:11,  | ; Traducido del kattalage traducido como “Expiación” en Romanos 5:11,  |
| RELACIÓN | ; proveer para los nuestros (1 Tim. 5:8),  | ; proveer para los nuestros (1 Timoteo 5:8),  |
| RELACIÓN | ; la casa de tu padre (Sal. 45:10-11), humano, esperanzas, metas, ambiciones,  | ; la casa de tu padre (Salmos 45:10-11), humano, esperanzas, metas, ambiciones,  |
| ARREPENTIMIENTO | Dones y llamamientos de Dios afuera (Rom. 11:29),  | Dones y llamamientos de Dios afuera (Romanos 11:29),  |
| ARREPENTIMIENTO | ; imposible de renovar (Heb. 6:4-9),  | ; imposible de renovar (Hebreos 6:4-9),  |
| ARREPENTIMIENTO | ; pecadores llamados a (Mat. 9:13),  | ; pecadores llamados a (Mateo 9:13),  |
| REPROCHES | Discípulos no exentos de lo que cayó sobre el Maestro (Sal. 69:9),  | Discípulos no exentos de lo que cayó sobre el Maestro (Salmos 69:9),  |
| CATÓLICO ROMANO | ; cuerno pequeño (Dan. 8:9),  | ; cuerno pequeño (Daniel 8:9),  |
| CATÓLICO ROMANO | ; ascenso del poder clerical en (Dan. 11:27),  | ; ascenso del poder clerical en (Daniel 11:27),  |
| IMPERIO ROMANO | ; descrito como “rey del norte” (Dan. 11:5-19),  | ; descrito como “rey del norte” (Daniel 11:5-19),  |
| SACRIFICIO | ; “espiritual” (1 Ped. 2:5) omitido en el manuscrito sinaítico,  | ; “espiritual” (1 Pedro 2:5) omitido en el manuscrito sinaítico,  |
| SALVACIÓN | ; no prometido por 1 Tim. 2:4,  | ; no prometido por 1 Timoteo 2:4,  |
| SANTIFICACIÓN | En heb. 10:29 está justificado,  | En Hebreos 10:29 está justificado,  |
| SEMILLA | La iglesia se mezcla con, para formar Babilonia (Dan. 2:43),  | La iglesia se mezcla con, para formar Babilonia (Daniel 2:43),  |
| SEPARADO | ; Isa. 53:2-3 no niega que Jesús existiera,  | ; Isaías 53:2-3 no niega que Jesús existiera,  |
| PLATA | ; respecto a Jam. 5:1-9, | ; respecto a Santiago 5:1-9, |
| PECADO | ; y muerte con respecto a Lam. 2:1,  | ; y muerte con respecto a Lamentaciones 2:1,  |
| OFRENDA POR EL PECADO | La humanidad dibujada tras la Iglesia completa (Jn. 6:44),  | La humanidad dibujada tras la Iglesia completa (Juan 6:44),  |
| HIJO DE DIOS | ; mostrado en Jn. 14:7-10,  | ; mostrado en Juan 14:7-10,  |
| ESPURIO | ; algunas palabras de Jn. 3:13,  | ; algunas palabras de Juan 3:13,  |
| ESTÁNDAR | ; simboliza la verdad divina (Isa. 13:1),  | ; simboliza la verdad divina (Isaías 13:1),  |
| MESA | Por la fe Iglesia sentada junto al Maestro, y él está sirviendo (Lc. 12:37),  | Por la fe Iglesia sentada junto al Maestro, y él está sirviendo (Lucas 12:37),  |
| MESA | ; “Declararlo claro en tablas” (gráficos), (Hab. 2:2),  | ; “Declararlo claro en tablas” (gráficos), (Habacuc 2:2),  |
| MESA | ; dos reyes hablan mentiras a uno (Dan. 11:27),  | ; dos reyes hablan mentiras a uno (Daniel 11:27),  |
| DIENTES | Cuando están nerviosos (Jer. 31:29-30; Eze. 18:2, 4, 30),  | Cuando están nerviosos (Jeremías 31:29-30; Ezequiel 18:2, 4, 30),  |
| DIENTES | ; en el fuego del tiempo de angustia, (Mat. 13:39),  | ; en el fuego del tiempo de angustia, (Mateo 13:39),  |
| JUSTIFICACIÓN TENTATIVA | ; L3; “Por tanto, hermanos, os ruego” son (Ro. 12:1),  | ; L3; “Por tanto, hermanos, os ruego” son (Romanos 12:1),  |
| LADRÓN | El Día del Señor viene como, (1 Tes. 5:4),  | El Día del Señor viene como, (1 Tesalonicenses 5:4),  |
| LADRÓN |  ; amo de casa, sin saber a qué hora, llega (Mat. 24:42),  |  ; amo de casa, sin saber a qué hora, llega (Mateo 24:42),  |
| PENSAMIENTOS | Por encima del hombre (Isa. 55:8-9),  | Por encima del hombre (Isaías 55:8-9),  |
| TIEMPOS | ; “En aquellos días” (Jer. 31:39-34),  | ; “En aquellos días” (Jeremías 31:39-34),  |
| DIEZMOS | ; Leví pagó a Melquisedec (Heb. 7:9-10),  | ; Leví pagó a Melquisedec (Hebreos 7:9-10),  |
| TRADUCCIONES | De 1 Jn. 5:7,  | De 1 Juan 5:7,  |
| TRADUCCIONES | De Fil. 2:6 examinado,  | De Filipenses 2:6 examinado,  |
| ÁRBOLES | ; Memoria de sólo lectura. 11:17, 24,  | ; Romanos 11:17, 24,  |
| ÁRBOLES | ; Antiguo Testamento y Nuevo Testamento (Zac. 4:3),  | ; Antiguo Testamento y Nuevo Testamento (Zacarías 4:3),  |
| ÁRBOLES | ; como cae, así será (Ecl. 11:3),  | ; como cae, así será (Eclesiastés 11:3),  |
| ÁRBOLES |  - 604:1; bahía verde (Sal. 37:35),  |  - 604:1; bahía verde (Salmos 37:35),  |
| TRINIDAD | ; ese Espíritu santo no puede ser una persona como se muestra en Ef. 5:18-20,  | ; ese Espíritu santo no puede ser una persona como se muestra en Efesios 5:18-20,  |
| TROMPETA | SÉPTIMO: Mat. 24:31,  | SÉPTIMO: Mateo 24:31,  |
| TIRO | ; los fuertes de la tierra, Sal. 45:12-17,  | ; los fuertes de la tierra, Salmos 45:12-17,  |
| TIRO | DIOS: Los ha encerrado a todos en, Rom. 11:32,  | DIOS: Los ha encerrado a todos en, Romanos 11:32,  |
| UNIVERSAL | ; aplica mal el apoyo a 1 Tim. 2:4,  | ; aplica mal el apoyo a 1 Timoteo 2:4,  |
| Venganza | ; Zac. 14:6-7, confundido con  | ; Zacarías 14:6-7, confundido con  |
| VELAR | ; Bienaventurados siervos a quienes el Señor encuentre, (Lc. 12:37),  | ; Bienaventurados siervos a quienes el Señor encuentre, (Lucas 12:37),  |
| VELAR | ; cuando llegue el tiempo, lo sabrán (Mc. 13:32-33),  | ; cuando llegue el tiempo, lo sabrán (Marcos 13:32-33),  |
| PALABRA | : Como ocurre en Jn. 1:1 significa “una palabra”,  | : Como ocurre en Juan 1:1 significa “una palabra”,  |
| OBRAS | ; maravilloso, del diablo (Mat. 7:22-23),  | ; maravilloso, del diablo (Mateo 7:22-23),  |

Contextos asociados corregidos: **81**. Detalle en `reporte_contextos_biblicos.csv`.
