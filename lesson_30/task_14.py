# Napisz program, który kopiuje wszystkie pliki z jednego katalogu do drugiego. Każdy plik
# powinien być kopiowany w osobnym wątku. Wyświetlaj postęp, np. "Kopiowanie pliku X...",
# "Ukończono kopiowanie pliku X". Program główny powinien zakończyć się dopiero po
# skopiowaniu wszystkich plików.

import os
import shutil
import threading


def kopiuj_plik(sciezka_zrodlowa, katalog_docelowy):
	nazwa_pliku = os.path.basename(sciezka_zrodlowa)
	sciezka_docelowa = os.path.join(katalog_docelowy, nazwa_pliku)

	print(f"Kopiowanie pliku {nazwa_pliku}...")
	shutil.copy2(sciezka_zrodlowa, sciezka_docelowa)
	print(f"Ukończono kopiowanie pliku {nazwa_pliku}")


def main():
	katalog_zrodlowy = input("Podaj ścieżkę do katalogu źródłowego: ").strip()
	katalog_docelowy = input("Podaj ścieżkę do katalogu docelowego: ").strip()

	if not os.path.isdir(katalog_zrodlowy):
		print("Podany katalog źródłowy nie istnieje.")
		return

	os.makedirs(katalog_docelowy, exist_ok=True)

	pliki = []
	for nazwa in os.listdir(katalog_zrodlowy):
		sciezka = os.path.join(katalog_zrodlowy, nazwa)
		if os.path.isfile(sciezka):
			pliki.append(sciezka)

	if not pliki:
		print("Brak plików do skopiowania.")
		return

	watki = []

	for sciezka_pliku in pliki:
		watek = threading.Thread(target=kopiuj_plik, args=(sciezka_pliku, katalog_docelowy))
		watki.append(watek)
		watek.start()

	for watek in watki:
		watek.join()

	print("Wszystkie pliki zostały skopiowane.")


if __name__ == "__main__":
	main()

