#Zadanie 18 – Symulacja wyścigu w banku

# Stwórz klasę KontoBankowe z atrybutem saldo. Stwórz metody wplac(kwota) i wyplac(kwota). Metoda wyplac powinna sprawdzać, czy na koncie jest wystarczająco środków. Uruchom 10 wątków, z których 5 wpłaca losowe kwoty, a 5 wypłaca losowe kwoty. Zabezpiecz metody za pomocą blokady, aby saldo na koniec było prawidłowe.

import threading
import random
import time


class KontoBankowe:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.lock = threading.Lock()

    def wplac(self, kwota):
        with self.lock:
            stara_wartosc = self.saldo
            time.sleep(0.01)  # opóźnienie
            self.saldo = stara_wartosc + kwota
            print(f"[WPŁATA] +{kwota} -> saldo: {self.saldo}")

    def wyplac(self, kwota):
        with self.lock:
            if self.saldo >= kwota:
                stara_wartosc = self.saldo
                time.sleep(0.01)  # opóźnienie
                self.saldo = stara_wartosc - kwota
                print(f"[WYPŁATA] -{kwota} -> saldo: {self.saldo}")
            else:
                print(f"[WYPŁATA] brak środków na {kwota} -> saldo: {self.saldo}")


def wplaty(konto):
    for _ in range(10):
        kwota = random.randint(10, 100)
        konto.wplac(kwota)
        time.sleep(random.uniform(0.01, 0.05))


def wyplaty(konto):
    for _ in range(10):
        kwota = random.randint(10, 100)
        konto.wyplac(kwota)
        time.sleep(random.uniform(0.01, 0.05))


def main():
    konto = KontoBankowe(100)

    threads = []

    # 5 wątków wpłat
    for _ in range(5):
        t = threading.Thread(target=wplaty, args=(konto,))
        threads.append(t)

    # 5 wątków wypłat
    for _ in range(5):
        t = threading.Thread(target=wyplaty, args=(konto,))
        threads.append(t)

    
    for t in threads:
        t.start()

    # czekamy na zakończenie
    for t in threads:
        t.join()

    print("\nKOŃCOWE SALDO:", konto.saldo)


if __name__ == "__main__":
    main()