"""
Stwórz handler /api/search, który odczyta z request.query parametr q.
Jeśli istnieje — zwróć {"szukana_fraza": "wartosc_q"}.
Jeśli nie — zwróć {"błąd": "Brak parametru q"}.
"""

from aiohttp import web

async def search_handler(request):
    q = request.query.get("q")

    if q:
        return web.json_response({"szukana_fraza": q})
    else:
        return web.json_response({"błąd": "Brak parametru q"})

def main():
    app = web.Application()
    app.router.add_get("/api/search", search_handler)

    web.run_app(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()
