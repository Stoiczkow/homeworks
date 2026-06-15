import threading
import multiprocessing
import time


def heavy_calculation():
    result = sum(i * i for i in range(20_000_000))
    return result


def run_calculation_and_print():
    result = heavy_calculation()
    print(f"Wynik: {result}")


if __name__ == "__main__":
    # 1. Dwa razy sekwencyjnie
    start = time.time()

    heavy_calculation()
    heavy_calculation()

    end = time.time()
    print(f"Sekwencyjnie: {end - start:.2f} sekund")


    # 2. Dwa razy w dwóch wątkach
    start = time.time()

    thread_1 = threading.Thread(target=run_calculation_and_print)
    thread_2 = threading.Thread(target=run_calculation_and_print)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    end = time.time()
    print(f"Wątki: {end - start:.2f} sekund")


    # 3. Dwa razy w dwóch procesach
    start = time.time()

    process_1 = multiprocessing.Process(target=run_calculation_and_print)
    process_2 = multiprocessing.Process(target=run_calculation_and_print)

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    end = time.time()
    print(f"Procesy: {end - start:.2f} sekund")


    # Komentarz:
    # Zadanie jest CPU-bound, czyli ograniczone mocą procesora.
    # Wątki w Pythonie nie przyspieszają mocno takich obliczeń przez GIL.
    # Procesy mogą być szybsze, ponieważ każdy proces ma własny interpreter Pythona i własny GIL.