import threading
from pathlib import Path


word_to_find = "python"
total_count = 0
lock = threading.Lock()


def count_word_in_file(file_path):
    global total_count

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().lower()

    word_count = content.count(word_to_find)

    with lock:
        total_count += word_count

    print(f"{file_path.name}: {word_count}")


if __name__ == "__main__":
    # Tworzymy przykładowe pliki, żeby zadanie od razu dało się uruchomić
    sample_files = {
        "file_1.txt": "Python jest fajny. Lubię Python.",
        "file_2.txt": "Django używa Pythona. python python python.",
        "file_3.txt": "Tutaj nie ma szukanego słowa.",
    }

    for filename, content in sample_files.items():
        Path(filename).write_text(content, encoding="utf-8")

    txt_files = list(Path(".").glob("*.txt"))

    threads = []

    for file_path in txt_files:
        thread = threading.Thread(target=count_word_in_file, args=(file_path,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("-" * 40)
    print(f"Łączna liczba wystąpień słowa '{word_to_find}': {total_count}")