const staticDevCoffee = "ESP-Intervallometer"
const assets = [
    "ESP-Intervallometer//",
    "ESP-Intervallometer//index.html",
    "ESP-Intervallometer//assets/css/bootstrap.min.css",
    "ESP-Intervallometer//assets/css/easings.css",
    "ESP-Intervallometer//assets/css/theme.css",
    "ESP-Intervallometer//assets/js/bootstrap.min.js",
    "ESP-Intervallometer//assets/js/constants.js",
    "ESP-Intervallometer//assets/js/jquery-3.3.1.slim.min.js",
    "ESP-Intervallometer//assets/js/popper.min.js",
    "ESP-Intervallometer//assets/js/script.js",
    "ESP-Intervallometer//assets/js/theme.js",
    "ESP-Intervallometer//assets/icon/icon.svg",
    "ESP-Intervallometer//assets/icon/icon.png"
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
