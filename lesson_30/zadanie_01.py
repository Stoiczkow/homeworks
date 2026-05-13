import threading
import time


def thread_task() -> None:
    time.sleep(3)
    print("Wątek zakończył pracę!")


if __name__ == "__main__":
    worker = threading.Thread(target=thread_task)
    worker.start()
    print("Główny program czeka na wątek...")
    worker.join()
