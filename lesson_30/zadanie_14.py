import shutil
import threading
from pathlib import Path


def copy_file(source: Path, destination: Path) -> None:
    print(f"Kopiowanie pliku {source.name}...")
    shutil.copy2(source, destination)
    print(f"Ukończono kopiowanie pliku {source.name}")


def prepare_source(source_dir: Path) -> None:
    source_dir.mkdir(exist_ok=True)
    for i in range(1, 6):
        file_path = source_dir / f"file_{i}.txt"
        file_path.write_text(f"Zawartość pliku {i}\n" * 100, encoding="utf-8")


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    source_dir = base_dir / "data_zadanie_14_source"
    destination_dir = base_dir / "data_zadanie_14_destination"

    prepare_source(source_dir)
    destination_dir.mkdir(exist_ok=True)

    threads = []
    for file_path in source_dir.iterdir():
        if file_path.is_file():
            thread = threading.Thread(
                target=copy_file,
                args=(file_path, destination_dir / file_path.name),
            )
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    print(f"\nSkopiowano {len(threads)} plików do {destination_dir}.")
