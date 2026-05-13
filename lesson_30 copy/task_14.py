# Zadanie 14 – Kopiowanie plików w tle
# Napisz program, który kopiuje wszystkie pliki z jednego katalogu do drugiego. Każdy plik
# powinien być kopiowany w osobnym wątku. Wyświetlaj postęp, np. "Kopiowanie pliku X...",
# "Ukończono kopiowanie pliku X". Program główny powinien zakończyć się dopiero po
# skopiowaniu wszystkich plików.

from pathlib import Path
import threading
import shutil

source_folder = Path("source")
destination_folder = Path('destination')


