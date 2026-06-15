"""
Napisz program, który uruchamia osobny proces.
Proces ten powinien obliczyć silnię liczby 10 i wydrukować wynik.
"""

import multiprocessing
import math

def oblicz_silnie():
    wynik = math.factorial(10)
    print("Silnia 10 wynosi:", wynik)

if __name__ == "__main__":
    proces = multiprocessing.Process(target=oblicz_silnie)
    proces.start()
    proces.join()
