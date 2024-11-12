
const CACHE_NAME = 'my-app-cache-v1';
const urlsToCache = [
    '/index.html',
    '/website/pages/license.html',
    '/website/pages/license.html',
    '/website/pages/contributor.html',
    '/website/styles/style.css',
    '/website/styles/contributor.css',
    '/script.js',
    '/software/images/icon-192x192.png',
    '/software/images/icon-512x512.png'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
    );
});
