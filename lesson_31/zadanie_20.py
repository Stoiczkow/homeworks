"""
Zadanie 20 – Timeout dla zadania
asyncio.wait_for() anuluje korutynę, jeśli nie skończy się w 3 sekundy.
"""
import asyncio
import random


async def dluga_operacja():
    czas_snu = random.uniform(1, 5)
    print(f"Operacja będzie trwać {czas_snu:.2f}s...")
    await asyncio.sleep(czas_snu)
    return f"Wynik po {czas_snu:.2f}s"


async def main():
    TIMEOUT = 3.0
    try:
        wynik = await asyncio.wait_for(dluga_operacja(), timeout=TIMEOUT)
        print(f"Sukces: {wynik}")
    except asyncio.TimeoutError:
        print(f"Przekroczono limit czasu ({TIMEOUT}s) – operacja anulowana.")


asyncio.run(main())
