from aiohttp import web


async def handle_search(request: web.Request) -> web.Response:
    q = request.query.get("q")
    if q is None:
        return web.json_response({"błąd": "Brak parametru q"}, status=400)
    return web.json_response({"szukana_fraza": q})


app = web.Application()
app.router.add_get("/api/search", handle_search)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)