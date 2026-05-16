# Zadanie 12 – GIL w praktyce (CPU-bound)

# Napisz funkcję, która wykonuje intensywne obliczenia, np. sum(i*i for i in range(20_000_000)). Zmierz czas wykonania tej funkcji dwa razy pod rząd. Następnie
# zmierz czas wykonania jej dwa razy jednocześnie w dwóch różnych wątkach. Na koniec
# zmierz czas, wykonując ją dwa razy jednocześnie w dwóch różnych procesach. Porównaj i # wyjaśnij wyniki w komentarzu w kodzie

import time
import threading
import multiprocessing


# Funkcja obliczenia
def obliczenia():
    return sum(i * i for i in range(20_000_000))


if __name__ == "__main__":

# Wykonanie sekwencyjne
    start = time.time()

    obliczenia()
    obliczenia()

    koniec = time.time()

    print("Czas sekwencyjny:", round(koniec - start, 2), "sek")

# Wykonanie na wątkach 
    start = time.time()

    t1 = threading.Thread(target=obliczenia)
    t2 = threading.Thread(target=obliczenia)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    koniec = time.time()

    print("Czas wątków:", round(koniec - start, 2), "sek")

# Wykonanie na procesach 
    start = time.time()

    p1 = multiprocessing.Process(target=obliczenia)
    p2 = multiprocessing.Process(target=obliczenia)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    koniec = time.time()

    print("Czas procesów:", round(koniec - start, 2), "sek")