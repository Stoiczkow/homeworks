import asyncio
import time

import aiohttp

URL = "https://api.publicapis.org/random?auth=null"


async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json(content_type=None)


async def main() -> None:
    start = time.time()
    async with aiohttp.ClientSession() as session:
        wyniki = await asyncio.gather(
            fetch(session, URL),
            fetch(session, URL),
            fetch(session, URL),
        )
    for i, w in enumerate(wyniki, 1):
        print(f"--- Wynik {i} ---")
        print(w)
    print(f"\nCzas: {time.time() - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())