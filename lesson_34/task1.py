# zadanie 1
from aiohttp import web


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        await ws.send_str(f"Server: {msg.data}")

    return ws


app = web.Application()

app.router.add_get("/ws", websocket_handler)

if __name__ == "__main__":
    print("🚀 Serwer WebSocket działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)