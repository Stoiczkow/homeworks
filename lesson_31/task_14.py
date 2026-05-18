# 14. 🧠 Kolejka producent-konsument
# Zaimplementuj system z jednym producentem i dwoma konsumentami przy użyciu
# asyncio.Queue. Producent co 0.5 sekundy dodaje do kolejki liczbę (od 1 do 20).
# Konsumenci pobierają liczby z kolejki, jak tylko się pojawią, i wypisują, który konsument
# przetworzył daną liczbę (np. "Konsument 1 przetworzył liczbę: 5").
# (challenge)


import asyncio
import time


async def producer(queue):
    for i in range(1, 21):
        await asyncio.sleep(0.5)
        await queue.put(i)


async def consumer(name, queue):
    while True:
        get_from_q = queue.get()

        try:
            element = await asyncio.wait_for(get_from_q, timeout=2)
        except TimeoutError:
            break

        print(f"{name} przetworzył liczbę: {element}")


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue), consumer("Konsument 1", queue), consumer("Konsument 2", queue)
    )


asyncio.run(main())