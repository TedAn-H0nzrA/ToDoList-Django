const CACHE_NAME = "todo-cache-v1";
const urlsToCache = [
  "/",
  "/Static/Icons/list.svg",
  "/Static/Icons/list.svg",
];

self.addEventListener("install", function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
    .then(function(cache) {
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener("fetch", function(event) {
  event.respondWith(
    caches.match(event.request)
    .then(function(response) {
      return response || fetch(event.request);
    })
  );
});
