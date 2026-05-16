# Kolejka producent-konsument

# Zaimplementuj system z jednym producentem i dwoma konsumentami przy użyciu asyncio.Queue. Producent co 0.5 sekundy dodaje do kolejki liczbę (od 1 do 20). Konsumenci pobierają liczby z kolejki, jak tylko się pojawią, i wypisują, który konsument przetworzył daną liczbę (np. "Konsument 1 przetworzył liczbę: 5")


import asyncio

async def producer(queue: asyncio.Queue):
    for i in range(1, 21):
        await asyncio.sleep(0.5)
        await queue.put(i)
        print(f"Producent dodał: {i}")

    # zakonczenie dla konsumentów
    await queue.put(None)
    await queue.put(None)


async def consumer(queue: asyncio.Queue, consumer_id: int):
    while True:
        item = await queue.get()

        if item is None:
            # przekazuj sygnał dalej dla drugiego konsumenta
            await queue.put(None)
            break

        print(f"Konsument {consumer_id} przetworzył liczbę: {item}")
        queue.task_done()


async def main():
    queue = asyncio.Queue()

    prod = asyncio.create_task(producer(queue))
    cons1 = asyncio.create_task(consumer(queue, 1))
    cons2 = asyncio.create_task(consumer(queue, 2))

    await asyncio.gather(prod, cons1, cons2)

if __name__ == "__main__":
    asyncio.run(main())