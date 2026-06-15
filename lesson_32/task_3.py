"""
Rozbuduj serwer aiohttp. Dodaj handler na ścieżce /witaj/{imie},
który odczyta imię z request.match_info i zwróci tekst:
"Witaj, {imie}!"
"""

from aiohttp import web

async def witaj_strona(request):
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html"
    )

async def witaj_dynamicznie(request):
    imie = request.match_info.get("imie", "nieznajomy")
    return web.Response(text=f"Witaj, {imie}!")

def main():
    app = web.Application()
    app.router.add_get("/", witaj_strona)
    app.router.add_get("/witaj/{imie}", witaj_dynamicznie)

    web.run_app(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()
