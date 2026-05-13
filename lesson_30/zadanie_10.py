import threading
from pathlib import Path

SEARCH_WORD = "python"

total_count = 0
lock = threading.Lock()


def count_in_file(path: Path, word: str) -> None:
    global total_count
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError as exc:
        print(f"Nie udało się odczytać {path.name}: {exc}")
        return

    occurrences = content.lower().count(word.lower())
    print(f"{path.name}: {occurrences}")

    with lock:
        total_count += occurrences


def create_sample_files(directory: Path) -> None:
    directory.mkdir(exist_ok=True)
    samples = {
        "file1.txt": "Python jest świetny. python python.",
        "file2.txt": "Lubię programować w pythonie. Python to PYTHON.",
        "file3.txt": "Nic tu ciekawego. Java, C++, Rust.",
    }
    for name, content in samples.items():
        (directory / name).write_text(content, encoding="utf-8")


if __name__ == "__main__":
    data_dir = Path(__file__).parent / "data_zadanie_10"
    create_sample_files(data_dir)

    files = list(data_dir.glob("*.txt"))
    threads = []
    for file in files:
        thread = threading.Thread(target=count_in_file, args=(file, SEARCH_WORD))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"\nŁącznie '{SEARCH_WORD}' wystąpiło: {total_count}")