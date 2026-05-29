"""
Zadanie 17 – Komunikacja dwukierunkowa (Pipe)
Proces nadrzędny wysyła listę liczb do procesu potomnego.
Proces potomny oblicza sumę i średnią, odsyła krotkę (suma, srednia).
"""
import multiprocessing


def oblicz_statystyki(polaczenie):
    liczby = polaczenie.recv()
    suma = sum(liczby)
    srednia = suma / len(liczby) if liczby else 0
    polaczenie.send((suma, srednia))
    polaczenie.close()


if __name__ == '__main__':
    conn_rodzic, conn_dziecko = multiprocessing.Pipe()

    p = multiprocessing.Process(target=oblicz_statystyki, args=(conn_dziecko,))
    p.start()

    liczby = list(range(1, 101))  # liczby 1–100
    print(f"Wysyłam listę {len(liczby)} liczb do procesu potomnego...")
    conn_rodzic.send(liczby)

    suma, srednia = conn_rodzic.recv()
    print(f"Suma:    {suma}")
    print(f"Średnia: {srednia:.2f}")

    p.join()
    conn_rodzic.close()
