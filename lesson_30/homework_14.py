# Zadanie 14 – Kopiowanie plików w tle
# Napisz program, który kopiuje wszystkie pliki z jednego katalogu do drugiego. Każdy plik powinien być kopiowany w osobnym wątku. Wyświetlaj postęp, np. "Kopiowanie pliku X...", "Ukończono kopiowanie pliku X". Program główny powinien zakończyć się dopiero po skopiowaniu wszystkich plików.


import os
import shutil
import threading
def kopiuj_plik(src, dst):
    print(f"Kopiowanie pliku {src}...")
    shutil.copy(src, dst)
    print(f"Ukończono kopiowanie pliku {src}.") 

if __name__ == "__main__":      
    katalog_src = "katalog_zrodlowy"
    katalog_dsc = "katalog_docelowy"

    if not os.path.exists(katalog_dsc):
        os.makedirs(katalog_dsc)

    files = [f for f in os.listdir(katalog_src) if os.path.isfile(os.path.join(katalog_src, f))]

    watki = []
    for file in files:
        src = os.path.join(katalog_src, file)
        dst = os.path.join(katalog_dsc, file)
        watek = threading.Thread(target=kopiuj_plik, args=(src, dst))
        watki.append(watek)
        watek.start()

# Program główny powinien zakończyć się dopiero po skopiowaniu wszystkich plików.
    for watek in watki:
        watek.join()

    print("Wszystkie pliki zostały skopiowane.")

