from aiohttp import web


async def index(request):
    return web.Response(
        text="<h1>Witaj na stronie</h1>",
        content_type="text/html"
    )


app = web.Application()
app.router.add_get("/", index)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)