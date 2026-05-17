# Zadanie 11 – Producent i konsument
# Zaimplementuj klasyczny problem producenta-konsumenta. Stwórz współdzieloną,
# bezpieczną wątkowo kolejkę (import queue; q = queue.Queue()). "Producent" to wątek,
# który co sekundę dodaje do kolejki nowy element (np. losową liczbę). "Konsument" to
# wątek, który co 1.5 sekundy pobiera element z kolejki i go drukuje. Program powinien
# działać przez 10 sekund.

from multiprocessing import Queue, Process
import random
import time

def producer(task_queue):
    for i in range(0,10):
        random_no = random.randint(1, 100)
        task_queue.put(random_no)
        time.sleep(1)

def client(task_queue):
    start_time = time.time()
    while True:
        current_time = time.time()
        if current_time - 10 > start_time:
            break
        print(task_queue.get())
        time.sleep(1.5)



if __name__ == "__main__":
    q = Queue()

    producer_process = Process(target=producer, args=(q,))
    client_process = Process(target=client, args=(q,))

    producer_process.start()
    client_process.start()

    producer_process.join()
    client_process.join()