# ✏ Zadanie 1 – Pierwszy wątek
# Napisz program, który tworzy i uruchamia jeden wątek. Wątek powinien odczekać 3
# sekundy, a następnie wydrukować komunikat "Wątek zakończył pracę!". Główny program
# powinien w tym czasie wyświetlić "Główny program czeka na wątek...".

# Zadanie 2 – Wiele wątków
# Stwórz program, który uruchamia 5 wątków. Każdy wątek powinien otrzymać jako argument # swój numer (od 1 do 5) i wydrukować komunikat "Jestem wątkiem numer [numer]". Upewnij # się, że główny program czeka na zakończenie wszystkich wątków.

import threading
import time

def my_thread():
    time.sleep(3)
    print(f"Wątek zakończył pracę!")

thred = threading.Thread(target=my_thread)

thred.start()


thred.join()

# Zad 2

import threading
import time

def my_thread(args):
    time.sleep(3)
    print(f"Wątek {args} zakończył pracę!")

for i in range(1,6):
    thred = threading.Thread(target=my_thread, args=(i,))
    thred.start()


thred.join()
