import asyncio


async def pracownik() -> None:
    try:
        while True:
            print("Pracuję...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Anulowano, sprzątam...")
        raise


async def main() -> None:
    task = asyncio.create_task(pracownik())
    await asyncio.sleep(5)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Zadanie zakończone.")


if __name__ == "__main__":
    asyncio.run(main())
