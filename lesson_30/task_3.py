import threading
import time


def pobierz_dane(id_danych):
    print(f"Rozpoczynam pobieranie danych: {id_danych}")
    time.sleep(2)
    print(f"Zakończono pobieranie danych: {id_danych}")


# Wersja sekwencyjna
start = time.time()

pobierz_dane(1)
pobierz_dane(2)
pobierz_dane(3)

koniec = time.time()
print(f"Czas sekwencyjnie: {koniec - start:.2f} sekund")


print("-" * 40)


# Wersja wielowątkowa
start = time.time()

threads = []

for i in range(1, 4):
    thread = threading.Thread(target=pobierz_dane, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

koniec = time.time()
print(f"Czas wielowątkowo: {koniec - start:.2f} sekund")