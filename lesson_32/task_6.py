from aiohttp import web


async def handle_echo(request):
    data = await request.json()

    return web.json_response(data)


app = web.Application()
app.router.add_post("/api/echo", handle_echo)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)