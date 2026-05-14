# Napisz program z globalną listą. Stwórz 2 wątki - jeden dodaje do listy 100 tysięcy razy
# liczbę 1, a drugi 100 tysięcy razy liczbę 2. Po zakończeniu obu wątków, sprawdź długość
# listy. Czy wynosi ona 200 tysięcy? Uruchom program kilka razy.

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

if __name__ == "__main__":
    thread1 = threading.Thread(target=add_ones)
    thread2 = threading.Thread(target=add_twos)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print(f"Długość listy: {len(global_list)}")
    print(f"Czy wynosi 200 000? {len(global_list) == 200_000}")

