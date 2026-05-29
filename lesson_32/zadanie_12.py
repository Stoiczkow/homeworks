"""
Zadanie 12 – Aiohttp Klient – cena Bitcoina
Wymaga: pip install aiohttp
"""
import asyncio
import aiohttp

URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            data = await response.json(content_type=None)
            usd = data['bpi']['USD']['rate']
            czas = data['time']['updated']
            print(f"Cena Bitcoina w USD: {usd}")
            print(f"Zaktualizowano: {czas}")


asyncio.run(main())
