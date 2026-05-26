# zadanie 2

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