# Zadanie 20 – AI: Równoległe przetwarzanie obrazów (symulacja)
# Załóżmy, że masz do przetworzenia 10 "obrazów", reprezentowanych jako listy 1000x1000
# losowych liczb. Napisz funkcję zastosuj_filtr(obraz), która iteruje po każdym "pikselu" i
# wykonuje na nim jakąś operację matematyczną (np. piksel * 1.1), symulując zadanie CPU-
# bound. Użyj multiprocessing.Pool do przetworzenia wszystkich 10 obrazów równolegle i zmierz
# czas. Porównaj go z czasem wykonania sekwencyjnego