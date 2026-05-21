# Napisz korutynę dlugie_obliczenia(), która po losowym czasie (od 2 do 5 sekund) zwraca
# losową liczbę całkowitą (od 1 do 100). Uruchom 10 takich zadań współbieżnie i po
# zakończeniu wszystkich oblicz i wypisz sumę ich wyników.
import asyncio, random


async def dlugie_obliczenia():
    await asyncio.sleep(random.randint(2, 6))
    return random.randint(1, 101)

async def main():
    results = await asyncio.gather(*[
            dlugie_obliczenia() for _ in range(10)
            ])
    
    print(f"Suma wyników z 10 korutyn to: {sum(results)}")
    
asyncio.run(main())