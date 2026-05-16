# Zadanie 14 – 
# Kopiowanie plików w tle Napisz program, który kopiuje wszystkie pliki z jednego katalogu do drugiego. Każdy plik powinien być kopiowany w osobnym wątku. Wyświetlaj postęp, np. "Kopiowanie pliku X...", "Ukończono kopiowanie pliku X". Program główny powinien zakończyć się dopiero po skopiowaniu wszystkich plików

import os
import shutil
import threading


# Folder źródłowy i docelowy
SOURCE_FOLDER = "task14"
DEST_FOLDER = "copied_files"


# Funkcja kopiująca pojedynczy plik
def kopiuj_plik(nazwa_pliku):
    source_path = os.path.join(SOURCE_FOLDER, nazwa_pliku)
    dest_path = os.path.join(DEST_FOLDER, nazwa_pliku)

    print(f"Kopiowanie pliku {nazwa_pliku}...")

    shutil.copy2(source_path, dest_path)

    print(f"Ukończono kopiowanie pliku {nazwa_pliku}")


if __name__ == "__main__":

    # Tworzenie folderu docelowego jeśli nie istnieje
    os.makedirs(DEST_FOLDER, exist_ok=True)

    # Pobranie listy plików
    pliki = [
        f for f in os.listdir(SOURCE_FOLDER)
        if os.path.isfile(os.path.join(SOURCE_FOLDER, f))
    ]

    watki = []

    # Tworzenie wątków
    for plik in pliki:
        t = threading.Thread(target=kopiuj_plik, args=(plik,))
        t.start()
        watki.append(t)

    # Czekanie na zakończenie wszystkich wątków
    for t in watki:
        t.join()

    print("\nWszystkie pliki zostały skopiowane.")