import aiohttp
import asyncio

# podany w zadaniu endpoint już nie istnieje, dlatego użyłem inny

async def main():
    client = aiohttp.ClientSession("https://official-joke-api.appspot.com/")

    async with client as session:
        async with session.get("random_joke") as response:
            info = await response.json()     
            print(f'Joke for today: {info.get("setup")} - {info.get("punchline")}')

asyncio.run(main())