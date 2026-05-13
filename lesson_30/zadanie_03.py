import threading
import time


def fetch_data(data_id: int) -> None:
    print(f"Pobieranie danych {data_id}...")
    time.sleep(2)
    print(f"Dane {data_id} pobrane.")


if __name__ == "__main__":
    start = time.time()
    for data_id in (1, 2, 3):
        fetch_data(data_id)
    sequential_time = time.time() - start
    print(f"Sekwencyjnie: {sequential_time:.2f} s\n")

    start = time.time()
    threads = []
    for data_id in (1, 2, 3):
        thread = threading.Thread(target=fetch_data, args=(data_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    threaded_time = time.time() - start
    print(f"Wielowątkowo: {threaded_time:.2f} s")

    print(f"\nPrzyspieszenie: {sequential_time / threaded_time:.2f}x")