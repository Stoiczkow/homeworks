# Zadanie 2 – Wiele wątków
# Zadania trudniejsze (challenge)
# Stwórz program, który uruchamia 5 wątków. Każdy wątek powinien otrzymać jako argument
# swój numer (od 1 do 5) i wydrukować komunikat "Jestem wątkiem numer [numer]". Upewnij
# się, że główny program czeka na zakończenie wszystkich wątków.

import threading
import time

def wait(number):
    print(f"Jestem wątkiem numer {number}")

for i in range (1, 6):
    thread = threading.Thread(target=wait, args=(i, ))
    thread.start()

thread.join()