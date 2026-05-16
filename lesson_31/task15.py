# Asynchroniczny zapis do pliku

# Napisz program, w którym 5 korutyn współbieżnie generuje jakieś dane tekstowe (np. "Log z korutyny X"). Wszystkie powinny zapisywać swoje logi do jednego pliku. Zapewnij, aby dostęp do pliku był zsynchronizowany, żeby wpisy się nie pomieszały. Użyj asyncio.Lock oraz biblioteki aiofiles (pip install aiofiles).

import asyncio
import aiofiles
import random
import os

# Zapisz plik w tym samym katalogu co skrypt
script_dir = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(script_dir, "task15.txt")
lock = asyncio.Lock()


async def worker(worker_id: int):
    for i in range(5):
        await asyncio.sleep(random.uniform(0.1, 1.0))

        log_line = f"Log z korutyny {worker_id}, wpis {i}\n"

        async with lock:
            async with aiofiles.open(FILE_NAME, mode="a") as f:
                await f.write(log_line)

        print(f"Zapisano: {log_line.strip()}")


async def main():
    print("Zapis do:", os.path.abspath(FILE_NAME))

    f = await aiofiles.open(FILE_NAME, mode="w")
    await f.write("Start logów\n")
    await f.flush()
    await f.close()

    tasks = [asyncio.create_task(worker(i)) for i in range(1, 6)]
    await asyncio.gather(*tasks)
    
    print("Koniec zapisu")


if __name__ == "__main__":
    asyncio.run(main())