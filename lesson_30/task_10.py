# Zadanie 10 – Równoległe liczenie słów w plikach
# Napisz program, który liczy łączną liczbę wystąpień danego słowa we wszystkich plikach
# .txt w bieżącym katalogu. Każdy plik powinien być przeszukiwany w osobnym wątku. Wyniki
# zliczania z każdego wątku powinny być bezpiecznie dodane do wspólnego licznika.


from pathlib import Path
import threading

result = 0
lock = threading.Lock()

word = input("Jakiego słowa szukamy?: ")

p = Path.cwd()

object_list = list(p.glob('**/*.txt'))
path_list = []

for i in object_list:
    path_list.append(i.absolute())

def searching_word(word, file):
    with open(file, encoding="UTF-8", mode="r") as txtfile:
        global result
        content = txtfile.read()
        with lock:
            result += content.count(word)

threads = []

for file in path_list:
    thread = threading.Thread(target=searching_word, args=(word, file))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print(result)