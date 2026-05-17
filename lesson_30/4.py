# Zadanie 4 – Problem wyścigu
# Napisz program z globalną listą. Stwórz 2 wątki - jeden dodaje do listy 100 tysięcy razy
# liczbę 1, a drugi 100 tysięcy razy liczbę 2. Po zakończeniu obu wątków, sprawdź długość
# listy. Czy wynosi ona 200 tysięcy? Uruchom program kilka razy

import threading

test_list = []

def add_one():
    for _ in range(1000000):
        test_list.append(1)

def add_two():
    for _ in range(1000000):
        test_list.append(2)

thread1 = threading.Thread(target=add_one)
thread2 = threading.Thread(target=add_two)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Długość listy: {len(test_list)}")