#!/bin/bash
cd "$(dirname "$0")"
PERFIL="$HOME/.config/pastor-russell-chrome"
if ! (exec 3<>/dev/tcp/127.0.0.1/8100) 2>/dev/null; then
  nohup python3 asistente.py >> servidor.log 2>&1 &
  for i in $(seq 1 40); do
    (exec 3<>/dev/tcp/127.0.0.1/8100) 2>/dev/null && break
    sleep 0.25
  done
fi
exec google-chrome-stable --app=http://127.0.0.1:8100/ \
  --window-size=1280,900 --start-maximized \
  --class=PastorRussellLibrary --user-data-dir="$PERFIL" --no-first-run \
  --no-default-browser-check --disable-extensions --disable-sync \
  --disable-background-networking --disable-component-update
