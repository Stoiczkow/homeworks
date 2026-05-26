# zadanie 8
from aiohttp import web
import time

connections = 0


async def websocket_handler(request):
    global connections
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    connections += 1

    conection_start = time.time()

    await ws.send_str(f"Jesteś klientem nr {connections}")

    async for msg in ws:
        await ws.send_str(f"Server: {msg.data}")
        print(f"Otrzymano wiadomość: {msg}")

    connection_end = time.time()
    print(f"Klient był połączony {connection_end - conection_start}")
    return ws


app = web.Application()

app.router.add_get("/ws", websocket_handler)

if __name__ == "__main__":
    print("🚀 Serwer WebSocket działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)