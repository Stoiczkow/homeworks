import multiprocessing
import random


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":
    numbers = [random.randint(1, 1000) for _ in range(100)]

    with multiprocessing.Pool() as pool:
        results = pool.map(is_prime, numbers)

    prime_count = results.count(True)

    print(f"Wylosowane liczby: {numbers}")
    print(f"Wyniki True/False: {results}")
    print(f"Liczba znalezionych liczb pierwszych: {prime_count}")