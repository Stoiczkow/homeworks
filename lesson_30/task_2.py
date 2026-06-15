"""
Stwórz program, który uruchamia 5 wątków.
Każdy wątek powinien otrzymać jako argument swój numer (od 1 do 5)
i wydrukować komunikat "Jestem wątkiem numer [numer]".
Główny program powinien poczekać na zakończenie wszystkich wątków.
"""

import threading
import time

def worker(number):
    print(f"Jestem wątkiem numer {number}")
    time.sleep(1)

threads = []

for i in range(1, 6):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Wszystkie wątki zakończyły pracę.")
