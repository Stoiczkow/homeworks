# Zadanie 12 – GIL w praktyce (CPU-bound)
# Napisz funkcję, która wykonuje intensywne obliczenia, np. sum(i*i for i in
# range(20_000_000)). Zmierz czas wykonania tej funkcji dwa razy pod rząd. Następnie
# zmierz czas wykonania jej dwa razy jednocześnie w dwóch różnych wątkach. Na koniec
# zmierz czas, wykonując ją dwa razy jednocześnie w dwóch różnych procesach. Porównaj i
# wyjaśnij wyniki w komentarzu w kodzie.

import threading
import multiprocessing
import time

def calculations():
    return sum(i * i for i in range(20_000_000))

start1 = time.time()

calculations()
calculations()

end1 = time.time()

result1 = end1 - start1

print(f"Czas wykonania: {result1:.2f}")

thread1 = threading.Thread(target=calculations)
thread2 = threading.Thread(target=calculations)


start2 = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end2 = time.time()

result2 = end2 - start2

print(f"Czas wykonania przy pomocy wątków: {result2:.2f}")

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=calculations)
    process2 = multiprocessing.Process(target=calculations)

    start3 = time.time()

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end3 = time.time()

    result3 = end3 - start3

    print(f"Czas wykonania przy użyciu multiprocessing: {result3:.2f}")
    

# Wątki nie przyspieszają znacząco obliczeń CPU-bound,
# ponieważ Python posiada GIL (Global Interpreter Lock),
# który pozwala wykonywać kod Pythona tylko jednemu
# wątkowi naraz.
#
# Multiprocessing działa szybciej, ponieważ każdy proces
# posiada własny interpreter Pythona i własny GIL,
# dzięki czemu obliczenia mogą być wykonywane równolegle
# na wielu rdzeniach procesora.
