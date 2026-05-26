# Timeout dla zadania
# Napisz korutynę, która śpi przez losowy czas od 1 do 5 sekund. Uruchom ją, ale z
# ograniczeniem czasowym na 3 sekundy. Jeśli korutyna nie zakończy się w tym czasie,
# program powinien rzucić wyjątek asyncio.TimeoutError. Obsłuż ten wyjątek i wypisz
# odpowiedni komunikat. Wskazówka: użyj asyncio.wait_for().

import random
import asyncio

async def random_sleeping():
        await asyncio.sleep(random.randint(1,5))

async def main():
    try:
        await asyncio.wait_for(random_sleeping(), timeout=3)
        print("Zadanie 'random sleeping' wykonane w mniej niż 3s")
    except:
        print("Zadanie 'random sleeping' nie zdążyło się wykonać w ciągu 3s")

asyncio.run(main())