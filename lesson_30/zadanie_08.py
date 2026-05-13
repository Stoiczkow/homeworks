import multiprocessing


def ask_for_name(queue: multiprocessing.Queue) -> None:
    name = input("Podaj swoje imię: ")
    queue.put(name)


if __name__ == "__main__":
    queue: multiprocessing.Queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=ask_for_name, args=(queue,))
    process.start()
    process.join()

    name = queue.get()
    print(f"Witaj, {name}!")
