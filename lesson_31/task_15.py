# Napisz program, w którym 5 korutyn współbieżnie generuje jakieś dane tekstowe (np. "Log
# z korutyny X"). Wszystkie powinny zapisywać swoje logi do jednego pliku. Zapewnij, aby
# dostęp do pliku był zsynchronizowany, żeby wpisy się nie pomieszały. Użyj asyncio.Lock
# oraz biblioteki aiofiles (pip install aiofiles).
import asyncio, aiofiles

async def text_generator(generator_nr):
    lock = asyncio.Lock()
    
    async with lock:
        async with aiofiles.open("dane.txt", "a") as f:
            await f.write(f"Log z korutyny nr {generator_nr}\n")
        
async def main():
    tasks = [
        text_generator(i) 
        for i in range(5)
        ]
    
    await asyncio.gather(
        *tasks
    )

asyncio.run(main())