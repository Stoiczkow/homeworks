import asyncio


async def pracuj():
    try:
        while True:
            print("Pracuję...")
            await asyncio.sleep(1)

    except asyncio.CancelledError:
        print("Anulowano, sprzątam...")
        raise


async def main():
    task = asyncio.create_task(pracuj())

    await asyncio.sleep(5)

    print("Anuluję zadanie...")
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Zadanie zostało anulowane.")


asyncio.run(main())