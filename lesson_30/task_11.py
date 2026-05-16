# Zadanie 11 – Producent i konsument

# Zaimplementuj klasyczny problem producenta-konsumenta. Stwórz współdzieloną, bezpieczną wątkowo kolejkę (import queue; q = queue.Queue()). "Producent" to wątek,
# który co sekundę dodaje do kolejki nowy element (np. losową liczbę). "Konsument" to
# wątek, który co 1.5 sekundy pobiera element z kolejki i go drukuje. Program powinien # działać przez 10 sekund.

import threading
import queue
import random
import time

# Tworzenie kolejki
q = queue.Queue()

# konczenie działania programu
running = True


# Funkcja producenta
def producent():
    while running:
        liczba = random.randint(1, 100)
        q.put(liczba)
        print(f"[PRODUCENT] Dodano: {liczba}")
        time.sleep(1)


# Funkcja konsumenta
def konsument():
    while running or not q.empty():
        if not q.empty():
            element = q.get()
            print(f"[KONSUMENT] Pobrano: {element}")
        time.sleep(1.5)


# Tworzenie wątków
t_producent = threading.Thread(target=producent)
t_konsument = threading.Thread(target=konsument)

# Start
t_producent.start()
t_konsument.start()

# sleep 10 sek
time.sleep(10)

# Zatrzymanie programu
running = False


t_producent.join()
t_konsument.join()

print("Koniec programu.")