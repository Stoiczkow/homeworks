# zadanie 9
from aiohttp import web
from typing import Set

active_connections: Set[web.WebSocketResponse] = set()


async def broadcast_message(message: str, sender: web.WebSocketResponse = None):
    """
    Funkcja wysyłająca wiadomość do wszystkich podłączonych klientów.

    Args:
        message: Wiadomość do rozesłania
        sender: Połączenie, które wysłało wiadomość (opcjonalnie)
    """
    # Iterujemy po wszystkich aktywnych połączeniach
    for connection in active_connections:
        # Opcjonalnie pomijamy nadawcę
        if connection != sender and not connection.closed:
            try:
                await connection.send_str(message)
            except Exception as e:
                print(f"❌ Błąd wysyłania do klienta: {e}")


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    active_connections.add(ws)

    nick = None

    await ws.send_str(f"Jesteś klientem nr {len(active_connections)}")

    async for msg in ws:
        if nick:
            await broadcast_message(f"{nick}: {msg.data}")

        if not nick:
            nick = msg.data

        # await ws.send_str(f"Server: {msg.data}")
        print(f"Otrzymano wiadomość: {msg}")

    return ws


app = web.Application()

app.router.add_get("/ws", websocket_handler)

if __name__ == "__main__":
    print("🚀 Serwer WebSocket działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)