from multiprocessing import Pipe, Process
from multiprocessing.connection import Connection


def worker(connection: Connection) -> None:
    numbers = connection.recv()
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    connection.send((total, average))
    connection.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    process = Process(target=worker, args=(child_conn,))
    process.start()

    parent_conn.send([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    total, average = parent_conn.recv()
    print(f"Suma: {total}")
    print(f"Średnia: {average}")

    process.join()