import threading
import time


def worker():
    time.sleep(3)
    print("Wątek zakończył pracę!")


thread = threading.Thread(target=worker)

thread.start()

print("Główny program czeka na wątek...")

thread.join()

print("Program główny zakończył działanie.")