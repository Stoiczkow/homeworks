from aiohttp import web

async def witaj_dynamicznie(request):
    imie = request.match_info.get("imie", "nieznajomy")

    if imie == "admin":
        raise web.HTTPForbidden(text="Dostęp dla admina zabroniony")

    return web.Response(text=f"Witaj, {imie}!")


def main():
    app = web.Application()
    app.router.add_get("/witaj/{imie}", witaj_dynamicznie)
    web.run_app(app, host="127.0.0.1", port=8000)
