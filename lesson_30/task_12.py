import time
import threading, multiprocessing


def intensywne_obliczenia(n):
    print("Proces startuje...")
    suma = sum(i * i for i in range(n))
    print(f"Proces zakończył, suma: {suma}")
    

if __name__ == "__main__":
    start = time.time()
    
    intensywne_obliczenia(20000000)
    intensywne_obliczenia(20000000)

    print(f"Czas wykonania sekwencyjnie: {time.time() - start:.2f}")

    t1 = threading.Thread(target=intensywne_obliczenia, args=(20000000,))
    t2 = threading.Thread(target=intensywne_obliczenia, args=(20000000,))
    
    start = time.time()
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print(f"Czas wykonania w 2 wątkach: {time.time() - start:.2f}")
    
    p1 = multiprocessing.Process(target=intensywne_obliczenia, args=(20000000,))
    p2 = multiprocessing.Process(target=intensywne_obliczenia, args=(20000000,))
    
    start = time.time()
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f"Czas wykonania w 2 procesach: {time.time() - start:.2f}")
    
    # Czas wykonania sekwencyjnie i w 2 wątkach jest podobny ( w wątkach trochę większy), ponieważ w wątkach obliczenia nie wykonują się równolegle, gdyż GIL blokuje i w danym momencie może działać tylko 1 wątek.
    # inaczej jest przy multiprocessingu, wtedy czas jest o połowę mniejszy niż sekwencyjnie, ponieważ obliczenia wykonują się równolegle w 2 procesach.