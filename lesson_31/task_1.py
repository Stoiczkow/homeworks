import asyncio
import time

async def hello2(n):
    print("Hello world!")
    
    for i in range(1, n):
        print(i)
        await asyncio.sleep(1)
        
async def hello(n):
    print("Hello world!")
    
    for i in range(1, n):
        print(i)
        await asyncio.sleep(1)
    
asyncio.run(hello(10))