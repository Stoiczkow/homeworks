import math
import multiprocessing


def compute_factorial(n: int) -> None:
    result = math.factorial(n)
    print(f"Silnia liczby {n} = {result}")


if __name__ == "__main__":
    process = multiprocessing.Process(target=compute_factorial, args=(10,))
    process.start()
    process.join()
