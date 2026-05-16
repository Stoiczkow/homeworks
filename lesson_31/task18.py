# Anulowanie zadania

# Stwórz zadanie, które działa w nieskończonej pętli, co sekundę drukując "Pracuję...". W głównej korutynie main, pozwól mu pracować przez 5 sekund, a następnie je anuluj (task.cancel()). W "pracującej" korutynie obsłuż wyjątek asyncio.CancelledError, aby wydrukować komunikat "Anulowano, sprzątam..." przed jej ostatecznym zakończeniem

import asyncio


async def pracuj():
    try:
        while True:
            print("Pracuję")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Anulowano, sprzątam")
        raise  # przekazujemy  dalej


async def main():
    task = asyncio.create_task(pracuj())

    # pozwól działać 5 sekund
    await asyncio.sleep(5)

    # anulowanie zadania
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Zadanie zostało poprawnie zakończone.")


if __name__ == "__main__":
    asyncio.run(main())