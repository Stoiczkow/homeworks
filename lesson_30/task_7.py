import multiprocessing


def potega(liczba, pot):
    wynik = liczba ** pot
    print(f"{liczba} do potęgi {pot} wynosi: {wynik}")


if __name__ == "__main__":
    process = multiprocessing.Process(target=potega, args=(5, 3))

    process.start()
    process.join()

    print("Proces zakończył pracę.")