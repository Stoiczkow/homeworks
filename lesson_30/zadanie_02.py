import threading


def introduce(number: int) -> None:
    print(f"Jestem wątkiem numer {number}")


if __name__ == "__main__":
    threads = []
    for i in range(1, 6):
        thread = threading.Thread(target=introduce, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Wszystkie wątki zakończyły pracę.")
