"""
Zadanie 13 – Aiohttp Klient – asyncio.gather dla wielu URL-i
3 publiczne endpointy pobierane jednocześnie.
"""
import asyncio
import aiohttp

URLS = [
    'https://api.coindesk.com/v1/bpi/currentprice.json',
    'https://httpbin.org/get',
    'https://jsonplaceholder.typicode.com/todos/1',
]


async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        data = await response.json(content_type=None)
        print(f"  [{response.status}] {url}")
        return data


async def main():
    async with aiohttp.ClientSession() as session:
        wyniki = await asyncio.gather(*[fetch(session, url) for url in URLS])

    print(f"\nPobrano {len(wyniki)} zasobów jednocześnie.")


asyncio.run(main())
