import asyncio
import time

async def licznik(n):
    for i in range(n):
        print(f"{i}")
        await asyncio.sleep(1)

asyncio.run(licznik(7))