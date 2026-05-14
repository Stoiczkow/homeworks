# Napisz funkcję, która wykonuje intensywne obliczenia, np. sum(i*i for i in
# range(20_000_000)). Zmierz czas wykonania tej funkcji dwa razy pod rząd. Następnie
# zmierz czas wykonania jej dwa razy jednocześnie w dwóch różnych wątkach. Na koniec
# zmierz czas, wykonując ją dwa razy jednocześnie w dwóch różnych procesach. Porównaj i
# wyjaśnij wyniki w komentarzu w kodzie.

import multiprocessing
import threading
import time


LICZBA_ITERACJI = 20_000_000


def intensywne_obliczenia():
	return sum(i * i for i in range(LICZBA_ITERACJI))


def worker_watek(wyniki, indeks):
	wyniki[indeks] = intensywne_obliczenia()


def worker_proces(kolejka):
	kolejka.put(intensywne_obliczenia())


def zmierz_dwa_razy_pod_rzad():
	start = time.perf_counter()
	wynik_1 = intensywne_obliczenia()
	wynik_2 = intensywne_obliczenia()
	koniec = time.perf_counter()
	return koniec - start, wynik_1, wynik_2


def zmierz_dwa_watki_jednoczesnie():
	wyniki = [None, None]
	watek_1 = threading.Thread(target=worker_watek, args=(wyniki, 0))
	watek_2 = threading.Thread(target=worker_watek, args=(wyniki, 1))

	start = time.perf_counter()
	watek_1.start()
	watek_2.start()
	watek_1.join()
	watek_2.join()
	koniec = time.perf_counter()

	return koniec - start, wyniki[0], wyniki[1]


def zmierz_dwa_procesy_jednoczesnie():
	kolejka = multiprocessing.Queue()
	proces_1 = multiprocessing.Process(target=worker_proces, args=(kolejka,))
	proces_2 = multiprocessing.Process(target=worker_proces, args=(kolejka,))

	start = time.perf_counter()
	proces_1.start()
	proces_2.start()
	wynik_1 = kolejka.get()
	wynik_2 = kolejka.get()
	proces_1.join()
	proces_2.join()
	koniec = time.perf_counter()

	return koniec - start, wynik_1, wynik_2


if __name__ == "__main__":
	czas_pod_rzad, wynik_1, wynik_2 = zmierz_dwa_razy_pod_rzad()
	czas_watki, wynik_3, wynik_4 = zmierz_dwa_watki_jednoczesnie()
	czas_procesy, wynik_5, wynik_6 = zmierz_dwa_procesy_jednoczesnie()

	print(f"Dwa razy pod rząd: {czas_pod_rzad:.2f} s")
	print(f"Dwa wątki jednocześnie: {czas_watki:.2f} s")
	print(f"Dwa procesy jednocześnie: {czas_procesy:.2f} s")

	print("\nCzy wyniki obliczeń są takie same?")
	print(
		wynik_1 == wynik_2 == wynik_3 == wynik_4 == wynik_5 == wynik_6
	)

