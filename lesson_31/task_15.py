import asyncio
import random
import aiofiles


async def zapisz_log(numer_korutyny, lock):
    for i in range(1, 6):
        await asyncio.sleep(random.uniform(0.2, 1.0))

        tekst = f"Log z korutyny {numer_korutyny}, wpis numer {i}\n"

        async with lock:
            async with aiofiles.open("logs.txt", mode="a", encoding="utf-8") as file:
                await file.write(tekst)

        print(f"Zapisano: {tekst.strip()}")


async def main():
    lock = asyncio.Lock()

    zadania = []

    for numer in range(1, 6):
        task = asyncio.create_task(zapisz_log(numer, lock))
        zadania.append(task)

    await asyncio.gather(*zadania)

    print("\nWszystkie logi zapisane do pliku logs.txt")


asyncio.run(main())