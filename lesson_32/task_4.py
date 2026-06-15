"""
Stwórz handler aiohttp na ścieżce /api/status, który metodą GET zwróci JSON:
{"status": "OK", "server_time": "..."}.
Użyj datetime.now() oraz web.json_response.
"""

from datetime import datetime

from aiohttp import web

async def status_api(request):
    return web.json_response({"status": "success", "server_time": datetime.now().isoformat()})

def main():
    app = web.Application()
    app.router.add_get("/api/status", status_api)

    web.run_app(app, host="127.0.0.1", port=8000)


if __name__ == '__main__':
    main()