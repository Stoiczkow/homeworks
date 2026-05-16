#Zadanie 16 – Równoległe haszowanie plików

# Napisz skrypt, który oblicza skrót SHA256 dla każdego pliku w danym katalogu. Użyj
# multiprocessing.Pool, aby rozdzielić listę plików między dostępne rdzenie procesora. Program powinien na końcu wydrukować słownik, gdzie kluczem jest nazwa pliku, a wartością jego hash.


import os
import hashlib
from multiprocessing import Pool, cpu_count


def sha256_file(filepath):
    """Oblicza SHA256 dla pojedynczego pliku."""
    hash_sha256 = hashlib.sha256()

    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hash_sha256.update(chunk)
        return os.path.basename(filepath), hash_sha256.hexdigest()

    except (OSError, IOError):
        # jeśli plik jest niedostępny
        return os.path.basename(filepath), None


def get_files(directory):
    #Zwraca listę pełnych ścieżek
    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]


def main(directory):
    files = get_files(directory)

    with Pool(cpu_count()) as pool:
        results = pool.map(sha256_file, files)

    # zamiana na słownik
    hash_dict = dict(results)

    print(hash_dict)


if __name__ == "__main__":
    directory = input("Podaj ścieżkę do katalogu: ").strip()
    main(directory)