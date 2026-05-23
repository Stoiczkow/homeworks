from aiohttp import web


async def index(request):
    return web.Response(
        text="<h1>Strona główna</h1>",
        content_type="text/html"
    )


async def witaj(request):
    imie = request.match_info.get("imie")

    # blokada dla admina
    if imie == "admin":
        raise web.HTTPForbidden(text="Dostęp dla admina zabroniony")

    return web.Response(
        text=f"Witaj, {imie}!",
        content_type="text/plain"
    )


app = web.Application()
app.router.add_get("/", index)
app.router.add_get("/witaj/{imie}", witaj)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)