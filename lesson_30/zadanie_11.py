"""
Zadanie 11 – Producent i konsument
queue.Queue jest bezpieczna wątkowo, więc nie potrzeba dodatkowych blokad.
"""
import queue
import random
import threading
import time


def producent(q, stop_event):
    while not stop_event.is_set():
        liczba = random.randint(1, 100)
        q.put(liczba)
        print(f"[PRODUCENT] dodano: {liczba}  (rozmiar kolejki: {q.qsize()})")
        time.sleep(1)


def konsument(q, stop_event):
    while not stop_event.is_set():
        try:
            liczba = q.get(timeout=0.5)
            print(f"         [KONSUMENT] pobrano: {liczba}")
            q.task_done()
        except queue.Empty:
            pass
        time.sleep(1.5)


if __name__ == '__main__':
    q = queue.Queue()
    stop_event = threading.Event()

    t_prod = threading.Thread(target=producent, args=(q, stop_event))
    t_kons = threading.Thread(target=konsument, args=(q, stop_event))

    t_prod.start()
    t_kons.start()

    time.sleep(10)
    stop_event.set()

    t_prod.join()
    t_kons.join()
    print("Program zakończony.")
