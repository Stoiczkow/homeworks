import hashlib
import multiprocessing
from pathlib import Path


FILES_DIR = Path("hash_files")


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return file_path.name, sha256.hexdigest()


if __name__ == "__main__":
    FILES_DIR.mkdir(exist_ok=True)

    sample_files = {
        "file_1.txt": "To jest pierwszy plik.",
        "file_2.txt": "To jest drugi plik.",
        "file_3.txt": "Python multiprocessing SHA256.",
    }

    for filename, content in sample_files.items():
        file_path = FILES_DIR / filename
        file_path.write_text(content, encoding="utf-8")

    files = [file_path for file_path in FILES_DIR.iterdir() if file_path.is_file()]

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_sha256, files)

    hashes = dict(results)

    print("Skróty SHA256 plików:")

    for filename, file_hash in hashes.items():
        print(f"{filename}: {file_hash}")