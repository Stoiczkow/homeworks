from aiohttp import web
import asyncio
from typing import Set


# Globalny zbiór wszystkich aktywnych połączeń
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


async def chat_handler(request):
    """
    Handler obsługujący chat room przez WebSocket.
    Każdy klient może wysyłać wiadomości, które są rozesłane do wszystkich.
    """
    # Tworzymy nowe połączenie WebSocket
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    # Dodajemy połączenie do aktywnych
    active_connections.add(ws)
    print(f"✅ Nowy klient! Łącznie połączeń: {len(active_connections)}")

    # Powiadamiamy wszystkich o nowym użytkowniku
    await broadcast_message(
        f"🟢 Nowy użytkownik dołączył! Aktywnych: {len(active_connections)}",
        sender=ws
    )

    try:
        # Pętla nasłuchiwania wiadomości od tego klienta
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                user_message = msg.data
                print(f"💬 Wiadomość: {user_message}")

                # Rozesłanie wiadomości do wszystkich
                await broadcast_message(f"💬 Użytkownik: {user_message}")

            elif msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd WebSocket: {ws.exception()}")

    finally:
        # Usuwamy połączenie z aktywnych (klient się rozłączył)
        active_connections.discard(ws)
        print(f"❌ Klient rozłączony. Zostało: {len(active_connections)}")

        # Powiadamiamy pozostałych
        await broadcast_message(
            f"🔴 Użytkownik opuścił chat. Aktywnych: {len(active_connections)}"
        )

    return ws


# Aplikacja
app = web.Application()
app.router.add_get('/chat', chat_handler)

if __name__ == '__main__':
    print("🚀 Chat server działa na ws://localhost:8080/chat")
    web.run_app(app, host='localhost', port=8080)