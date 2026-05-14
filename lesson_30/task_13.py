# Stwórz listę 100 losowych liczb od 1 do 1000. Użyj multiprocessing.Pool do stworzenia puli
# procesów, która dla każdej liczby sprawdzi, czy jest ona liczbą pierwszą. Funkcja pool.map
# powinna zwrócić listę wartości True/False. Wydrukuj, ile liczb pierwszych znalazłeś.

import random
from multiprocessing import Pool


def czy_pierwsza(liczba):
	if liczba < 2:
		return False

	for i in range(2, int(liczba ** 0.5) + 1):
		if liczba % i == 0:
			return False

	return True


if __name__ == "__main__":
	liczby = [random.randint(1, 1000) for _ in range(100)]

	with Pool() as pool:
		wyniki = pool.map(czy_pierwsza, liczby)

	ile_pierwszych = sum(wyniki)

	print(f"Znaleziono {ile_pierwszych} liczb pierwszych.")

