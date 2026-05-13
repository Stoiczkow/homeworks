import threading

shared_list: list[int] = []
lock = threading.Lock()


def append_value(value: int, times: int) -> None:
    for _ in range(times):
        with lock:
            shared_list.append(value)


if __name__ == "__main__":
    for attempt in range(1, 4):
        shared_list.clear()

        t1 = threading.Thread(target=append_value, args=(1, 100_000))
        t2 = threading.Thread(target=append_value, args=(2, 100_000))

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        print(f"Próba {attempt}: długość listy = {len(shared_list)}")