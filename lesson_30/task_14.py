import threading
import shutil
from pathlib import Path


source_dir = Path("source_files")
destination_dir = Path("copied_files")


def copy_file(file_path):
    destination_path = destination_dir / file_path.name

    print(f"Kopiowanie pliku {file_path.name}...")

    shutil.copy(file_path, destination_path)

    print(f"Ukończono kopiowanie pliku {file_path.name}")


if __name__ == "__main__":
    source_dir.mkdir(exist_ok=True)
    destination_dir.mkdir(exist_ok=True)

    # Tworzymy przykładowe pliki, żeby zadanie dało się od razu uruchomić
    sample_files = {
        "file_1.txt": "To jest pierwszy plik.",
        "file_2.txt": "To jest drugi plik.",
        "file_3.txt": "To jest trzeci plik.",
        "file_4.txt": "To jest czwarty plik.",
        "file_5.txt": "To jest piąty plik.",
    }

    for filename, content in sample_files.items():
        file_path = source_dir / filename
        file_path.write_text(content, encoding="utf-8")

    files = list(source_dir.glob("*"))

    threads = []

    for file_path in files:
        if file_path.is_file():
            thread = threading.Thread(target=copy_file, args=(file_path,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    print("Wszystkie pliki zostały skopiowane.")