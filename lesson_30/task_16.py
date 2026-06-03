import hashlib
from pathlib import Path
from multiprocessing import Pool

# Zadanie 16 – Równoległe haszowanie plików
# Napisz skrypt, który oblicza skrót SHA256 dla każdego pliku w danym katalogu. Użyj
# multiprocessing.Pool, aby rozdzielić listę plików między dostępne rdzenie procesora. Program
# powinien na końcu wydrukować słownik, gdzie kluczem jest nazwa pliku, a wartością jego hash

def hash_file(file):
    with open(file, "rb") as f:
        data = f.read()

        hash_value = hashlib.sha256(data).hexdigest()
        
        return file.name, hash_value


files = [path for path in Path(".").iterdir() if path.is_file()]

with Pool(processes=4) as pool:
    results = pool.map(hash_file, files)
    
print(dict(results))