"""
Zmodyfikuj program z globalną listą, dodając threading.Lock,
aby operacja dodawania do listy była bezpieczna.
Sprawdź, czy teraz długość listy jest zawsze poprawna.
"""

import threading

global_list = []
lock = threading.Lock()

def add_ones():
    for _ in range(100_000):
        with lock: 
            global_list.append(1)

def add_twos():
    for _ in range(100_000):
        with lock: 
            global_list.append(2)

t1 = threading.Thread(target=add_ones)
t2 = threading.Thread(target=add_twos)

t1.start()
t2.start()

t1.join()
t2.join()

print("Długość listy:", len(global_list))
