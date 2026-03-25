from database_raw import TaskManagerRaw


# ZADANIE 8
class TaskAppRaw:
    """Prosta aplikacja konsolowa do obsługi listy zadań."""

    def __init__(self):
        self.manager = TaskManagerRaw()

    def pokaz_zadania(self):
        """Wyświetla listę wszystkich zadań."""
        zadania = self.manager.pobierz_zadania()
        if not zadania:
            print("Brak zadań na liście.")
            return
        print("\n--- Twoja lista zadań ---")
        for zadanie in zadania:
            status = "✓" if zadanie[2] else "✗"
            print(f"[{status}] ID: {zadanie[0]}, Opis: {zadanie[1]}")
        print("------------------------\n")

    def wyszukaj_zadania(self):
        """Wyszukuje zadania po fragmencie opisu."""
        fraza = input("Podaj frazę do wyszukania: ")
        zadania = self.manager.wyszukaj_zadania(fraza)
        if not zadania:
            print("Nie znaleziono zadań pasujących do podanej frazy.")
            return

        print("\n--- Wyniki wyszukiwania ---")
        for zadanie in zadania:
            status = "✓" if zadanie[2] else "✗"
            print(f"[{status}] ID: {zadanie[0]}, Opis: {zadanie[1]}")
        print("---------------------------\n")

    def uruchom(self):
        """Uruchamia główną pętlę aplikacji."""
        while True:
            print("Menu:")
            print("1. Pokaż zadania")
            print("2. Dodaj zadanie")
            print("3. Oznacz zadanie jako zrobione")
            print("4. Usuń zadanie")
            print("5. Wyszukaj zadania")
            print("6. Wyjdź")

            wybor = input("Wybierz opcję: ")
            if wybor == '1':
                self.pokaz_zadania()
            elif wybor == '2':
                opis = input("Podaj opis zadania: ")
                try:
                    priorytet = int(input("Podaj priorytet zadania: "))
                    self.manager.dodaj_zadanie(opis, priorytet)
                    print("Zadanie dodane!")
                except ValueError:
                    print("Błędny priorytet. Podaj liczbę.")
            elif wybor == '3':
                try:
                    id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                    self.manager.oznacz_jako_zrobione(id_zadania)
                    print("Zadanie zaktualizowane!")
                except ValueError:
                    print("Błędne ID. Podaj liczbę.")
            elif wybor == '4':
                try:
                    id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                    liczba_usunietych = self.manager.usun_zadanie(id_zadania)
                    if liczba_usunietych:
                        print("Zadanie usunięte!")
                    else:
                        print("Nie znaleziono zadania o podanym ID.")
                except ValueError:
                    print("Błędne ID. Podaj liczbę.")
            elif wybor == '5':
                self.wyszukaj_zadania()
            elif wybor == '6':
                print("Do zobaczenia!")
                break
            else:
                print("Nieznana opcja, spróbuj ponownie.")
# koniec zadania


def main():
    app = TaskAppRaw()
    app.uruchom()


if __name__ == "__main__":
    main()