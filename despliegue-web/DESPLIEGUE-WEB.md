# Pastor Russell Library — despliegue web

## 1. Qué hace falta

- Un VPS con Debian/Ubuntu, 1–2 GB de RAM y 5 GB de disco.
- Un dominio apuntando a la IP del VPS.
- Python 3, SQLite y Caddy.

## 2. Copiar la biblioteca

En el VPS:

```bash
sudo mkdir -p /opt/pastor-russell-library
sudo chown carlos:carlos /opt/pastor-russell-library
```

Desde tu equipo:

```bash
rsync -av app.html asistente.py biblioteca.db icono.png \
  carlos@TU_SERVIDOR:/opt/pastor-russell-library/
```

No copies `texto/`, `kjv/` ni los PDFs: el servidor solo necesita
`app.html`, `asistente.py` y `biblioteca.db`.

## 3. Servicio

Copia `pastor-russell.service` a `/etc/systemd/system/` y ejecuta:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now pastor-russell
sudo systemctl status pastor-russell
```

El servidor queda escuchando solo en `127.0.0.1:8100`.

## 4. HTTPS y contraseña

Instala Caddy y copia el `Caddyfile` a `/etc/caddy/Caddyfile`.
Cambia el dominio y genera el hash de la contraseña:

```bash
caddy hash-password
```

Pega el hash en `basicauth` y recarga:

```bash
sudo systemctl reload caddy
```

Abre solo los puertos 80 y 443 en el cortafuegos. **No abras el 8100.**

## 5. DeepL

Crea `/opt/pastor-russell-library/deepl.key` con tu clave.
Si no existe, la biblioteca usa Google Translate como respaldo.

## 6. Copias de seguridad

Copia `biblioteca.db` con:

```bash
sqlite3 biblioteca.db ".backup '/ruta/biblioteca-$(date +%F).db'"
```

No copies la base con `cp` mientras el servidor está escribiendo.

## 7. Comprobación

- `https://TU_DOMINIO/` debe pedir usuario y contraseña.
- El lector, el buscador y la traducción deben funcionar.
- `http://TU_IP:8100` no debe responder desde fuera.
