from aiohttp import web


async def echo(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response(
            {"błąd"},
            status=400
        )

    return web.json_response(data)


app = web.Application()
app.router.add_post("/api/echo", echo)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)