# 2. ✏ Zadanie 2 – Klient wysyłający 3 wiadomości
# Napisz klienta WebSocket, który łączy się z serwerem i wysyła 3 wiadomości: "Cześć", "Jak
# się masz?", "Do widzenia".
# (proste)


from aiohttp import ClientSession
import asyncio


async def main():
    async with ClientSession() as session:
        async with session.ws_connect("ws://localhost:8080/ws") as ws:

            MESSAGES = ["Cześć", "Jak się masz?", "Do widzenia"]

            for msg in MESSAGES:
                await ws.send_str(msg)
                await asyncio.sleep(1)


asyncio.run(main())