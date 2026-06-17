from aiohttp import web


async def handle_search(request):
    query = request.query.get("q")

    if query:
        return web.json_response({
            "szukana_fraza": query
        })

    return web.json_response({
        "błąd": "Brak parametru q"
    })


app = web.Application()
app.router.add_get("/api/search", handle_search)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)