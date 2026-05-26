# 11. ✏ Zadanie 11 – WebSocket Ping-Pong
# Zaimplementuj mechanizm ping-pong: co 30 sekund serwer wysyła "ping", klient musi
# odpowiedzieć "pong". Jeśli brak odpowiedzi przez 60s, rozłącz klienta.
# (średnie)

from aiohttp import web
import asyncio
import time
from typing import Set


active_connections: Set[web.WebSocketResponse] = set()



async def ping_loop(ws):
    """
    Co 30 sekund wysyła ping do klienta.
    Jeśli klient nie odpowie pong przez 60 sekund,
    połączenie zostaje zamknięte.
    """

    try:
        while True:

            await ws.send_str("ping")
            print("Ping")

            await asyncio.sleep(30)

            if time.time() - ws.last_pong > 60:
                print("User nie odpowiedział pong")
                await ws.close(
                    message=b"Brak pong"
                )
                break

    except asyncio.CancelledError:
        pass


async def websocket_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    active_connections.add(ws)

    print("Klient połączony")

    ws.last_pong = time.time()
  
    ping_task = asyncio.create_task(
        ping_loop(ws)
    )

    try:
        async for msg in ws:

            if msg.type == web.WSMsgType.TEXT:

                print(f"Otrzymano: {msg.data}")

                # klient odpowiedział pong
                if msg.data == "pong":

                    ws.last_pong = time.time()

                    print("Otrzymano Pong")

                else:
                    await ws.send_str(
                        f"Echo: {msg.data}"
                    )

            elif msg.type == web.WSMsgType.ERROR:

                print(f"Błąd: {ws.exception()}")

    finally:

        ping_task.cancel()

        active_connections.discard(ws)

        print("Klient rozłączony")

    return ws


app = web.Application()

app.router.add_get(
    "/ws",
    websocket_handler
)


if __name__ == "__main__":

    print("🚀 WebSocket server: ws://localhost:8080/ws")

    web.run_app(
        app,
        host="localhost",
        port=8080
    )