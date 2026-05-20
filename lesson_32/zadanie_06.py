import json
from aiohttp import web


async def handle_echo(request: web.Request) -> web.Response:
    try:
        data = await request.json()
    except json.JSONDecodeError:
        raise web.HTTPBadRequest(text="Niepoprawny format JSON")
    return web.json_response(data)


app = web.Application()
app.router.add_post("/api/echo", handle_echo)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)