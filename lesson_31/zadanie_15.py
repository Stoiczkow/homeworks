"""
Zadanie 15 – Asynchroniczny zapis do pliku
5 korutyn współbieżnie zapisuje logi do jednego pliku.
asyncio.Lock zapobiega pomieszaniu się wpisów.
Wymaga: pip install aiofiles
"""
import asyncio
import aiofiles

PLIK_LOG = 'async_logs.txt'
lock = asyncio.Lock()


async def generuj_log(numer):
    await asyncio.sleep(numer * 0.3)  # różne opóźnienia
    wpis = f"Log z korutyny {numer}\n"
    async with lock:
        async with aiofiles.open(PLIK_LOG, 'a', encoding='utf-8') as f:
            await f.write(wpis)
    print(f"Korutyna {numer} zapisała log.")


async def main():
    # Wyczyść plik przed uruchomieniem
    async with aiofiles.open(PLIK_LOG, 'w', encoding='utf-8') as f:
        await f.write('')

    await asyncio.gather(*[generuj_log(i) for i in range(1, 6)])

    print(f"\nZawartość pliku '{PLIK_LOG}':")
    async with aiofiles.open(PLIK_LOG, 'r', encoding='utf-8') as f:
        print(await f.read())


asyncio.run(main())
