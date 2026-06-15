import multiprocessing


def prepare_greeting(name, queue):
    message = f"Witaj, {name}!"
    queue.put(message)


if __name__ == "__main__":
    queue = multiprocessing.Queue()

    name = input("Podaj imię: ")

    process = multiprocessing.Process(
        target=prepare_greeting,
        args=(name, queue)
    )

    process.start()

    message = queue.get()

    process.join()

    print(message)