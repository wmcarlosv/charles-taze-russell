#!/usr/bin/env python3
"""Sube los archivos grandes (audio) como adjuntos de una publicación de GitHub.

GitHub no admite archivos de más de 100 MB en el repositorio, pero sí
adjuntos de hasta 2 GB en una release. Este script crea la release
`audio-v1` y sube las dos partes del audio. Se puede volver a ejecutar:
las partes ya subidas se omiten.
"""
import http.client
import json
import os
import sys
import time
import urllib.parse
import urllib.request

DUEÑO = 'wmcarlosv'
REPO = 'charles-taze-russell'
ETIQUETA = 'audio-v1'
TOKEN = open(os.path.expanduser('~/.config/charles-taze-russell/token'), encoding='utf-8').read().strip()
CABECERAS = {'Authorization': 'Bearer ' + TOKEN,
             'Accept': 'application/vnd.github+json',
             'Content-Type': 'application/json',
             'User-Agent': 'pastor-russell-library'}


def api(ruta, metodo='GET', cuerpo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo else None
    req = urllib.request.Request('https://api.github.com' + ruta, data=datos,
                                 method=metodo, headers=CABECERAS)
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def release():
    try:
        return api('/repos/%s/%s/releases/tags/%s' % (DUEÑO, REPO, ETIQUETA))
    except Exception:
        return api('/repos/%s/%s/releases' % (DUEÑO, REPO), 'POST', {
            'tag_name': ETIQUETA,
            'name': 'Audio narrado — 2,9 GB',
            'body': 'Audio de la biblioteca española (1189 archivos MP3).\n\n'
                    'Descarga las dos partes y descomprímelas dentro de la carpeta '
                    '`biblioteca-espanola/`:\n\n'
                    '```bash\ntar -xf audio-parte1.tar\ntar -xf audio-parte2.tar\n```',
        })


def subir(rel, ruta):
    nombre = os.path.basename(ruta)
    tam = os.path.getsize(ruta)
    for a in api('/repos/%s/%s/releases/%d/assets' % (DUEÑO, REPO, rel['id'])):
        if a['name'] == nombre and a.get('size') == tam:
            print('ya está', nombre, flush=True)
            return
    print('subiendo %s (%.1f GB)…' % (nombre, tam / 1e9), flush=True)
    con = http.client.HTTPSConnection('uploads.github.com', timeout=7200)
    con.putrequest('POST', '/repos/%s/%s/releases/%d/assets?name=%s'
                   % (DUEÑO, REPO, rel['id'], urllib.parse.quote(nombre)))
    con.putheader('Authorization', 'Bearer ' + TOKEN)
    con.putheader('Content-Type', 'application/octet-stream')
    con.putheader('Content-Length', str(tam))
    con.putheader('Accept', 'application/vnd.github+json')
    con.putheader('User-Agent', 'pastor-russell-library')
    con.endheaders()
    enviado = 0
    ultimo = 0
    with open(ruta, 'rb') as f:
        while True:
            trozo = f.read(1024 * 1024)
            if not trozo:
                break
            con.send(trozo)
            enviado += len(trozo)
            if enviado - ultimo >= 200 * 1024 * 1024:
                ultimo = enviado
                print('  %.1f GB de %.1f GB' % (enviado / 1e9, tam / 1e9), flush=True)
    r = con.getresponse()
    cuerpo = r.read().decode('utf-8', 'replace')
    con.close()
    print('respuesta', r.status, cuerpo[:160], flush=True)
    if r.status >= 300:
        raise SystemExit('fallo al subir %s' % nombre)


def main():
    rel = release()
    print('release', rel['html_url'], flush=True)
    for ruta in sys.argv[1:]:
        subir(rel, ruta)
    print('terminado', flush=True)


if __name__ == '__main__':
    main()
