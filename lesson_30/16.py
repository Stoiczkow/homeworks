# Zadanie 16 – Równoległe haszowanie plików
# Napisz skrypt, który oblicza skrót SHA256 dla każdego pliku w danym katalogu. Użyj
# multiprocessing.Pool, aby rozdzielić listę plików między dostępne rdzenie procesora. Program
# powinien na końcu wydrukować słownik, gdzie kluczem jest nazwa pliku, a wartością jego hash

from pathlib import Path
from multiprocessing import Pool
from hashlib import sha256

cwd = Path.cwd() / "files_to_copy"

file_list = list(cwd.glob("*"))

def hash_file(filepath):

    with open(filepath, 'rb') as file:
        h256 = sha256()
        data = file.read()
        h256.update(data)

    return filepath.name, h256.hexdigest()

if __name__ == "__main__":

    with Pool(processes=2) as pool:
        task = pool.map(hash_file, file_list)

    hashes = dict(task)

    print(hashes)