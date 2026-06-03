import queue, threading
import random
import time 

running = True

def producer(numbers_q):  
    while running:  
        rand_number = random.randint(0, 1000)
        numbers_q.put(rand_number)           
        print(f"Producent (dodano): {rand_number},")
        time.sleep(1)
    
def consumer(numbers_q):
    while running:
        print(f"Konsument(pobrano): {numbers_q.get()},")
        time.sleep(1.5)
    
if __name__ == "__main__":
    numbers_q = queue.Queue()
    producer_tread = threading.Thread(target=producer, args=(numbers_q,))
    consumer_tread = threading.Thread(target=consumer, args=(numbers_q,))
    
    producer_tread.start()
    consumer_tread.start()
    
    time.sleep(10)
    running = False
        
    producer_tread.join()
    consumer_tread.join()
    
    print("Koniec programu")