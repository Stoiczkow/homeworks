import asyncio

import aiohttp

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            response.raise_for_status()
            data = await response.json(content_type=None)
    cena_usd = data["bpi"]["USD"]["rate"]
    print(f"Cena Bitcoina (USD): {cena_usd}")


if __name__ == "__main__":
    asyncio.run(main())