import threading
import time
import queue
import random

from multiprocessing import Pool
# #task1
# def zadanie_dla_watku():

#     time.sleep(3) 
#     print("Wątek kończy pracę.")


# watek = threading.Thread(target=zadanie_dla_watku)

# watek.start()

# print("Główny program czeka na wątek...")

# watek.join()


# #task2

# # Stwórz program, który uruchamia 5 wątków. Każdy wątek powinien otrzymać jako argument
# # swój numer (od 1 do 5) i wydrukować komunikat "Jestem wątkiem numer [numer]". Upewnij
# # się, że główny program czeka na zakończenie wszystkich wątków.

# def zadanie_dla_watku(numer_watku):

#     print(f"Jestem wątkiem numer: {numer_watku}")
#     time.sleep(1) 
#     print("Wątek kończy pracę.")


# watki = []

# for i in range(1,6):
#     thread = threading.Thread(target=zadanie_dla_watku, args=(i,))
#     watki.append(thread)
#     thread.start()

# for thread in watki:
#     thread.join()


# # zadanie 3.

# def pobierz_dane(id_danych):
#     print(f"pobieranie danych {id_danych}")
#     time.sleep(2)

# lista_danych = [21, 22, 23]

# start_timer = time.time()

# for i in lista_danych:
#     pobierz_dane(i)

# end_timer = time.time()

# timer_sekwencyjnie = end_timer - start_timer
# print(timer_sekwencyjnie)

# watki = []
# start_timer_watki = time.time()
# for i in lista_danych:

#     watek = threading.Thread(target=pobierz_dane, args=(i,))
#     watki.append(watek)
#     watek.start()


##task4

# list_ = []

# def add_to_list_1():
#     for _ in range(100000):
#         list_.append(1)
        
# def add_to_list_1():
#     for _ in range(100000):
#             list_.append(2)

# watek1 = threading.Thread(target=add_to_list_1)

# watek2 = threading.Thread(target=add_to_list_1)
# watek1.start()
# watek2.start()

# watek1.join()
# watek2.join()



# print(len(list_))

##5


# #task6

# import multiprocessing
# import math


# def calculate_factorial():
#     wynik = math.factorial(10)
#     print(f"Silnia z 10 wynosi: {wynik}")


# if __name__ == "__main__":
#     process = multiprocessing.Process(target=calculate_factorial)

#     process.start()

#     process.join()

# #task7

# import multiprocessing


# def potega(liczba, pot):
#     print(liczba**pot)


# if __name__ == "__main__":
#     proccess = multiprocessing.Process(target=potega, args=(5, 3))

#     proccess.start()
#     proccess.join()

##task8

# from multiprocessing import Process, Queue

# def my_name(wynik):
#     wynik.put("hello")

# if __name__ == "__main__":

#     wyniki_q = Queue()

#     p = Process(target=my_name, args=(wyniki_q, ))
#     p.start()
#     p.join()

#     print(wyniki_q.get())

# #9

# import threading

# data = [
#     range(250000),
#     range(250000, 500000),
#     range(500000, 750000),
#     range(750000, 1000000),
# ]


# result = 0

# lock = threading.Lock()


# def sum_elements(data):
#     global result
#     with lock:
#         result += sum(data)


# threads = []

# for i in range(4):
#     thread = threading.Thread(target=sum_elements, args=(data[i],))
#     threads.append(thread)
#     thread.start()


# for t in threads:
#     t.join()

# print(f"Wynik końcowy {result}")
# print(f"Wynik testowy {sum(range(0, 1000000))}")

# # Zadanie 10 – Równoległe liczenie słów w plikach


# from pathlib import Path
# import threading

# result = 0
# lock = threading.Lock()

# word = input("Jakiego słowa szukamy? ")

# p = Path.cwd()

# object_list = list(p.glob('**/*.txt'))
# path_list = []

# for i in object_list:
#     path_list.append(i.absolute())

# def searching_word(word, file):
#     with open(file, encoding="UTF-8", mode="r") as txtfile:
#         global result
#         content = txtfile.read()
#         with lock:
#             result += content.count(word)

# threads = []

# for file in path_list:
#     thread = threading.Thread(target=searching_word, args=(word, file))
#     thread.start()
#     threads.append(thread)

# for t in threads:
#     t.join()

# print(result)

#zad 11


# def producent(kolejka, stop_event):
#     "Wątek producenta ktory dodaje losowy element (liczbe) do kolejki co 1 sekundę."
#     while not stop_event.is_set():
#         liczba = random.randint(1, 100)
#         kolejka.put(liczba)
#         print(f"Producent: liczba {liczba} zostala dodana")
#         time.sleep(1)
#     print("Producent: koniec")

# def konsument(kolejka, stop_event):
#     "Wątek konsumenta ktory odpowiada za  pobranie i wyswietlenie elementu co 1.5 sekundy."
#     while not stop_event.is_set() or not kolejka.empty():
#         try:
#             element = kolejka.get(timeout=0.5)
#             print(f"Konsyment Producent: liczba {element} zostala dodana")
#             kolejka.task_done()
#         except queue.Empty:
#             continue
#         time.sleep(1.5)
#     print("Konsument: koniec")

# if __name__ == "__main__":
#     wspolna_kolejka = queue.Queue()
    
#     stop_sygnal = threading.Event()

#     watek_producenta = threading.Thread(target=producent, args=(wspolna_kolejka, stop_sygnal))
#     watek_konsumenta = threading.Thread(target=konsument, args=(wspolna_kolejka, stop_sygnal))

#     print("Start:")
#     watek_producenta.start()
#     watek_konsumenta.start()

#     time.sleep(10)

