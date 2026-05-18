# 15. 🧠 Asynchroniczny zapis do pliku
# Napisz program, w którym 5 korutyn współbieżnie generuje jakieś dane tekstowe (np. "Log
# z korutyny X"). Wszystkie powinny zapisywać swoje logi do jednego pliku. Zapewnij, aby
# dostęp do pliku był zsynchronizowany, żeby wpisy się nie pomieszały. Użyj asyncio.Lock
# oraz biblioteki aiofiles (pip install aiofiles).
# (challenge)

import asyncio
import aiofiles

async def dane_tekstowe(nazwa, numer, lock):
    tekst = f"{nazwa} generuje z korutyny {numer}\n"

    async with lock:
        async with aiofiles.open("logi.txt", mode="a") as file:
            await file.write(tekst)

    

async def main():
    lock = asyncio.Lock()

    tasks = asyncio.gather(
        dane_tekstowe("Log", 1, lock),
        dane_tekstowe("Log", 2, lock),
        dane_tekstowe("Log", 3, lock),
        dane_tekstowe("Log", 4, lock),
        dane_tekstowe("Log", 5, lock)
    )
    await tasks

asyncio.run(main())