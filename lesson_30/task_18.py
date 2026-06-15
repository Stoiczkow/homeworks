import threading
import random
import time


class KontoBankowe:
    def __init__(self, saldo_poczatkowe):
        self.saldo = saldo_poczatkowe
        self.lock = threading.Lock()

    def wplac(self, kwota):
        with self.lock:
            stare_saldo = self.saldo
            time.sleep(0.01)
            self.saldo += kwota
            print(f"Wpłata: {kwota} zł | {stare_saldo} zł -> {self.saldo} zł")

    def wyplac(self, kwota):
        with self.lock:
            if self.saldo >= kwota:
                stare_saldo = self.saldo
                time.sleep(0.01)
                self.saldo -= kwota
                print(f"Wypłata: {kwota} zł | {stare_saldo} zł -> {self.saldo} zł")
            else:
                print(f"Brak środków na wypłatę: {kwota} zł | saldo: {self.saldo} zł")


def wykonaj_wplaty(konto):
    for _ in range(5):
        kwota = random.randint(10, 100)
        konto.wplac(kwota)


def wykonaj_wyplaty(konto):
    for _ in range(5):
        kwota = random.randint(10, 100)
        konto.wyplac(kwota)


if __name__ == "__main__":
    konto = KontoBankowe(500)

    threads = []

    for _ in range(5):
        thread = threading.Thread(target=wykonaj_wplaty, args=(konto,))
        threads.append(thread)
        thread.start()

    for _ in range(5):
        thread = threading.Thread(target=wykonaj_wyplaty, args=(konto,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("-" * 40)
    print(f"Saldo końcowe: {konto.saldo} zł")