# 3. ✏ Zadanie 3 – Licznik połączeń
# Zmodyfikuj echo server tak, aby przy każdym nowym połączeniu wysyłał wiadomość
# "Jesteś klientem numer X", gdzie X to liczba aktywnych połączeń.
# (proste)


from aiohttp import web

connections = 0


async def websocket_handler(request):
    global connections
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    connections += 1

    await ws.send_str(f"Jesteś klientem nr {connections}")

    async for msg in ws:
        await ws.send_str(f"Server: {msg.data}")
        print(f"Otrzymano wiadomość: {msg}")
    return ws


app = web.Application()

app.router.add_get("/ws", websocket_handler)

if __name__ == "__main__":
    print("🚀 Serwer WebSocket działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)