# Napisz program, który uruchamia osobny proces. Proces ten powinien obliczyć silnię liczby
# 10 i wydrukować wynik.

import multiprocessing
import math


def calculate_factorial():
    """Funkcja obliczająca silnię liczby 10"""
    result = math.factorial(10)
    print(f"Silnia liczby 10 = {result}")


if __name__ == '__main__':
    # Tworzenie osobnego procesu
    process = multiprocessing.Process(target=calculate_factorial)
    
    # Uruchomienie procesu
    process.start()
    
    # Oczekiwanie na zakończenie procesu
    process.join()
    
    print("Proces zakończył się")

