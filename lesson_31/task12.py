# Kto pierwszy, ten lepszy

# Uruchom 5 zadań, z których każde śpi przez losowy czas (od 1 do 10 sekund), a następnie zwraca swój czas uśpienia. Napisz program, który zakończy działanie i wypisze wynik pierwszego zakończonego zadania, nie czekając na pozostałe. Wskazówka: użyj asyncio.wait() z argumentem return_when=asyncio.FIRST_COMPLETED.

import asyncio
import random

async def task(task_id: int):
    sleep_time = random.randint(1, 10)
    await asyncio.sleep(sleep_time)
    return task_id, sleep_time

async def main():
    tasks = [asyncio.create_task(task(i)) for i in range(5)]

    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    # pobieramy wynik pierwszego zakończonego zadania
    for d in done:
        task_id, sleep_time = d.result()
        print(f"Pierwsze zakończone zadanie: Task {task_id}, spało {sleep_time} sekund")

    # anuluj pozostałe zadania
    for p in pending:
        p.cancel()

    # poczeka az się anulują
    await asyncio.gather(*pending, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())