"""
Zadanie 16 – Równoległe haszowanie plików
multiprocessing.Pool oblicza SHA256 dla każdego pliku w katalogu.
"""
import hashlib
import os
import multiprocessing


def oblicz_sha256(sciezka):
    sha256 = hashlib.sha256()
    with open(sciezka, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            sha256.update(chunk)
    return sciezka, sha256.hexdigest()


if __name__ == '__main__':
    katalog = '.'  # bieżący katalog – zmień na wybrany

    pliki = [
        os.path.join(katalog, f)
        for f in os.listdir(katalog)
        if os.path.isfile(os.path.join(katalog, f))
    ]

    if not pliki:
        print("Brak plików w katalogu.")
    else:
        with multiprocessing.Pool() as pool:
            wyniki = pool.map(oblicz_sha256, pliki)

        hashes = {os.path.basename(sciezka): hash_val for sciezka, hash_val in wyniki}
        for nazwa, hash_val in sorted(hashes.items()):
            print(f"{hash_val}  {nazwa}")
