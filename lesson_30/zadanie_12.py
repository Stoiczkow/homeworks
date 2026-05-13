import multiprocessing
import threading
import time

WORKLOAD_SIZE = 20_000_000


def heavy_computation() -> int:
    return sum(i * i for i in range(WORKLOAD_SIZE))


def measure_sequential() -> float:
    start = time.time()
    heavy_computation()
    heavy_computation()
    return time.time() - start


def measure_threads() -> float:
    start = time.time()
    t1 = threading.Thread(target=heavy_computation)
    t2 = threading.Thread(target=heavy_computation)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return time.time() - start


def measure_processes() -> float:
    start = time.time()
    p1 = multiprocessing.Process(target=heavy_computation)
    p2 = multiprocessing.Process(target=heavy_computation)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    return time.time() - start


if __name__ == "__main__":
    sequential_time = measure_sequential()
    print(f"Sekwencyjnie (2x):  {sequential_time:.2f} s")

    thread_time = measure_threads()
    print(f"Dwa wątki:          {thread_time:.2f} s")

    process_time = measure_processes()
    print(f"Dwa procesy:        {process_time:.2f} s")

    # Wyjaśnienie wyników:
    # - Sequential: jedno CPU robi dwa zadania pod rząd.
    # - Threads: czas zbliżony do sekwencyjnego, bo GIL pozwala wykonywać
    #   kod bajtowy Pythona tylko jednemu wątkowi naraz. Zadania CPU-bound
    #   nie zyskują na wielowątkowości.
    # - Processes: każdy proces ma własny GIL i może działać na osobnym
    #   rdzeniu, więc czas powinien być ~połowę krótszy od sekwencyjnego
    #   (minus narzut na uruchomienie procesów i serializację).
