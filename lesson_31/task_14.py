# Zaimplementuj system z jednym producentem i dwoma konsumentami przy użyciu
# asyncio.Queue. Producent co 0.5 sekundy dodaje do kolejki liczbę (od 1 do 20).
# Konsumenci pobierają liczby z kolejki, jak tylko się pojawią, i wypisują, który konsument
# przetworzył daną liczbę (np. "Konsument 1 przetworzył liczbę: 5").
import asyncio

queue = asyncio.Queue()

async def producer(queue):
    for i in range(1, 21):
        print(f"Produkuje {i}")
        await queue.put(i)
        await asyncio.sleep(0.5)
        
async def consumer(consumer_nr, queue):
    while True:    
        try:
            number = await asyncio.wait_for(queue.get(), timeout=5)
            
            print(f"Konsument {consumer_nr} przetworzył liczbę: {number}")
            
        except asyncio.TimeoutError:
            break
    
async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue),
        consumer(1, queue),
        consumer(2, queue)
    )

asyncio.run(main())