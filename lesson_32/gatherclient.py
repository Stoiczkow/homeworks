import aiohttp
import asyncio

# podany w zadaniu endpoint już nie istnieje, dlatego użyłem inny

async def fetch(session, url):
    async with session.get(url) as response:
        try:
            info = await response.json()  
        except:
            try:
                info = await response.text()
            except:
                print("Nie udało się pobrać danych")
                return
            
        print(f"{info}\n\n")

async def main():
    async with aiohttp.ClientSession() as client:
        tasks_to_run = [
        fetch(client, "https://blockchain.info/q/latesthash"),
        fetch(client, "https://official-joke-api.appspot.com/random_joke"),
        fetch(client, "https://randomuser.me/api/")
        ]
        await asyncio.gather(*tasks_to_run)

asyncio.run(main())