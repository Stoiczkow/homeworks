import asyncio
import time


async def zadanie(opoznienie):
    print(f"Start zadania: {opoznienie}s")
    await asyncio.sleep(opoznienie)
    print(f"Koniec zadania: {opoznienie}s")


async def main():
    start = time.perf_counter()

    await asyncio.gather(
        zadanie(1),
        zadanie(4),
        zadanie(2)
    )

    koniec = time.perf_counter()

    print(f"\Całkowity czas wykonania: {koniec - start:.2f} s")


if __name__ == "__main__":
    asyncio.run(main())