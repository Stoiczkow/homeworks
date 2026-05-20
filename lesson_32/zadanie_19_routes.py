from datetime import datetime

from aiohttp import web


async def handle_index(request: web.Request) -> web.Response:
    return web.Response(text="<h1>Strona główna</h1>", content_type="text/html")


async def handle_status(request: web.Request) -> web.Response:
    return web.json_response({
        "status": "OK",
        "server_time": datetime.now().isoformat(),
    })


async def handle_witaj(request: web.Request) -> web.Response:
    imie = request.match_info["imie"]
    return web.Response(text=f"Witaj, {imie}!")


def setup_routes(app: web.Application) -> None:
    app.router.add_get("/", handle_index)
    app.router.add_get("/api/status", handle_status)
    app.router.add_get("/witaj/{imie}", handle_witaj)