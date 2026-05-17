import threading
import time

def wait():
    print("Rozpoczynam czekanie")
    time.sleep(3)
    print("Kończę czekanie")

thread = threading.Thread(target=wait)

thread.start()