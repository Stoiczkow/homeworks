from sqlalchemy.orm import Session
from sqlalchemy_app.database import get_db
from sqlalchemy_app.models import Tag, Zadanie

def pokaz_zadania(db: Session):
    """Wyświetla listę wszystkich zadań."""
    zadania = db.query(Zadanie).all() # Zamiast SELECT * FROM ...
    if not zadania:
        print("Brak zadań na liście.")
        return
    print("\n--- Twoja lista zadań ---")
    # ZADANIE NR3
    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}")
    # koniec zadania
    print("------------------------\n")

# ZADANIE 7
def wyszukaj_zadania(db: Session, fraza: str):
    """Wyszukuje zadania, których opis zawiera podaną frazę."""
    zadania = db.query(Zadanie).filter(Zadanie.opis.contains(fraza)).all()
    if not zadania:
        print("Nie znaleziono zadań pasujących do podanej frazy.")
        return

    print("\n--- Wyniki wyszukiwania ---")
    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}")
    print("---------------------------\n")
# koniec zadania


# ZADANIE 9
def dodaj_tag_do_zadania(db: Session, id_zadania: int, nazwa_taga: str):
    """Dodaje tag do wskazanego zadania."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if not zadanie:
        print("Nie znaleziono zadania o podanym ID.")
        return

    nazwa_taga = nazwa_taga.strip()
    if not nazwa_taga:
        print("Nazwa taga nie może być pusta.")
        return

    tag = db.query(Tag).filter(Tag.nazwa == nazwa_taga).first()
    if tag is None:
        tag = Tag(nazwa=nazwa_taga)
        db.add(tag)
        db.flush()

    if tag in zadanie.tagi:
        print("To zadanie ma już ten tag.")
        return

    zadanie.tagi.append(tag)
    db.commit()
    print("Tag został dodany do zadania!")
# koniec zadania


# ZADANIE 10
def edytuj_zadanie(db: Session, id_zadania: int, nowy_opis: str):
    """Aktualizuje opis wskazanego zadania."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if not zadanie:
        print("Nie znaleziono zadania o podanym ID.")
        return

    zadanie.opis = nowy_opis
    db.commit()
    print("Opis zadania został zaktualizowany!")
# koniec zadania

def dodaj_zadanie(db: Session, opis: str):
    """Dodaje nowe zadanie do bazy."""
    nowe_zadanie = Zadanie(opis=opis) # Tworzymy obiekt, a nie piszemy INSERT
    db.add(nowe_zadanie)
    db.commit()
    db.refresh(nowe_zadanie) # Odśwież, aby pobrać ID

def oznacz_jako_zrobione(db: Session, id_zadania: int):
    """Oznacza zadanie jako zrobione."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first() # Wyszukujemy obiekt
    if zadanie:
        zadanie.zrobione = True # Po prostu zmieniamy atrybut!
        db.commit()
        print("Zadanie zaktualizowane!")
    else:
        print("Nie znaleziono zadania o podanym ID.")

# ZADANIE NR2
def usun_zadanie(db: Session, id_zadania: int):
    """Usuwa zadanie z bazy danych po ID."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        db.delete(zadanie)
        db.commit()
        print("Zadanie usunięte!")
    else:
        print("Nie znaleziono zadania o podanym ID.")
# koniec zadania

def main():
    db_generator = get_db()
    db_session = next(db_generator)
    while True:
        print("Menu (SQLAlchemy):")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadania")
        print("6. Dodaj tag do zadania")
        print("7. Edytuj zadanie")
        print("8. Wyjdź")
  
        wybor = input("Wybierz opcję: ")
        if wybor == '1':
            pokaz_zadania(db_session)
        elif wybor == '2':
            opis = input("Podaj opis zadania: ")
            dodaj_zadanie(db_session, opis)
            print("Zadanie dodane!")
        elif wybor == '3':
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                oznacz_jako_zrobione(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '4':
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                usun_zadanie(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '5':
            fraza = input("Podaj frazę do wyszukania: ")
            wyszukaj_zadania(db_session, fraza)
        elif wybor == '6':
            try:
                id_zadania = int(input("Podaj ID zadania: "))
                nazwa_taga = input("Podaj nazwę taga: ")
                dodaj_tag_do_zadania(db_session, id_zadania, nazwa_taga)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '7':
            try:
                id_zadania = int(input("Podaj ID zadania do edycji: "))
                nowy_opis = input("Podaj nowy opis zadania: ")
                edytuj_zadanie(db_session, id_zadania, nowy_opis)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '8':
            print("Do zobaczenia!")
            db_session.close()
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")
        
if __name__ == "__main__":
    main()