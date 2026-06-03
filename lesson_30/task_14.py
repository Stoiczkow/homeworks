# Napisz program, który kopiuje wszystkie pliki z jednego katalogu do drugiego. Każdy plik
# powinien być kopiowany w osobnym wątku. Wyświetlaj postęp, np. "Kopiowanie pliku X...",
# "Ukończono kopiowanie pliku X". Program główny powinien zakończyć się dopiero po
# skopiowaniu wszystkich plików.

from pathlib import Path
import threading
import shutil

def copy_file(file, dir_out):
    print(f"Kopiowanie pliku {file.name}...")
    shutil.copy(
        file,
        dir_out
    )
    print(f"Ukończono kopiowanie pliku {file.name}...")
    

if __name__ == "__main__":
    threads = []
    dir_in = Path("test_in")
    dir_out = Path("test_out")
    
    dir_out.mkdir(exist_ok=True)

    files = [f for f in dir_in.iterdir() if f.is_file()]

    for file in files:
        t = threading.Thread(target=copy_file, args=(file, dir_out,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print("Koniec działania programu")