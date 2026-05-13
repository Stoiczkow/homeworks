import threading

ELEMENT_COUNT = 10_000_000
THREAD_COUNT = 4

total_sum = 0
lock = threading.Lock()


def sum_chunk(chunk: list[int]) -> None:
    global total_sum
    partial = sum(chunk)
    with lock:
        total_sum += partial


if __name__ == "__main__":
    data = list(range(1, ELEMENT_COUNT + 1))

    chunk_size = len(data) // THREAD_COUNT
    threads = []
    for i in range(THREAD_COUNT):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < THREAD_COUNT - 1 else len(data)
        thread = threading.Thread(target=sum_chunk, args=(data[start:end],))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    expected = ELEMENT_COUNT * (ELEMENT_COUNT + 1) // 2
    print(f"Obliczona suma: {total_sum}")
    print(f"Oczekiwana suma: {expected}")
    print(f"Zgodność: {total_sum == expected}")