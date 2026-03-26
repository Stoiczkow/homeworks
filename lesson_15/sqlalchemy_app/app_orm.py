from sqlalchemy.orm import Session
from database import get_db
from models import Zadanie, Tag


def pokaz_zadania(db: Session):
    """Wyświetla listę wszystkich zadań."""
    zadania = db.query(Zadanie).all()
    if not zadania:
        print("Brak zadań na liście.")
        return

    print("\n--- Twoja lista zadań ---")
    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        tagi = ", ".join([t.nazwa for t in zadanie.tagi]) if zadanie.tagi else "brak"
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}, Priorytet: {zadanie.priorytet}, Tagi: [{tagi}]")
    print("------------------------\n")


def dodaj_zadanie(db: Session, opis: str, priorytet: int):
    """Dodaje nowe zadanie do bazy."""
    nowe_zadanie = Zadanie(opis=opis, priorytet=priorytet)
    db.add(nowe_zadanie)
    db.commit()
    db.refresh(nowe_zadanie)


def oznacz_jako_zrobione(db: Session, id_zadania: int):
    """Oznacza zadanie jako zrobione."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        zadanie.zrobione = True
        db.commit()
        print("Zadanie zaktualizowane!")
    else:
        print("Nie znaleziono zadania o podanym ID.")


def wyszukaj_zadania(db: Session, fraza: str):
    zadania = db.query(Zadanie).filter(Zadanie.opis.contains(fraza)).all()
    if not zadania:
        print(f"Brak zadań o opisie: {fraza}.")
        return
    print("\n--- Twoja lista zadań ---")
    for zadanie in zadania:
        print(f" ID: {zadanie.id}, Opis: {zadanie.opis}")
    print("------------------------\n")


def usun_zadanie(db: Session, id_zadania: int):
    """Usuń zadanie o podanym ID."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        db.delete(zadanie)
        db.commit()
        print(f"Zadanie o ID: {zadanie.id} zostało usunięte.")
    else:
        print("Nie znaleziono zadania o podanym ID.")


def dodaj_tag_do_zadania(db: Session, id_zadania: int, nazwa_tagu: str):
    """Dodaje tag do zadania. Tworzy tag, jeśli nie istnieje."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if not zadanie:
        print("Nie znaleziono zadania o podanym ID.")
        return

    tag = db.query(Tag).filter(Tag.nazwa == nazwa_tagu).first()
    if not tag:
        tag = Tag(nazwa=nazwa_tagu)
        db.add(tag)

    if tag not in zadanie.tagi:
        zadanie.tagi.append(tag)
        db.commit()
        print(f"Tag '{nazwa_tagu}' dodany do zadania ID: {id_zadania}.")
    else:
        print(f"Tag '{nazwa_tagu}' jest już przypisany do tego zadania.")


def pokaz_tagi(db: Session):
    """Wyświetla wszystkie tagi."""
    tagi = db.query(Tag).all()
    if not tagi:
        print("Brak tagów.")
        return
    print("\n--- Lista tagów ---")
    for tag in tagi:
        print(f"ID: {tag.id}, Nazwa: {tag.nazwa}")
    print("-------------------\n")


def edytuj_zadanie(db: Session, id_zadania: int, nowy_opis: str):
    """Edytuje opis zadania o podanym ID."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        zadanie.opis = nowy_opis
        db.commit()
        print(f"Zadanie ID: {id_zadania} zaktualizowane!")
    else:
        print("Nie znaleziono zadania o podanym ID.")


def main():
    db_generator = get_db()
    db_session = next(db_generator)

    while True:
        print("Menu (SQLAlchemy):")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Wyszukaj zadania")
        print("5. Usuń zadanie")
        print("6. Dodaj tag do zadania")
        print("7. Pokaż tagi")
        print("8. Edytuj zadanie")
        print("9. Wyjdź")
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            pokaz_zadania(db_session)
        elif wybor == '2':
            opis = input("Podaj opis zadania: ")
            priorytet = int(input("Podaj priorytet zadania: "))
            dodaj_zadanie(db_session, opis, priorytet)
            print("Zadanie dodane!")
        elif wybor == '3':
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                oznacz_jako_zrobione(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '4':
            fraza = input("Podaj frazę do wyszukania: ")
            wyszukaj_zadania(db_session, fraza)
        elif wybor == '5':
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                usun_zadanie(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '6':
            try:
                id_zadania = int(input("Podaj ID zadania: "))
                nazwa_tagu = input("Podaj nazwę tagu: ")
                dodaj_tag_do_zadania(db_session, id_zadania, nazwa_tagu)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '7':
            pokaz_tagi(db_session)
        elif wybor == '8':
            try:
                id_zadania = int(input("Podaj ID zadania do edycji: "))
                nowy_opis = input("Podaj nowy opis zadania: ")
                edytuj_zadanie(db_session, id_zadania, nowy_opis)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '9':
            print("Do zobaczenia!")
            db_session.close()
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()