from aiohttp import web


async def search(request):
    q = request.query.get("q")

    if q:
        return web.json_response({
            "szukana_fraza": q
        })

    return web.json_response({
        "błąd": "Brak parametru "
    })


app = web.Application()
app.router.add_get("/api/search", search)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)