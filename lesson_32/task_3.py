from aiohttp import web


async def handle_home(request):
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html"
    )


async def handle_greeting(request):
    imie = request.match_info.get("imie", "Gość")

    return web.Response(
        text=f"Witaj, {imie}!",
        content_type="text/html"
    )


app = web.Application()
app.router.add_get("/", handle_home)
app.router.add_get("/witaj/{imie}", handle_greeting)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)