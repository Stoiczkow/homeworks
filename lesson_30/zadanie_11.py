import queue
import random
import threading
import time

DURATION_S = 10
STOP_SIGNAL = None


def producer(q: queue.Queue, stop_event: threading.Event) -> None:
    while not stop_event.is_set():
        item = random.randint(1, 100)
        q.put(item)
        print(f"[Producer] Wyprodukował: {item}")
        time.sleep(1)
    q.put(STOP_SIGNAL)


def consumer(q: queue.Queue) -> None:
    while True:
        item = q.get()
        if item is STOP_SIGNAL:
            print("[Consumer] Otrzymał sygnał końca.")
            break
        print(f"[Consumer] Odebrał: {item}")
        time.sleep(1.5)


if __name__ == "__main__":
    q: queue.Queue = queue.Queue()
    stop_event = threading.Event()

    producer_thread = threading.Thread(target=producer, args=(q, stop_event))
    consumer_thread = threading.Thread(target=consumer, args=(q,))

    producer_thread.start()
    consumer_thread.start()

    time.sleep(DURATION_S)
    stop_event.set()

    producer_thread.join()
    consumer_thread.join()
    print("Koniec symulacji producent-konsument.")