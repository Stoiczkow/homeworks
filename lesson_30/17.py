# Zadanie 17 – Komunikacja dwukierunkowa (Pipe)
# Użyj multiprocessing.Pipe do stworzenia dwukierunkowej komunikacji. Proces nadrzędny
# wysyła do procesu potomnego listę liczb. Proces potomny oblicza ich sumę i średnią, a
# następnie odsyła krotkę z wynikami ((suma, srednia)) do procesu nadrzędnego, który je
# drukuje.

from multiprocessing import Process, Pipe
from statistics import mean
import random


def calculate(conn):
    data = conn.recv()
    data_sum = sum(data)
    data_av = round(mean(data), ndigits=2)
    conn.send((data_sum, data_av))
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    child_process = Process(target=calculate, args=(child_conn, ))
    child_process.start()

    int_list = []
    for n in range(30):
        int_list.append(random.randint(0, 100))

    parent_conn.send(int_list)
    
    results = parent_conn.recv()

    print(f"Odebrane wyniki (Suma, Średnia): {results}")

    parent_conn.close()
    child_process.join()