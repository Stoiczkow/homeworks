import threading
import queue
import time
import random


q = queue.Queue()
stop_event = threading.Event()


def producer():
    while not stop_event.is_set():
        number = random.randint(1, 100)
        q.put(number)
        print(f"Producent dodał do kolejki: {number}")
        time.sleep(1)


def consumer():
    while not stop_event.is_set() or not q.empty():
        try:
            number = q.get(timeout=0.5)
        except queue.Empty:
            continue

        print(f"Konsument pobrał z kolejki: {number}")
        q.task_done()
        time.sleep(1.5)


if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    time.sleep(10)

    stop_event.set()

    producer_thread.join()
    consumer_thread.join()

    print("Program zakończył działanie.")