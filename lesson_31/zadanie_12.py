import asyncio
import random


async def spij_losowo(numer: int) -> float:
    czas = random.uniform(1, 10)
    await asyncio.sleep(czas)
    return czas


async def main() -> None:
    zadania = {asyncio.create_task(spij_losowo(i), name=f"zadanie-{i}") for i in range(1, 6)}
    done, pending = await asyncio.wait(zadania, return_when=asyncio.FIRST_COMPLETED)

    zwyciezca = done.pop()
    print(f"Pierwsze zakończone: {zwyciezca.get_name()} po {zwyciezca.result():.2f}s")

    for task in pending:
        task.cancel()
    await asyncio.gather(*pending, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
