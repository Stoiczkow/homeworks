# Zadanie 2 – Wiele wątków
# Stwórz program, który uruchamia 5 wątków. Każdy wątek powinien otrzymać jako argument
# swój numer (od 1 do 5) i wydrukować komunikat "Jestem wątkiem numer [numer]". Upewnij
# się, że główny program czeka na zakończenie wszystkich wątków.


import threading


def watek(id):
    print(f"Jestem wątkiem numer {id}")

watki = []

for i in range(1, 6):
    thread = threading.Thread(target=watek, args=(i, ))
    watki.append(thread)
    thread.start()

for thread in watki:
    thread.join()

print("Wszystkie œątki zakończyły swoją pracę.")