const CACHE = 'biblioteca-v12';
const SHELL = ['/', '/russell-icono.png', '/manifest.json'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).catch(()=>{}));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))));
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.origin !== location.origin) return;

  // la aplicación siempre se pide a la red (y se guarda para uso sin conexión)
  if (u.pathname === '/' || u.pathname === '/index.html' || u.pathname === '/tutorial') {
    e.respondWith(
      fetch(e.request).then(r => {
        const cp = r.clone();
        caches.open(CACHE).then(c => c.put(e.request, cp));
        return r;
      }).catch(() => caches.match(e.request).then(r => r || caches.match('/')))
    );
    return;
  }

  // datos del maná diario: red primero, caché si no hay conexión
  if (u.pathname.startsWith('/mana/')) {
    e.respondWith(
      fetch(e.request).then(r => {
        const cp = r.clone();
        caches.open(CACHE).then(c => c.put(e.request, cp));
        return r;
      }).catch(() => caches.match(e.request))
    );
    return;
  }

  // lecturas de la biblioteca: red primero, caché si no hay conexión
  if (u.pathname.startsWith('/api/')) {
    const cacheable = ['/api/pagina','/api/tema','/api/versiculo','/api/obras','/api/estado','/api/indice',
                       '/api/biblia','/api/biblia/capitulo','/api/biblia/comentarios'].some(p => u.pathname === p);
    if (!cacheable) return;
    e.respondWith(
      fetch(e.request).then(r => {
        const cp = r.clone();
        caches.open(CACHE).then(c => c.put(e.request, cp));
        return r;
      }).catch(() => caches.match(e.request))
    );
    return;
  }

  // el audio se sirve con Range y no debe guardarse en la caché del service worker
  if (u.pathname.startsWith('/audio/')) return;

  // estáticos: caché primero
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request).then(resp => {
      if (resp.ok) { const cp = resp.clone(); caches.open(CACHE).then(c => c.put(e.request, cp)); }
      return resp;
    }).catch(() => caches.match('/')))
  );
});
