"""
Zadanie 14 – Kopiowanie plików w tle
Każdy plik kopiowany w osobnym wątku, program kończy się po skopiowaniu wszystkich.
"""
import os
import shutil
import threading


def kopiuj_plik(src, dst):
    nazwa = os.path.basename(src)
    print(f"Kopiowanie pliku {nazwa}...")
    shutil.copy2(src, dst)
    print(f"Ukończono kopiowanie pliku {nazwa}")


if __name__ == '__main__':
    katalog_zrodlowy = 'pliki_zrodlowe'
    katalog_docelowy = 'pliki_skopiowane'

    # Przygotowanie: utwórz katalogi i kilka testowych plików
    os.makedirs(katalog_zrodlowy, exist_ok=True)
    os.makedirs(katalog_docelowy, exist_ok=True)
    for i in range(5):
        sciezka = os.path.join(katalog_zrodlowy, f'plik_{i+1}.txt')
        with open(sciezka, 'w', encoding='utf-8') as f:
            f.write(f"Zawartość pliku numer {i + 1}\n" * 100)

    pliki = [
        os.path.join(katalog_zrodlowy, f)
        for f in os.listdir(katalog_zrodlowy)
        if os.path.isfile(os.path.join(katalog_zrodlowy, f))
    ]

    watki = []
    for plik in pliki:
        t = threading.Thread(target=kopiuj_plik, args=(plik, katalog_docelowy))
        watki.append(t)
        t.start()

    for t in watki:
        t.join()

    print(f"\nWszystkie pliki zostały skopiowane do '{katalog_docelowy}'.")
