import multiprocessing
import time


def ciezka_praca_obliczeniowa(n):
    print("Proces startuje...")
    suma = sum(i * i for i in range(n))
    print(f"Proces zakończył, suma: {suma}")


# Uruchomienie sekwencyjne
start = time.time()

ciezka_praca_obliczeniowa(20000000)
ciezka_praca_obliczeniowa(20000000)

print(f"Sekwencyjnie zajęło: {time.time() - start:.2f}s")

# Uruchomienie równoległe
if __name__ == "__main__":
    start = time.time()

    p1 = multiprocessing.Process(target=ciezka_praca_obliczeniowa, args=(20_000_000,))

    p2 = multiprocessing.Process(target=ciezka_praca_obliczeniowa, args=(20_000_000,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Równolegle (2 procesy) zajęło: {time.time() - start:.2f}s")