from aiohttp import web
import asyncio
import time


clients = {}


async def ping_client(ws):
    while True:
        await asyncio.sleep(30)

        # jeśli klient nie odpowiedział  60s
        last_pong = clients.get(ws, 0)

        if time.time() - last_pong > 60:
            print("Klient nie odpowiedział - Rozłączanie")
            await ws.close()
            break

        try:
            print("Wysyła ping")
            await ws.send_str("ping")

        except Exception as e:
            print("Błąd:", e)
            break


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    print("Klient połączony")

    clients[ws] = time.time()

    # uruchomienie taska pingującego
    ping_task = asyncio.create_task(ping_client(ws))

    try:
        async for msg in ws:

            if msg.type == web.WSMsgType.TEXT:
                print("Odebrano:", msg.data)

                if msg.data == "pong":
                    clients[ws] = time.time()
                    print("Otrzymano")

    finally:
        ping_task.cancel()

        if ws in clients:
            del clients[ws]

        print("Klient rozłączony")

    return ws


app = web.Application()
app.router.add_get("/ws", websocket_handler)

web.run_app(app, port=8080)