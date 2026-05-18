import asyncio

import aiofiles

PLIK_LOGOW = "logi_async.txt"


async def zapisz_log(numer: int, lock: asyncio.Lock) -> None:
    for i in range(3):
        await asyncio.sleep(0.1 * numer)
        wpis = f"Log z korutyny {numer} (wpis #{i + 1})\n"
        async with lock:
            async with aiofiles.open(PLIK_LOGOW, mode="a", encoding="utf-8") as f:
                await f.write(wpis)
        print(f"Korutyna {numer} zapisała wpis {i + 1}")


async def main() -> None:
    async with aiofiles.open(PLIK_LOGOW, mode="w", encoding="utf-8"):
        pass

    lock = asyncio.Lock()
    await asyncio.gather(*(zapisz_log(i, lock) for i in range(1, 6)))

    print("\nZawartość pliku:")
    async with aiofiles.open(PLIK_LOGOW, mode="r", encoding="utf-8") as f:
        print(await f.read())


if __name__ == "__main__":
    asyncio.run(main())
