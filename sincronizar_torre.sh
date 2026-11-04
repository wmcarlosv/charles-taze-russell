#!/bin/bash
# Copia a la biblioteca española los números que ya estén traducidos.
cd /home/carlos/Programas/pastor-russell-library || exit 1
while true; do
  n=$(python3 -c "import sqlite3;print(sqlite3.connect('biblioteca.db').execute('select count(*) from torre_es').fetchone()[0])")
  if [ "$n" -ge 432 ]; then break; fi
  python3 insertar_torre_es.py >> sincronizacion.log 2>&1
  sleep 300
done
python3 insertar_torre_es.py >> sincronizacion.log 2>&1
echo "sincronización terminada $(date)" >> sincronizacion.log
