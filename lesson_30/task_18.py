# Zadanie 18 – Symulacja wyścigu w banku
# Stwórz klasę KontoBankowe z atrybutem saldo. Stwórz metody wplac(kwota) i wyplac(kwota).
# Metoda wyplac powinna sprawdzać, czy na koncie jest wystarczająco środków. Uruchom 10
# wątków, z których 5 wpłaca losowe kwoty, a 5 wypłaca losowe kwoty. Zabezpiecz metody za
# pomocą blokady, aby saldo na koniec było prawidłowe.

import random
import threading
import time


class KontoBankowe:
	def __init__(self, saldo_poczatkowe=0):
		self.saldo = saldo_poczatkowe
		self.blokada = threading.Lock()

	def wplac(self, kwota):
		with self.blokada:
			self.saldo += kwota
			print(
				f"{threading.current_thread().name}: wpłata {kwota} zł | saldo: {self.saldo} zł"
			)

	def wyplac(self, kwota):
		with self.blokada:
			if self.saldo >= kwota:
				self.saldo -= kwota
				print(
					f"{threading.current_thread().name}: wypłata {kwota} zł | saldo: {self.saldo} zł"
				)
				return True

			print(
				f"{threading.current_thread().name}: brak środków na wypłatę {kwota} zł | saldo: {self.saldo} zł"
			)
			return False


def wykonaj_wplate(konto, statystyki, blokada_statystyk):
	kwota = random.randint(50, 300)
	time.sleep(random.uniform(0.01, 0.1))
	konto.wplac(kwota)

	with blokada_statystyk:
		statystyki["wplaty"] += kwota


def wykonaj_wyplate(konto, statystyki, blokada_statystyk):
	kwota = random.randint(50, 300)
	time.sleep(random.uniform(0.01, 0.1))

	if konto.wyplac(kwota):
		with blokada_statystyk:
			statystyki["wyplaty"] += kwota


def main():
	saldo_poczatkowe = 1000
	konto = KontoBankowe(saldo_poczatkowe)

	statystyki = {
		"wplaty": 0,
		"wyplaty": 0,
	}
	blokada_statystyk = threading.Lock()
	watki = []

	for i in range(5):
		watki.append(
			threading.Thread(
				target=wykonaj_wplate,
				name=f"Wplata-{i + 1}",
				args=(konto, statystyki, blokada_statystyk),
			)
		)
		watki.append(
			threading.Thread(
				target=wykonaj_wyplate,
				name=f"Wyplata-{i + 1}",
				args=(konto, statystyki, blokada_statystyk),
			)
		)

	random.shuffle(watki)

	for watek in watki:
		watek.start()

	for watek in watki:
		watek.join()

	oczekiwane_saldo = (
		saldo_poczatkowe + statystyki["wplaty"] - statystyki["wyplaty"]
	)

	print("\nPodsumowanie:")
	print(f"Suma wpłat: {statystyki['wplaty']} zł")
	print(f"Suma udanych wypłat: {statystyki['wyplaty']} zł")
	print(f"Oczekiwane saldo końcowe: {oczekiwane_saldo} zł")
	print(f"Rzeczywiste saldo końcowe: {konto.saldo} zł")


if __name__ == "__main__":
	main()

