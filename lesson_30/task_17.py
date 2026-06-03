# 17. Użyj multiprocessing.Pipe do stworzenia dwukierunkowej komunikacji. Proces nadrzędny
# wysyła do procesu potomnego listę liczb. Proces potomny oblicza ich sumę i średnią, a
# następnie odsyła krotkę z wynikami ((suma, srednia)) do procesu nadrzędnego, który je
# drukuje

from multiprocessing import Process, Pipe


def child(conn):
    data = conn.recv()
    print("Child received:", data)

    numbers_sum = sum(data)
    numbers_avg = numbers_sum / len(data)

    conn.send((numbers_sum, numbers_avg))
    conn.close()


if __name__ == "__main__":

    numbers = list(range(1, 10))

    parent_conn, child_conn = Pipe()

    p = Process(target=child, args=(child_conn,))
    p.start()

    parent_conn.send(numbers)

    result = parent_conn.recv()

    print("Parent received results:")
    print(f"sum: {result[0]}")
    print(f"avg: {result[1]}")

    p.join()