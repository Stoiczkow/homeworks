# 4. ✏ (Proste) Aiohttp - Proste API JSON: Stwórz handler na ścieżce /api/status , który
# metodą GET zwróci odpowiedź JSON: {"status": "OK", "server_time": "..."} (użyj
# datetime.now() do czasu i web.json_response ).

from aiohttp import web
from datetime import datetime

async def status(request):
    return web.json_response(
        {
            "status": "ok",
            "server_time": str(datetime.now())
        }
    )

app = web.Application()

app.router.add_get("/api/status", status)


if __name__ == "__main__":
    print("Uruchamiam serwer na [http://127.0.0.1:8080] (http://127.0.0.1:8080)")
    web.run_app(app, host="127.0.0.1", port=8080)