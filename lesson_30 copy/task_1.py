# Zadanie 1 – Pierwszy wątek
# Napisz program, który tworzy i uruchamia jeden wątek. Wątek powinien odczekać 3
# sekundy, a następnie wydrukować komunikat "Wątek zakończył pracę!". Główny program
# powinien w tym czasie wyświetlić "Główny program czeka na wątek...".


import threading
import time

def zadanie_dla_watku():
    print("Wątek zaczyna swoją pracę.")
    time.sleep(3)
    print("Wątek zakończył swoją pracę.")

thread = threading.Thread(target=zadanie_dla_watku)

thread.start()

print("Główny program czeka na wątek")

thread.join()

print("Główny program zakończył pracę.")


# import threading
# import time

# def my_thread():
#     time.sleep(3)
#     print("Wątek zakończył pracę!")

# thread = threading.Thread(target=my_thread)

# thread.start()

# thread.join()

# print("Główny program czeka na wątek...")