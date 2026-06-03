import threading

data = [
    range(250000),
    range(250000, 500000),
    range(500000, 750000),
    range(750000, 1000000),
]

result = 0

lock = threading.Lock()

def sum_elements(elements):
    global result
    partial = sum(elements) 
    
    with lock:
        result += partial
        

threads = []

for i in range(4):
    thread = threading.Thread(target=sum_elements, args=(data[i],))
    threads.append(thread)
    thread.start()
    
for t in threads:
    t.join()
    
print(f"Wynik końcowy {result}")
print(f"Wynik testowy {sum(range(0, 1000000))}")