#     stop_sygnal.set()

#     watek_producenta.join()
#     watek_konsumenta.join()

#     print("Zakonczenie dzialania programu")


#zad 13
# import random
# from multiprocessing import Pool

# def liczba_pierwsz(number):
#     if number <= 1:
#         return False
#     if number <= 3:
#         return True
#     if number % 2 == 0 or number % 3 == 0:
#         return False
    
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# if __name__ == '__main__':
#     random_numbers = [random.randint(1, 1000) for _ in range(100)]
    
#     print("Wygenerowane liczby:")
#     print(random_numbers)
#     print("-" * 50)
    
#     with Pool() as pool:
#         results = pool.map(liczba_pierwsz, random_numbers)

#     prime_count = sum(results)
#     print(f"Liczby pierwsze: {prime_count}")
    
#     primes = []
#     for i in range(len(random_numbers)):
#         if results[i] == True:
#             primes.append(random_numbers[i])

#     print(f"Te liczby to: {primes}")

# #14
# import os
# import shutil
# import threading


# def kopiuj_plik(sciezka_zrodlowa, sciezka_docelowa, nazwa_pliku):
#     """Funkcja wykonywana przez pojedynczy wątek."""
#     pelna_sciezka_zrodlo = os.path.join(sciezka_zrodlowa, nazwa_pliku)
#     pelna_sciezka_cel = os.path.join(sciezka_docelowa, nazwa_pliku)

#     print(f"Watek kopiowanie pliku{nazwa_pliku}...")

#     try:
#         shutil.copy2(pelna_sciezka_zrodlo, pelna_sciezka_cel)
#         print(f"Watek ukończono kopiowanie pliku {nazwa_pliku}.")
#     except Exception as e:
#         print(f"Error:  kopiowanie nie powiodlo sie {nazwa_pliku}: {e}")


# def kopiuj_katalog(katalog_zrodlowy, katalog_docelowy):
#     if not os.path.exists(katalog_zrodlowy):
#         print(f"Error: Katalog docelowy '{katalog_zrodlowy}' nie istnieje.")
#         return

#     if not os.path.exists(katalog_docelowy):
#         os.makedirs(katalog_docelowy)
#         print(f"Utworzenie katalog docelowego: {katalog_docelowy}")

#     wszystkie_elementy = os.listdir(katalog_zrodlowy)

#     pliki = [
#         f
#         for f in wszystkie_elementy
#         if os.path.isfile(os.path.join(katalog_zrodlowy, f))
#     ]

#     if not pliki:
#         print("Brak plików do skopiowania w katalogu glownym.")
#         return

#     print(
#         f"Znaleziono {len(pliki)} plików. Uruchamianie wątków kopiujących...\n"
#     )

#     lista_watkow = []

#     for plik in pliki:
#         watek = threading.Thread(
#             target=kopiuj_plik,
#             args=(katalog_zrodlowy, katalog_docelowy, plik),
#         )
#         lista_watkow.append(watek)
#         watek.start() 

#     for watek in lista_watkow:
#         watek.join()

#     print("Program zakonczyl sie  sukcesem")

# if __name__ == "__main__":
#     kopiuj_katalog("./katalog_A", "./katalog_B")

#17

import multiprocessing

def proces_potomny(pipe_koniec):

    liczby = pipe_koniec.recv()
    
    if liczby:
        suma = sum(liczby)
        srednia = suma / len(liczby)
    else:
        suma, srednia = 0, 0.0
        
    pipe_koniec.send((suma, srednia))
    
    pipe_koniec.close()

if __name__ == "__main__":
    rodzic_conn, potomny_conn = multiprocessing.Pipe()
    
    liczby_do_wyslania = [10, 20, 30, 40, 50]
    
    proces = multiprocessing.Process(target=proces_potomny, args=(potomny_conn,))
    proces.start()
    
    print(f"lista liczb: {liczby_do_wyslania}")
    rodzic_conn.send(liczby_do_wyslania)
    
    wynik_suma, wynik_srednia = rodzic_conn.recv()
    
    print(f"wyniki:")
    print(f"  - Suma: {wynik_suma}")
    print(f"  - Średnia: {wynik_srednia}")
    
    proces.join()
    rodzic_conn.close()




#18

# class konto_bankowe:

#     def __init__(self, saldo_start):
#         self.saldo_konta = saldo_start
#         self.blokada = threading.Lock()

#     def wplac(self, kwota):
#         with self.blokada:
#             stare_saldo = self.saldo_konta
#             self.saldo_konta += kwota

#     def wyplac(self, kwota):
#         with self.blokada:
#             if self.saldo_konta >= kwota:
#                 stare_saldo = self.saldo_konta
#                 self.saldo_konta -= kwota

#     def saldo(self):
#         return self.saldo_konta


# def watek_wplac(konto):
#     money = random.randrange(1, 1000)
#     konto.wplac(money)


# def watek_wyplac(konto):
#     money = random.randrange(1, 1000)
#     konto.wyplac(money)
 
# if __name__ == "__main__":
#     konto_01 = konto_bankowe(1000)
#     print(f"Kwota poczatkowa na koncie {konto_01.saldo()} zl")

#     lista_watkow = []


#     for i in range(5):
#         watek = threading.Thread(target=watek_wplac, args=(konto_01,))
#         lista_watkow.append(watek)


#     for i in range(5):
#         watek = threading.Thread(target=watek_wyplac, args=(konto_01,))
#         lista_watkow.append(watek)

#     for watek in lista_watkow:
#         watek.start()


#     for watek in lista_watkow:
#         watek.join()

#     print(f"Stan konta na koniec operacji {konto_01.saldo()} zł")