# Zadanie 8 (uwaga zepsuta treść polecenia)

from multiprocessing import Process, Queue

def my_name(wynik):
    wynik.put("hello")

if __name__ == "__main__":

    wyniki_q = Queue()

    p = Process(target=my_name, args=(wyniki_q, ))
    p.start()
    p.join()

    print(wyniki_q.get())