# Stwórz program, który uruchamia 5 wątków. Każdy wątek powinien otrzymać jako argument
# swój numer (od 1 do 5) i wydrukować komunikat "Jestem wątkiem numer [numer]". Upewnij
# się, że główny program czeka na zakończenie wszystkich wątków.
import threading

def my_thread(args):
    print(f"Jestem wątkiem numer {args}")

threads = []
for i in range(1, 6):
    thred = threading.Thread(target=my_thread, args=(i,))
    thred.start()
    threads.append(thred)

for thred in threads:
    thred.join()
