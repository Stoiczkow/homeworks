import multiprocessing


def calculate_factorial():
    number = 10
    result = 1

    for i in range(1, number + 1):
        result *= i

    print(f"Silnia liczby {number} wynosi: {result}")


if __name__ == "__main__":
    process = multiprocessing.Process(target=calculate_factorial)

    process.start()
    process.join()

    print("Proces zakończył pracę.")