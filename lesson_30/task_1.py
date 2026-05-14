#  Zadanie 1 – Pierwszy wątek
# Napisz program, który tworzy i uruchamia jeden wątek. Wątek powinien odczekać 3
# sekundy, a następnie wydrukować komunikat "Wątek zakończył pracę!". Główny program powinien w tym czasie wyświetlić "Główny program czeka na wątek...".

import threading
import time

def my_thread(args):
    time.sleep(3)
    print(f"Wątek {args} zakończył pracę!")

print("Główny program czeka na wątek...")
threads = []
for i in range(1,6):
    thred = threading.Thread(target=my_thread, args=(i,))
    thred.start()
    threads.append(thred)

for thred in threads:
    thred.join()