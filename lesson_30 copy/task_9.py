# Zadanie 9 – Sumowanie z wątkami i blokadą
# Napisz program, który sumuje liczby w dużej liście (np. 10 milionów elementów). Podziel
# listę na 4 części i każdą część zsumuj w osobnym wątku. Wyniki częściowe dodawaj do
# globalnej zmiennej suma_calkowita, zabezpieczając dostęp do niej za pomocą
# threading.Lock.

import threading

data = [
    range(2_500_000),
    range(2_500_000, 5_000_000),
    range(5_000_000, 7_500_000),
    range(7_500_000, 10_000_000),
    ]

result = 0

lock = threading.Lock()

def sum_elements(data):
    global result
    with lock:
        result += sum(data)

threads = []

for i in range(4):
    thread = threading.Thread(target=sum_elements, args=(data[i],))
    threads.append(thread)
    thread.start()


for t in threads:
    t.join()

print(f"Wynik końcowy {result}")
print(f"Wynik testowy {sum(range(0, 10000000))}")