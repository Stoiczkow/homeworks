import hashlib
from multiprocessing import Pool
from pathlib import Path


def hash_file(path: Path) -> tuple[str, str]:
    hasher = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(65536), b""):
            hasher.update(chunk)
    return path.name, hasher.hexdigest()


def prepare_data(directory: Path) -> None:
    directory.mkdir(exist_ok=True)
    for i in range(1, 6):
        file_path = directory / f"file_{i}.bin"
        file_path.write_bytes(f"Dane pliku numer {i}\n".encode() * 1000)


if __name__ == "__main__":
    directory = Path(__file__).parent / "data_zadanie_16"
    prepare_data(directory)

    files = [p for p in directory.iterdir() if p.is_file()]

    with Pool() as pool:
        pairs = pool.map(hash_file, files)

    hashes = dict(pairs)
    for name, digest in hashes.items():
        print(f"{name}: {digest}")