# Zaimplementuj klasyczny problem producenta-konsumenta. Stwórz współdzieloną,
# bezpieczną wątkowo kolejkę (import queue; q = queue.Queue()). "Producent" to wątek,
# który co sekundę dodaje do kolejki nowy element (np. losową liczbę). "Konsument" to
# wątek, który co 1.5 sekundy pobiera element z kolejki i go drukuje. Program powinien
# działać przez 10 sekund.

import queue
import random
import threading
import time


q = queue.Queue()


def producer(end_time):
	while time.monotonic() < end_time:
		item = random.randint(1, 100)
		q.put(item)
		print(f"Producent dodał: {item}")

		remaining = end_time - time.monotonic()
		if remaining > 0:
			time.sleep(min(1, remaining))


def consumer(end_time):
	while time.monotonic() < end_time:
		remaining = end_time - time.monotonic()
		if remaining <= 0:
			break

		try:
			item = q.get(timeout=min(0.5, remaining))
			print(f"Konsument pobrał: {item}")
			q.task_done()
		except queue.Empty:
			pass

		remaining = end_time - time.monotonic()
		if remaining > 0:
			time.sleep(min(1.5, remaining))


def main():
	end_time = time.monotonic() + 10

	producer_thread = threading.Thread(target=producer, args=(end_time,))
	consumer_thread = threading.Thread(target=consumer, args=(end_time,))

	producer_thread.start()
	consumer_thread.start()

	producer_thread.join()
	consumer_thread.join()


if __name__ == "__main__":
	main()

