import asyncio


async def producent(queue):
    for number in range(1, 21):
        await asyncio.sleep(0.5)
        await queue.put(number)
        print(f"Producent dodał liczbę: {number}")

    await queue.put(None)
    await queue.put(None)


async def konsument(name, queue):
    while True:
        number = await queue.get()

        if number is None:
            print(f"{name} kończy pracę.")
            queue.task_done()
            break

        print(f"{name} przetworzył liczbę: {number}")
        queue.task_done()


async def main():
    queue = asyncio.Queue()

    task_producent = asyncio.create_task(producent(queue))
    task_konsument_1 = asyncio.create_task(konsument("Konsument 1", queue))
    task_konsument_2 = asyncio.create_task(konsument("Konsument 2", queue))

    await task_producent
    await queue.join()

    await task_konsument_1
    await task_konsument_2


asyncio.run(main())