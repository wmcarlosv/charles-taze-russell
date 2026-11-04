#!/bin/bash
# Sube los cambios del proyecto a GitHub.
# La clave se guarda fuera del repositorio, en ~/.config/charles-taze-russell/token
cd "$(dirname "$0")" || exit 1
exec python3 - <<'PY'
import io
import os
import time
from dulwich import porcelain
from dulwich.repo import Repo

token = open(os.path.expanduser('~/.config/charles-taze-russell/token'), encoding='utf-8').read().strip()
repo = Repo('.')
paths = [p.decode() for p in repo.open_index()]
porcelain.add(repo, paths=paths)
st = porcelain.status(repo)
cambios = any(st.staged[k] for k in ('add', 'modify', 'delete'))
if cambios:
    autor = b'Carlos <wmcarlosv@users.noreply.github.com>'
    mensaje = ('Actualización %s' % time.strftime('%Y-%m-%d %H:%M')).encode()
    cid = porcelain.commit(repo, message=mensaje, author=autor, committer=autor)
    print('commit', cid.decode())
else:
    print('sin cambios que subir')
porcelain.push(repo, 'https://github.com/wmcarlosv/charles-taze-russell.git',
               refspecs=[b'refs/heads/master:refs/heads/main'],
               username='x-access-token', password=token,
               outstream=io.BytesIO(), errstream=io.BytesIO())
print('subido a main')
PY
