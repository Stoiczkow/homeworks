# Użyj multiprocessing.Pipe do stworzenia dwukierunkowej komunikacji. Proces nadrzędny
# wysyła do procesu potomnego listę liczb. Proces potomny oblicza ich sumę i średnią, a
# następnie odsyła krotkę z wynikami ((suma, srednia)) do procesu nadrzędnego, który je
# drukuje.

from multiprocessing import Pipe, Process


def oblicz_wyniki(conn):
	liczby = conn.recv()
	suma = sum(liczby)
	srednia = suma / len(liczby) if liczby else 0
	conn.send((suma, srednia))
	conn.close()


if __name__ == "__main__":
	parent_conn, child_conn = Pipe()

	proces = Process(target=oblicz_wyniki, args=(child_conn,))
	proces.start()

	liczby = [10, 20, 30, 40, 50]
	parent_conn.send(liczby)

	wyniki = parent_conn.recv()
	print(wyniki)

	parent_conn.close()
	proces.join()

