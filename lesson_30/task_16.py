# Napisz skrypt, który oblicza skrót SHA256 dla każdego pliku w danym katalogu. Użyj
# multiprocessing.Pool, aby rozdzielić listę plików między dostępne rdzenie procesora. Program
# powinien na końcu wydrukować słownik, gdzie kluczem jest nazwa pliku, a wartością jego hash.

from hashlib import sha256
from multiprocessing import Pool, freeze_support
from pathlib import Path


def oblicz_sha256(sciezka_pliku):
	"""Zwraca nazwę pliku i jego skrót SHA256."""
	hasher = sha256()

	with open(sciezka_pliku, "rb") as plik:
		for fragment in iter(lambda: plik.read(4096), b""):
			hasher.update(fragment)

	return sciezka_pliku.name, hasher.hexdigest()


def main():
	sciezka_katalogu = input("Podaj ścieżkę do katalogu: ").strip()
	katalog = Path(sciezka_katalogu)

	if not katalog.exists() or not katalog.is_dir():
		print("Podana ścieżka nie jest katalogiem.")
		return

	lista_plikow = [element for element in katalog.iterdir() if element.is_file()]

	if not lista_plikow:
		print({})
		return

	with Pool() as pool:
		wyniki = pool.map(oblicz_sha256, lista_plikow)

	slownik_hashy = dict(wyniki)
	print(slownik_hashy)


if __name__ == "__main__":
	freeze_support()
	main()

