import threading 
import time

def my_thread(i):
    time.sleep(3)
    print(f"Wątek {i} zakończył pracę!")

threads = []

for i in range(1, 6):    
    thread = threading.Thread(target=my_thread, args=(i,))
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()