const staticDevCoffee = "ESP-Intervallometer"
const assets = [
    "/",
    "index.html",
    "assets/css/bootstrap.min.css",
    "assets/css/easings.css",
    "assets/css/theme.css",
    "assets/js/bootstrap.min.js",
    "assets/js/constants.js",
    "assets/js/jquery-3.3.1.slim.min.js",
    "assets/js/popper.min.js",
    "assets/js/script.js",
    "assets/js/theme.js",
    "assets/icon/icon.svg",
    "assets/icon/icon.png"
]

self.addEventListener("install", installEvent => {
    installEvent.waitUntil(
        caches.open(staticDevCoffee).then(cache => {
            cache.addAll(assets)
        })
    )
})

self.addEventListener("fetch", fetchEvent => {
    fetchEvent.respondWith(
        caches.match(fetchEvent.request).then(res => {
            return res || fetch(fetchEvent.request)
        })
    )
})
