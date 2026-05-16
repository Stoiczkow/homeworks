# Timeout dla zadania

# Napisz korutynę, która śpi przez losowy czas od 1 do 5 sekund. Uruchom ją, ale z ograniczeniem czasowym na 3 sekundy. Jeśli korutyna nie zakończy się w tym czasie, program powinien rzucić wyjątek asyncio.TimeoutError. Obsłuż ten wyjątek i wypisz odpowiedni komunikat. Wskazówka: użyj asyncio.wait_for().

import asyncio
import random


async def dlugie_zadanie():
    czas = random.randint(1, 5)
    print(f"Zadanie będzie trwać {czas} sekund")
    await asyncio.sleep(czas)
    print("Zadanie zakończone")


async def main():
    try:
        await asyncio.wait_for(dlugie_zadanie(), timeout=3)
    except asyncio.TimeoutError:
        print("Timeout Zadanie nie zakończyło się w 5 sekund.")


if __name__ == "__main__":
    asyncio.run(main())