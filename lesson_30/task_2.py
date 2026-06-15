import threading
import time


def worker(thread_number):
    print(f"Jestem wątkiem numer {thread_number}")
    time.sleep(1)


threads = []

for i in range(1, 6):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

print("Wszystkie wątki zostały uruchomione.")

for thread in threads:
    thread.join()

print("Wszystkie wątki zakończyły pracę.")