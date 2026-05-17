# Zadanie 18 – Symulacja wyścigu w banku
# Stwórz klasę KontoBankowe z atrybutem saldo. Stwórz metody wplac(kwota) i wyplac(kwota).
# Metoda wyplac powinna sprawdzać, czy na koncie jest wystarczająco środków. Uruchom 10
# wątków, z których 5 wpłaca losowe kwoty, a 5 wypłaca losowe kwoty. Zabezpiecz metody za
# pomocą blokady, aby saldo na koniec było prawidłowe

from threading import Thread, Lock
from random import random, randint
import time

class KontoBankowe():
    def __init__(self):
        self.saldo = 0
        self.lock = Lock()

    def wplac(self, kwota):
        with self.lock:
            self.saldo += kwota
            print(f"Wpłacono {kwota}")
            print(f"Obecne saldo: {self.saldo}")
    
    def wyplac(self, kwota):
        with self.lock:
            if self.saldo >= kwota:
                self.saldo -= kwota
                print(f"Wypłacono {kwota}")
                print(f"Obecne saldo: {self.saldo}")
            else:
                print(f"Brak środków na koncie, nie udało się wypłacić {kwota}")

konto = KontoBankowe()

threads = []

def wplacanie(konto):
    for _ in range(10):
        random_int = randint(0,100)
        random_wait = random()
        konto.wplac(random_int)
        time.sleep(random_wait)

def wyplacanie(konto):
    for _ in range(10):
        random_int = randint(0,100)
        random_wait = random()
        konto.wyplac(random_int)
        time.sleep(random_wait)

for i in range(10):
    
    if i < 6:
        thread = Thread(target=wplacanie, args=(konto,))
        thread.start()
        threads.append(thread)
    else:
        thread = Thread(target=wyplacanie, args=(konto,))
        thread.start()
        threads.append(thread)

for t in threads:
    t.join()