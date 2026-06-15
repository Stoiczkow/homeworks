"""
Stwórz prosty serwer aiohttp, który na ścieżce "/" zwróci stronę HTML:
<h1>Witaj na mojej stronie!</h1>
z poprawnym content_type='text/html'.
"""

from aiohttp import web

async def witaj(request):
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html"
    )

def main():
    app = web.Application()
    app.router.add_get("/", witaj)

    web.run_app(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()
