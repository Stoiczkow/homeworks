# Zadanie 11 – Producent i konsument
# Zaimplementuj klasyczny problem producenta-konsumenta. Stwórz współdzieloną,
# bezpieczną wątkowo kolejkę (import queue; q = queue.Queue()). "Producent" to wątek,
# który co sekundę dodaje do kolejki nowy element (np. losową liczbę). "Konsument" to
# wątek, który co 1.5 sekundy pobiera element z kolejki i go drukuje. Program powinien
# działać przez 10 sekund.

import threading
import queue
import random
import time

q = queue.Queue()

def producent():
    for _ in range(10):

        liczba = random.randint(1, 100)

        q.put(liczba)

        print(f"Producent dodał: {liczba}")

        time.sleep(1)

def konsument():
    for _ in range (10):

        element = q.get()

        print(f"Konsument pobrał: {element}")

        time.sleep(1.5)

t1 = threading.Thread(target=producent)
t2 = threading.Thread(target=konsument)

t1.start()
t2.start()

t1.join()
t2.join()

print("Koniec programu.")