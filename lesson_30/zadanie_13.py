import math
import random
from multiprocessing import Pool


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, int(math.isqrt(n)) + 1, 2):
        if n % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    random.seed(42)
    numbers = [random.randint(1, 1000) for _ in range(100)]

    with Pool() as pool:
        results = pool.map(is_prime, numbers)

    primes = [number for number, prime in zip(numbers, results) if prime]
    print(f"Liczby pierwsze ({len(primes)}): {primes}")
