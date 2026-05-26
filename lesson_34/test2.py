from aiohttp import web


async def advanced_handler(request):
    """
    Obsługa różnych typów wiadomości WebSocket
    """
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:

        # 1. Wiadomość tekstowa (najczęstszy typ)
        if msg.type == web.WSMsgType.TEXT:
            data = msg.data  # str
            await ws.send_str(f"Otrzymałem tekst: {data}")

        # 2. Wiadomość binarna (np. pliki, obrazy)
        elif msg.type == web.WSMsgType.BINARY:
            data = msg.data  # bytes
            await ws.send_bytes(data)  # Echo binarny

        # 3. Zamknięcie połączenia
        elif msg.type == web.WSMsgType.CLOSE:
            print("Klient zamyka połączenie")
            break

        # 4. Błąd
        elif msg.type == web.WSMsgType.ERROR:
            print(f"Błąd: {ws.exception()}")

    return ws


# Tip: JSON przez WebSocket
# Najczęściej wysyłamy dane w formacie JSON jako tekst.
# Możesz użyć ws.send_json(dict) i ws.receive_json() do automatycznej
# serializacji/deserializacji.

# Warning: Pamięć o zamykaniu połączeń
# Zawsze dodawaj obsługę rozłączenia klienta (try-finally)
# i usuwaj połączenie ze zbioru aktywnych. Inaczej możesz mieć memory leak!
app = web.Application()
app.router.add_get("/ws", advanced_handler)

if __name__ == "__main__":
    print("🚀 Chat server działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)