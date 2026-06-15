import threading
import time


numbers = list(range(1, 1_000_001))

suma_calkowita = 0
lock = threading.Lock()


def sum_part(part):
    global suma_calkowita

    partial_sum = sum(part)

    with lock:
        suma_calkowita += partial_sum


start_time = time.time()

chunk_size = len(numbers) // 4

parts = [
    numbers[0:chunk_size],
    numbers[chunk_size:chunk_size * 2],
    numbers[chunk_size * 2:chunk_size * 3],
    numbers[chunk_size * 3:]
]

threads = []

for part in parts:
    thread = threading.Thread(target=sum_part, args=(part,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

expected_sum = sum(numbers)

print(f"Suma całkowita: {suma_calkowita}")
print(f"Oczekiwana suma: {expected_sum}")
print(f"Czy wynik jest poprawny? {suma_calkowita == expected_sum}")
print(f"Czas wykonania: {end_time - start_time:.2f} sekund")