"""
Zadanie 18 – Symulacja wyścigu w banku
KontoBankowe z blokadą – 5 wątków wpłaca, 5 wypłaca losowe kwoty.
"""
import random
import threading


class KontoBankowe:
    def __init__(self, saldo_poczatkowe=1000):
        self.saldo = saldo_poczatkowe
        self._lock = threading.Lock()

    def wplac(self, kwota):
        with self._lock:
            stare = self.saldo
            self.saldo += kwota
            print(f"  [WPŁATA  +{kwota:4}]  {stare} → {self.saldo}")

    def wyplac(self, kwota):
        with self._lock:
            if self.saldo >= kwota:
                stare = self.saldo
                self.saldo -= kwota
                print(f"  [WYPŁATA -{kwota:4}]  {stare} → {self.saldo}")
            else:
                print(f"  [BRAK ŚRODKÓW] próba wypłaty {kwota}, saldo: {self.saldo}")


if __name__ == '__main__':
    konto = KontoBankowe(saldo_poczatkowe=5000)
    watki = []

    for _ in range(5):
        kwota = random.randint(100, 500)
        t = threading.Thread(target=konto.wplac, args=(kwota,))
        watki.append(t)

    for _ in range(5):
        kwota = random.randint(100, 800)
        t = threading.Thread(target=konto.wyplac, args=(kwota,))
        watki.append(t)

    for t in watki:
        t.start()
    for t in watki:
        t.join()

    print(f"\nSaldo końcowe: {konto.saldo}")
