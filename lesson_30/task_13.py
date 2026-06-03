# Stwórz listę 100 losowych liczb od 1 do 1000. Użyj multiprocessing.Pool do stworzenia puli
# procesów, która dla każdej liczby sprawdzi, czy jest ona liczbą pierwszą. Funkcja pool.map
# powinna zwrócić listę wartości True/False. Wydrukuj, ile liczb pierwszych znalazłeś

import random
import multiprocessing

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

numbers = [random.randint(1, 1000) for i in range(100)]

pool = multiprocessing.Pool(processes=100)

results_list = pool.map(is_prime, numbers)

count_primes = 0
for result in results_list:
    if result:
        count_primes += 1
        
print(numbers)        
print(f"Na liście jest {count_primes} liczb pierwszych")