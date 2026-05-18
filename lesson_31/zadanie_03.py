import asyncio
import time


async def zadanie1() -> None:
    await asyncio.sleep(2)
    print("Zadanie 1 zakończone")


async def zadanie2() -> None:
    await asyncio.sleep(1)
    print("Zadanie 2 zakończone")


async def main() -> None:
    start = time.time()
    await zadanie1()
    await zadanie2()
    print(f"Czas wykonania (sekwencyjnie): {time.time() - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
