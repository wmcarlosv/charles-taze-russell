#!/bin/bash
# Copia de seguridad diaria de la base de la biblioteca.
set -e
DEST="${BIBLIOTECA_BACKUP_DIR:-$HOME/Copias/Biblioteca}"
mkdir -p "$DEST"
python3 - "$DEST" <<'PY'
import datetime, glob, gzip, os, shutil, sqlite3, sys
db = os.path.join(os.environ.get('BIBLIOTECA_DIR', '/home/carlos/Programas/biblioteca-ia'), 'biblioteca.db')
dest = sys.argv[1]
con = sqlite3.connect(db)
con.execute('PRAGMA wal_checkpoint(TRUNCATE)')
con.close()
stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M')
out = os.path.join(dest, 'biblioteca-%s.db.gz' % stamp)
tmp = out + '.part'
with open(db, 'rb') as f, gzip.open(tmp, 'wb', compresslevel=9) as g:
    shutil.copyfileobj(f, g)
os.replace(tmp, out)
files = sorted(glob.glob(os.path.join(dest, 'biblioteca-*.db.gz')))
for f in files[:-14]:
    try:
        os.remove(f)
    except OSError:
        pass
print(out)
PY
