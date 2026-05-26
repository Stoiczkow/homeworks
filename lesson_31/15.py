# Asynchroniczny zapis do pliku
# Napisz program, w którym 5 korutyn współbieżnie generuje jakieś dane tekstowe (np. "Log
# z korutyny X"). Wszystkie powinny zapisywać swoje logi do jednego pliku. Zapewnij, aby
# dostęp do pliku był zsynchronizowany, żeby wpisy się nie pomieszały. Użyj asyncio.Lock
# oraz biblioteki aiofiles (pip install aiofiles).

import asyncio
import aiofiles
from pathlib import Path
from faker import Faker

fake = Faker()
cwd = Path.cwd()
text_file_cwd = cwd / "test_file.txt"

async def make_logs(lock, name):
    for _ in range(3):
        log_text = fake.text(max_nb_chars=20)
        async with lock:
            async with aiofiles.open(text_file_cwd, mode='a') as f:
                await f.write(f"Tekst z korutiny {name}: {log_text}\n")

async def main():

    lock = asyncio.Lock()

    tasks = asyncio.gather(
        make_logs(lock, "c1"),
        make_logs(lock, "c2"),
        make_logs(lock, "c3"),
        make_logs(lock, "c4"),
        make_logs(lock, "c5")
    )

    await tasks

asyncio.run(main())