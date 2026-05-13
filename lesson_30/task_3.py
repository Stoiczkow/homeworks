# Zadanie 3 – Symulacja pobierania danych
# Napisz funkcję pobierz_dane(id_danych), która symuluje pobieranie danych przez
# time.sleep(2). Uruchom tę funkcję dla 3 różnych id_danych sekwencyjnie i zmierz czas.
# Następnie zrób to samo, ale uruchamiając każdą funkcję w osobnym wątku i również
# zmierz czas. Porównaj wyniki.

import threading
import time

def pobierz_dane(id_danych):
    print(f"Pobieranie danych {id_danych}")
    time.sleep(2)
    print (f"Dane {id_danych} pobrane.")

start = time.time()

for i in range(1, 4):
    pobierz_dane(i)

koniec = time.time()

wynik = koniec - start

print(f"\nCzas wykonania sekwencyjnego: {wynik} sekundy")

watki = []

start = time.time()

for i in range(1, 4):
    thread = threading.Thread(target=pobierz_dane, args=(i, ))
    watki.append(thread)
    thread.start()

for thread in watki:
    thread.join()
 
koniec = time.time()

test = koniec - start

print(f"\nCzas wykonania wielowątkowego: {test} sekundy")