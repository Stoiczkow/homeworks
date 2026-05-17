# Zadanie 14 – Kopiowanie plików w tle
# Napisz program, który kopiuje wszystkie pliki z jednego katalogu do drugiego. Każdy plik
# powinien być kopiowany w osobnym wątku. Wyświetlaj postęp, np. "Kopiowanie pliku X...",
# "Ukończono kopiowanie pliku X". Program główny powinien zakończyć się dopiero po
# skopiowaniu wszystkich plików

from pathlib import Path
import shutil
from multiprocessing import Pool

cwd = Path.cwd()
folder_input = cwd / "files_to_copy"
folder_output = cwd / "output_folder"

file_list_glob = list(folder_input.glob("*"))

file_list = [f.absolute() for f in folder_input.glob("*")]

def copy_file(input_path):
    print(f"Kopiowanie pliku {input_path.name}")
    shutil.copy(input_path, folder_output)
    print(f"Zakończono kopiowanie pliku {input_path.name}")

if __name__ == "__main__":

    with Pool(processes=4) as pool:
        task = pool.map(copy_file, file_list)