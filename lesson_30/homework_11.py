#  🧠 Zadanie 11 – Producent i konsument
# Zaimplementuj klasyczny problem producenta-konsumenta. Stwórz współdzieloną, bezpieczną wątkowo kolejkę (import queue; q = queue.Queue()). "Producent" to wątek, który co sekundę dodaje do kolejki nowy element (np. losową liczbę). "Konsument" to wątek, który co 1.5 sekundy pobiera element z kolejki i go drukuje. Program powinien działać przez 10 sekund.

# Przykład 8: Komunikacja przez kolejkę
import threading
import time
import random
import queue

q = queue.Queue()

def producent():
    while True:
        liczba = random.randint(1, 100)
        q.put(liczba)
        print("Wyprodukowano:", liczba)
        time.sleep(1)

def konsument():
    while True:
        try:
            liczba = q.get(timeout=1.5)  # Czekaj na element przez 1.5 sekundy
            print("    Skonsumowano:", liczba)
            time.sleep(1.5)
        except queue.Empty:
            print("Brak elementów do skonsumowania.")

t1 = threading.Thread(target=producent, daemon=True)
t2 = threading.Thread(target=konsument, daemon=True)

t1.start()
t2.start()

time.sleep(10)  # Program działa przez 10 sekund, join nie jest potrzebne i źle zadziała, ponieważ wątki są daemonami, czyli zakończą się automatycznie po zakończeniu głównego wątku.


print("End of program.")

