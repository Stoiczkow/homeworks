# Anulowanie zadania
# Stwórz zadanie, które działa w nieskończonej pętli, co sekundę drukując "Pracuję...". W
# głównej korutynie main, pozwól mu pracować przez 5 sekund, a następnie je anuluj
# (task.cancel()). W "pracującej" korutynie obsłuż wyjątek asyncio.CancelledError, aby
# wydrukować komunikat "Anulowano, sprzątam..." przed jej ostatecznym zakończeniem.

import asyncio

async def worker():
    while True:
        try:
            print("Pracuję...")
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            print("Anulowano, sprzątam...")
            break

async def main():
    worker_task = asyncio.create_task(worker())

    await asyncio.sleep(5)
    worker_task.cancel()

asyncio.run(main())