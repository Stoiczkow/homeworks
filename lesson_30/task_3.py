"""
Napisz funkcję pobierz_dane(id_danych), która symuluje pobieranie danych przez time.sleep(2).
Uruchom tę funkcję dla 3 różnych id_danych sekwencyjnie i zmierz czas.
Następnie uruchom te same wywołania w osobnych wątkach i również zmierz czas.
Porównaj wyniki.
"""

import time
import threading

def pobierz_dane(id_danych):
    print(f"Pobieram dane {id_danych}...")
    time.sleep(2)
    print(f"Zakończono pobieranie {id_danych}")

start = time.time()

pobierz_dane(1)
pobierz_dane(2)
pobierz_dane(3)

end = time.time()
print(f"Czas sekwencyjny: {end - start:.2f} s\n")

start = time.time()

threads = []
for i in [1, 2, 3]:
    t = threading.Thread