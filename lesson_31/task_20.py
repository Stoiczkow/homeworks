import asyncio
import random


async def losowa_praca():
    czas = random.randint(1, 5)
    print(f"Zadanie będzie trwało {czas} sekund.")

    await asyncio.sleep(czas)

    return f"Zadanie zakończone po {czas} sekundach."


async def main():
    try:
        wynik = await asyncio.wait_for(losowa_praca(), timeout=3)
        print(wynik)

    except asyncio.TimeoutError:
        print("Zadanie przekroczyło limit czasu 3 sekund.")


asyncio.run(main())