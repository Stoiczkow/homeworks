import asyncio
import time

async def zadanie1():
    await asyncio.sleep(2)
    print("Zadanie 1 zakończone")
    
async def zadanie2():
    await asyncio.sleep(7)
    print("Zadanie 2 zakończone")
    
async def main():
    start = time.time()
    
    task1 = asyncio.create_task(zadanie1())
    
    
    await zadanie2()
    await task1
    
    
    
    stop = time.time()
    
    print(f"Czas wykonania: {stop - start}")
    
asyncio.run(main())
