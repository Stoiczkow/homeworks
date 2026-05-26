from aiohttp import web
import asyncio


async def websocket_handler(request):
    """
    Handler obsługujący połączenia WebSocket.
    Tworzy echo server - zwraca każdą otrzymaną wiadomość z powrotem.
    """
    # Przygotowanie połączenia WebSocket
    ws = web.WebSocketResponse()

    # Wykonanie handshake (upgrade z HTTP do WebSocket)
    await ws.prepare(request)

    print("✅ Nowy klient połączony!")

    # Pętla nasłuchiwania wiadomości
    async for msg in ws:
        # msg.type zawiera typ wiadomości (TEXT, BINARY, CLOSE, etc.)
        if msg.type == web.WSMsgType.TEXT:
            # Otrzymaliśmy wiadomość tekstową
            print(f"📥 Otrzymano: {msg.data}")

            # Odsyłamy echo z powrotem
            await ws.send_str(f"Echo: {msg.data}")

        elif msg.type == web.WSMsgType.ERROR:
            # Wystąpił błąd połączenia
            print(f"❌ Błąd WebSocket: {ws.exception()}")

    print("❌ Klient rozłączony")
    return ws


# Tworzenie aplikacji aiohttp
app = web.Application()

# Rejestracja route'a dla WebSocket
app.router.add_get('/ws', websocket_handler)

# Uruchomienie serwera
if __name__ == '__main__':
    print("🚀 Serwer WebSocket działa na ws://localhost:8080/ws")
    web.run_app(app, host='localhost', port=8080)

# Jak przetestować w przeglądarce (Console):
# const ws = new WebSocket('ws://localhost:8080/ws');
# ws.onmessage = (e) => console.log(e.data);
# ws.send('Cześć!');