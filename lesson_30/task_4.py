"""
Napisz program z globalną listą. Stwórz 2 wątki – jeden dodaje do listy
100 tysięcy razy liczbę 1, a drugi 100 tysięcy razy liczbę 2.
Po zakończeniu obu wątków sprawdź długość listy.
Uruchom program kilka razy i sprawdź, czy wynik wynosi 200 tysięcy.
"""

import threading

global_list = []

def add_ones():
    for _ in range(100_000):
        global_list.append(1)

def add_twos():
    for _ in range(100_000):
        global_list.append(2)

t1 = threading.Thread(target=add_ones)
t2 = threading.Thread(target=add_twos)

t1.start()
t2.start()

t1.join()
t2.join()

print("Długość listy:", len(global_list))
