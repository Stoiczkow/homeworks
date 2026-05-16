# Napisz funkcję pobierz_dane(id_danych), która symuluje pobieranie danych przez
# time.sleep(2). Uruchom tę funkcję dla 3 różnych id_danych sekwencyjnie i zmierz czas.
# Następnie zrób to samo, ale uruchamiając każdą funkcję w osobnym wątku i również
# zmierz czas. Porównaj wyniki.

import threading
import time

def pobierz_dane(id):
    time.sleep(2)

def pobierz_dane_2(id):
    time.sleep(2)

start_time = time.time()
for i in range(3):
    pobierz_dane(i)

print(f"Czas wykonania sekwencyjnie - {time.time() - start_time}")

threads = []
start_time = time.time()
for i in range(3):
    thread = threading.Thread(target=pobierz_dane, args=(i, ))
    threads.append(thread)
    thread.start()

print(id(thread))
thread.join()
for t in threads:
    print(id(t))
    t.join()
print(f"Czas wykonania wątkowo - {time.time() - start_time}")


# Join musi robić każdy wątek w petli