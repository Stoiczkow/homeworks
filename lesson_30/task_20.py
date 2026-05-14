# Zadanie 20 – AI: Równoległe przetwarzanie obrazów (symulacja)
# Załóżmy, że masz do przetworzenia 10 "obrazów", reprezentowanych jako listy 1000x1000
# losowych liczb. Napisz funkcję zastosuj_filtr(obraz), która iteruje po każdym "pikselu" i
# wykonuje na nim jakąś operację matematyczną (np. piksel * 1.1), symulując zadanie CPU-
# bound. Użyj multiprocessing.Pool do przetworzenia wszystkich 10 obrazów równolegle i zmierz
# czas. Porównaj go z czasem wykonania sekwencyjnego.

import multiprocessing as mp
import random
import time

LICZBA_OBRAZOW = 10
ROZMIAR_OBRAZU = 1000  
MNOZNIK_FILTRA = 1.1

def generuj_obraz(seed):
	"""Tworzy obraz 1000x1000 z losowych liczb."""
	generator = random.Random(seed)
	return [
		[generator.random() for _ in range(ROZMIAR_OBRAZU)]
		for _ in range(ROZMIAR_OBRAZU)
	]


def zastosuj_filtr(obraz):
	"""
	Iteruje po każdym pikselu i wykonuje prostą operację matematyczną.
	Zwraca sumę kontrolną, żeby nie przesyłać całych obrazów między procesami.
	"""
	suma_po_filtrze = 0.0

	for wiersz in obraz:
		for indeks_piksela, piksel in enumerate(wiersz):
			nowy_piksel = piksel * MNOZNIK_FILTRA
			wiersz[indeks_piksela] = nowy_piksel
			suma_po_filtrze += nowy_piksel

	return suma_po_filtrze


def przetworz_jeden_obraz(seed):
	"""
	Generuje obraz i od razu go przetwarza.
	Dzięki temu nie trzymamy wszystkich 10 obrazów jednocześnie w pamięci.
	"""
	obraz = generuj_obraz(seed)
	return zastosuj_filtr(obraz)


def przetwarzanie_sekwencyjne(seeds):
	return [przetworz_jeden_obraz(seed) for seed in seeds]


def przetwarzanie_rownolegle(seeds):
	with mp.Pool(processes=mp.cpu_count()) as pool:
		return pool.map(przetworz_jeden_obraz, seeds)


def main():
	seeds = list(range(LICZBA_OBRAZOW))

	print(f"Liczba obrazów: {LICZBA_OBRAZOW}")
	print(f"Rozmiar każdego obrazu: {ROZMIAR_OBRAZU}x{ROZMIAR_OBRAZU}")
	print(f"Liczba procesów w puli: {mp.cpu_count()}")

	start = time.perf_counter()
	wyniki_sekwencyjne = przetwarzanie_sekwencyjne(seeds)
	czas_sekwencyjny = time.perf_counter() - start

	start = time.perf_counter()
	wyniki_rownolegle = przetwarzanie_rownolegle(seeds)
	czas_rownolegly = time.perf_counter() - start

	suma_sekwencyjna = sum(wyniki_sekwencyjne)
	suma_rownolegla = sum(wyniki_rownolegle)
	wyniki_zgodne = abs(suma_sekwencyjna - suma_rownolegla) < 1e-6
	przyspieszenie = (
		czas_sekwencyjny / czas_rownolegly if czas_rownolegly > 0 else float("inf")
	)

	print(f"\nCzas sekwencyjny: {czas_sekwencyjny:.2f} s")
	print(f"Czas równoległy: {czas_rownolegly:.2f} s")
	print(f"Przyspieszenie: {przyspieszenie:.2f}x")
	print(f"Wyniki zgodne: {'tak' if wyniki_zgodne else 'nie'}")

	if czas_rownolegly < czas_sekwencyjny:
		print("Wersja równoległa była szybsza.")
	elif czas_rownolegly > czas_sekwencyjny:
		print("W tym uruchomieniu wersja sekwencyjna była szybsza.")
	else:
		print("Obie wersje miały taki sam czas.")


if __name__ == "__main__":
	mp.freeze_support()
	main()

