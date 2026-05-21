# 12. (Challenge) Aiohttp Klient - Publiczne API: Aiohttp to także klient! Napisz osobny
# skrypt .py (nie serwer), który w korutynie main :
# 1. Stworzy aiohttp.ClientSession() .
# 2. Wykona zapytanie GET na publiczne API:
# https://api.coindesk.com/v1/bpi/currentprice.json .
# 3. Pobierze odpowiedź JSON ( await response.json() ).
# 4. Wypisze w konsoli cenę Bitcoina w USD.
# Hint: Użyj async with aiohttp.ClientSession() as session: async with session.get(url) as
# response:

# 13. (Challenge) Aiohttp Klient - Gather: Rozbuduj zadanie 12. Napisz korutynę
# fetch(session, url) , która pobiera dane. W main stwórz listę 3 różnych URL-i (np. z
# https://api.publicapis.org/random?auth=null - wywołaj 3 razy) i użyj
# asyncio.gather , aby pobrać je wszystkie jednocześnie

import asyncio

import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()
    
async def main():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    urls = [
        "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
        "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT",
        "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
    ]
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            
            price = float(data["price"])
            print(f"Cena Bitcoina w USD: {price:.2f}")
            
        results = await asyncio.gather(
            *(fetch(session, url) for url in urls)
        )
        print("Pobrane dane:")
        for result in results:
            print(result)

asyncio.run(main())