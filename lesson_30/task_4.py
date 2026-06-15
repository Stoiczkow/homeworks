import threading


numbers = []


def add_ones():
    for _ in range(100_000):
        numbers.append(1)


def add_twos():
    for _ in range(100_000):
        numbers.append(2)


thread_1 = threading.Thread(target=add_ones)
thread_2 = threading.Thread(target=add_twos)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f"Długość listy: {len(numbers)}")
print("Oczekiwana długość: 200000")

print(f"Liczba jedynek: {numbers.count(1)}")
print(f"Liczba dwójek: {numbers.count(2)}")