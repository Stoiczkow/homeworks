# Zadanie 6 – Pierwszy proces
# Napisz program, który uruchamia osobny proces. Proces ten powinien obliczyć silnię liczby
# 10 i wydrukować wynik.

import multiprocessing
import math

def calculate_factorial():
    print(math.factorial(10))

if __name__ == "__main__":
    process = multiprocessing.Process(target=calculate_factorial)
    process.start()
    process.join()