# Zadanie 18 – Symulacja wyścigu w banku
# Stwórz klasę KontoBankowe z atrybutem saldo. Stwórz metody wplac(kwota) i wyplac(kwota).
# Metoda wyplac powinna sprawdzać, czy na koncie jest wystarczająco środków. Uruchom 10
# wątków, z których 5 wpłaca losowe kwoty, a 5 wypłaca losowe kwoty. Zabezpiecz metody za
# pomocą blokady, aby saldo na koniec było prawidłowe

import random
import threading


class KontoBankowe:
    def __init__(self, saldo_start):
        self.saldo = saldo_start
        self.lock = threading.Lock()

    def wplac(self, kwota):
        with self.lock:
            self.saldo += kwota
            print(f"**wplata** +{kwota} - aktualne saldo: {self.saldo}")

    def wyplac(self, kwota):
        with self.lock:
            if self.saldo >= kwota:
                self.saldo -= kwota
                print(f"**wyplata** -{kwota} - aktualne saldo: {self.saldo}")
            else:
                print(f"za niskie saldo {kwota} > {self.saldo}")


konto = KontoBankowe(50)

threads = []

for _ in range(5):
    kwota = random.randint(1, 20)
    t = threading.Thread(target=konto.wplac, args=(kwota,))
    threads.append(t)

for _ in range(5):
    kwota = random.randint(1, 20)
    t = threading.Thread(target=konto.wyplac, args=(kwota,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Końcowe saldo:", konto.saldo)