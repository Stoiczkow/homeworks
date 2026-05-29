"""
Zadanie 18 – Anulowanie zadania
Zadanie drukuje "Pracuję..." co sekundę przez 5 sekund,
po czym jest anulowane. CancelledError obsługiwany w pętli.
"""
import asyncio


async def pracownik():
    try:
        while True:
            print("Pracuję...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Anulowano, sprzątam...")
        raise  # re-raise jest dobrą praktyką – informuje event loop o anulowaniu


async def main():
    task = asyncio.create_task(pracownik())

    await asyncio.sleep(5)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Zadanie zostało anulowane.")


asyncio.run(main())
