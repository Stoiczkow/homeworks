import threading
from pathlib import Path

path = Path(".")
txt_files = list(path.glob("*.txt"))

counter = 0
lock = threading.Lock()

def count_file(word, filename):
    global counter

    with open(filename, "r", encoding="utf-8") as f:
        file_content = f.read()

    count = file_content.count(word)

    with lock:
        counter += count


threads = []
word = "hello"

for filename in txt_files:
    thread = threading.Thread(
        target=count_file,
        args=(word, str(filename))
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Słowo '{word}' występuje {counter} razy we wszystkich plikach txt")