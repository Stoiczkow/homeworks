# Stwórz proces, który prosi użytkownika o podanie imienia (input()), a następnie wysyła to
# imię do procesu nadrzędnego za pomocą multiprocessing.Queue. Proces nadrzędny
# odbiera imię i drukuje "Witaj, [imię]!".

import multiprocessing


def child_process(queue):
    """Proces potomny - prosi o imię i wysyła do kolejki"""
    name = input("Podaj swoje imię: ")
    queue.put(name)


if __name__ == "__main__":
    # Tworzenie kolejki
    queue = multiprocessing.Queue()
    
    # Tworzenie i uruchamianie procesu potomnego
    process = multiprocessing.Process(target=child_process, args=(queue,))
    process.start()
    
    # Proces nadrzędny odbiera imię z kolejki
    name = queue.get()
    print(f"Witaj, {name}!")
    
    # Czekanie na zakończenie procesu potomnego
    process.join()

