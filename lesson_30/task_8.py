# Stwórz proces, który prosi użytkownika o podanie imienia (input()), a następnie wysyła to  imię do procesu nadrzędnego za pomocą multiprocessing.Queue. Proces nadrzędny odbiera imię i drukuje "Witaj, [imię]!".

# porces nadrzędzny to główny program 

from multiprocessing import Process, Queue

def my_name(wynik):
    wynik.put("hello")

if __name__ == "__main__":

    wyniki_q = Queue()

    p = Process(target=my_name, args=(wyniki_q, ))
    p.start()
    p.join()

    print(wyniki_q.get())