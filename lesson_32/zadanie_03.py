from aiohttp import web


async def handle_index(request: web.Request) -> web.Response:
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html",
    )


async def handle_witaj(request: web.Request) -> web.Response:
    imie = request.match_info["imie"]
    return web.Response(text=f"Witaj, {imie}!")


app = web.Application()
app.router.add_get("/", handle_index)
app.router.add_get("/witaj/{imie}", handle_witaj)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)