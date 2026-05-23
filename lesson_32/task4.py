from aiohttp import web
from datetime import datetime


async def status(request):
    return web.json_response({
        "status": "OK",
        "server_time": datetime.now().isoformat()
    })


app = web.Application()
app.router.add_get("/api/status", status)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)