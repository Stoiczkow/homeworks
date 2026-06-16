import asyncio
import time
# 2. ✏️ Asynchroniczny licznik
# Napisz korutynę licznik(n), która przyjmuje liczbę n i co sekundę wypisuje kolejne liczby od 1 do n. Użyj asyncio.sleep(1).

async def licznik(n):
    for i in range(n):
        print(f"{i}")
        await asyncio.sleep(1)

asyncio.run(licznik(7))