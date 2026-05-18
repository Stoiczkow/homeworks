# 20. 🧠 Timeout dla zadania
# Napisz korutynę, która śpi przez losowy czas od 1 do 5 sekund. Uruchom ją, ale z
# ograniczeniem czasowym na 3 sekundy. Jeśli korutyna nie zakończy się w tym czasie,
# program powinien rzucić wyjątek asyncio.TimeoutError. Obsłuż ten wyjątek i wypisz
# odpowiedni komunikat. Wskazówka: użyj asyncio.wait_for().
# (challenge)

import asyncio
import random


async def praca():
    time = random.randint(1, 5)
    print(f"Zadanie będzie trwało {time} sekund...")
    await asyncio.sleep(time)
    return "Zakończono"

async def main():
    try:
        wynik = await asyncio.wait_for(praca(), timeout=3)
        print(wynik)

    except asyncio.TimeoutError:
        print("Timeout! Zadanie nie zdążyło się wykonać w 3 sekundy.")

asyncio.run(main())