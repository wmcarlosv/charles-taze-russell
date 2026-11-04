#!/bin/bash
cd "$(dirname "$0")"
PERFIL="$HOME/.config/biblioteca-ia-chrome"

# voces del sistema para el botón «Escuchar»
systemctl --user start speech-dispatcher >/dev/null 2>&1 || true

# servidor local (si no está ya en marcha)
if ! (exec 3<>/dev/tcp/127.0.0.1/8099) 2>/dev/null; then
  # Preferir el servicio del sistema (arranque automático y reinicio)
  systemctl --user start biblioteca.service >/dev/null 2>&1 || true
  for i in $(seq 1 40); do
    (exec 3<>/dev/tcp/127.0.0.1/8099) 2>/dev/null && break
    sleep 0.25
  done
  # Si el servicio no está disponible, arrancar de la forma tradicional
  if ! (exec 3<>/dev/tcp/127.0.0.1/8099) 2>/dev/null; then
    nohup python3 asistente.py >> servidor.log 2>&1 &
    for i in $(seq 1 40); do
      (exec 3<>/dev/tcp/127.0.0.1/8099) 2>/dev/null && break
      sleep 0.25
    done
  fi
fi

# tamaño útil de la pantalla (descontando el panel del escritorio)
GEO=$(xprop -root _NET_WORKAREA 2>/dev/null | sed 's/.*= //' | awk -F', *' '{print $1, $2, $3, $4}')
set -- $GEO
WX=${1:-0}; WY=${2:-0}; WW=${3:-1280}; WH=${4:-720}

exec google-chrome-stable --app=http://127.0.0.1:8099/ \
  --window-size="$WW,$WH" --window-position="$WX,$WY" --start-maximized \
  --class=BibliotecaBiblica --user-data-dir="$PERFIL" --no-first-run --no-default-browser-check \
  --disable-extensions --disable-sync --disable-background-networking --disable-component-update \
  --disable-default-apps --disable-features=Translate,MediaRouter,OptimizationHints,DialMediaRouteProvider
