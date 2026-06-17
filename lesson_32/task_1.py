import asyncio
import time


async def simulated_task(task_id, delay):
    print(f"Start zadania {task_id}, opóźnienie: {delay}s")
    await asyncio.sleep(delay)
    print(f"Koniec zadania {task_id}")
    return f"Zadanie {task_id} zakończone"


async def main():
    start_time = time.time()

    results = await asyncio.gather(
        simulated_task(1, 1),
        simulated_task(2, 4),
        simulated_task(3, 2),
    )

    end_time = time.time()

    print("Wyniki:", results)
    print(f"Całkowity czas wykonania: {end_time - start_time:.2f} sekundy")


if __name__ == "__main__":
    asyncio.run(main())