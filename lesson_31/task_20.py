# Timeout dla zadania
# Napisz korutynę, która śpi przez losowy czas od 1 do 5 sekund. Uruchom ją, ale z
# ograniczeniem czasowym na 3 sekundy. Jeśli korutyna nie zakończy się w tym czasie,
# program powinien rzucić wyjątek asyncio.TimeoutError. Obsłuż ten wyjątek i wypisz
# odpowiedni komunikat. Wskazówka: użyj asyncio.wait_for().
import asyncio, random

async def worker():
    sleep_time = random.randint(1,5)
    print(f"Czas wykonania: {sleep_time}")
    await asyncio.sleep(sleep_time)
    
async def main():
    try:
        await asyncio.wait_for(worker(), timeout=3)        
    except asyncio.TimeoutError:
        print("Przeroczony czas wykonania zadania")

asyncio.run(main())