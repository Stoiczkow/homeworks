import multiprocessing


def calculate_sum_and_average(child_connection):
    numbers = child_connection.recv()

    total = sum(numbers)
    average = total / len(numbers)

    child_connection.send((total, average))

    child_connection.close()


if __name__ == "__main__":
    parent_connection, child_connection = multiprocessing.Pipe()

    process = multiprocessing.Process(
        target=calculate_sum_and_average,
        args=(child_connection,)
    )

    process.start()

    numbers = [10, 20, 30, 40, 50]

    parent_connection.send(numbers)

    result = parent_connection.recv()

    process.join()

    parent_connection.close()

    total, average = result

    print(f"Liczby: {numbers}")
    print(f"Suma: {total}")
    print(f"Średnia: {average}")