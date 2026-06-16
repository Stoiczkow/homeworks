import asyncio
import random


async def losowe_zadanie(numer):
    czas = random.randint(1, 10)
    print(f"Zadanie {numer} startuje. Będzie spało {czas} sekund.")

    await asyncio.sleep(czas)

    return f"Zadanie {numer} wygrało! Spało {czas} sekund."


async def main():
    tasks = []

    for i in range(1, 6):
        task = asyncio.create_task(losowe_zadanie(i))
        tasks.append(task)

    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    pierwsze_zadanie = done.pop()
    wynik = await pierwsze_zadanie

    print("\nPierwsze zakończone zadanie:")
    print(wynik)

    for task in pending:
        task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)


asyncio.run(main())