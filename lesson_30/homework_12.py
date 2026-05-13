# Zadanie 12 – GIL w praktyce (CPU-bound)
# Napisz funkcję, która wykonuje intensywne obliczenia, np. sum(i*i for i in range(20_000_000)). Zmierz czas wykonania tej funkcji dwa razy pod rząd. Następnie zmierz czas wykonania jej dwa razy jednocześnie w dwóch różnych wątkach. Na koniec zmierz czas, wykonując ją dwa razy jednocześnie w dwóch różnych procesach. Porównaj i wyjaśnij wyniki w komentarzu w kodzie.



import threading
import time


def ciezkie_obliczenia():
    return sum(i * i for i in range(20_000_000))

# 1. Dwa razy pod rząd
start = time.perf_counter()

ciezkie_obliczenia()
ciezkie_obliczenia()

koniec = time.perf_counter()
print("Sekwencyjnie:", koniec - start)

t1 = threading.Thread(target=ciezkie_obliczenia)
t2 = threading.Thread(target=ciezkie_obliczenia)

t1.start()
t2.start()

t1.join()
t2.join()

koniec = time.perf_counter()
print("Wątki:", koniec - start)

# W przypadku wątków, czas wykonania jest zbliżony do czasu sekwencyjnego, ponieważ GIL (Global Interpreter Lock) ogranicza wykonywanie kodu Pythona do jednego wątku na raz. Mimo że mamy dwa wątki, to tylko jeden z nich może wykonywać kod Pythona w danym momencie, co powoduje, że nie ma rzeczywistego przyspieszenia.
start = time.perf_counter()

import multiprocessing
p1 = multiprocessing.Process(target=ciezkie_obliczenia)
p2 = multiprocessing.Process(target=ciezkie_obliczenia)
p1.start()
p2.start()
p1.join()
p2.join()
koniec = time.perf_counter()
print("Procesy:", koniec - start)

