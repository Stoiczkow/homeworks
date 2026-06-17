import asyncio
import aiohttp


async def main():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                text = await response.text()
                print(f"Błąd API. Status: {response.status}")
                print(text[:500])
                return

            data = await response.json()

            bitcoin_price_usd = data["bpi"]["USD"]["rate"]

            print(f"Cena Bitcoina w USD: {bitcoin_price_usd}")


if __name__ == "__main__":
    asyncio.run(main())