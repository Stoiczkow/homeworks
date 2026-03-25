from sqlalchemy.orm import Session
from database import get_db
from models import Zadania, Tag, ZadaniaTag

def pokaz_zadania(db: Session):
    zadania = db.query(Zadania).all()

    if not zadania:
        print("Brak zdefiniowanych zadań!")
        return

    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗" # type: ignore
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}, Data utworzenia: {zadanie.data_utworzenia}, Tagi: {zadanie.tags}")

def pokaz_tagi(db: Session):
    tags = db.query(Tag).all()

    print("=== Twoje tagi ===")
    for tag in tags:
        print(f"ID: {tag.id}, Nazwa: {tag.nazwa}, Zadanie: {tag.zadania}")

# Zadanie 7
def filtruj_zadania_po_opisie(db: Session, fraza):
    zadania = db.query(Zadania).filter(Zadania.opis.contains(fraza)).all()

    if zadania:
        for zadanie in zadania:
            status = "✓" if zadanie.zrobione else "✗" # type: ignore
            print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}, Data utworzenia: {zadanie.data_utworzenia}")
    else:
        print(f"Nie znaleziono zadań z frazą {fraza} w opinie")

# Zadanie 2 – Usuwanie zadań (SQLAlchemy)
# Zrób to samo dla aplikacji app_orm.py. Funkcja w warstwie danych powinna znaleźć obiekt
# zadania, a następnie użyć db.delete(obiekt_zadania) i db.commit()
def usun_zadanie(db: Session, id_zadania: int):
    zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).first()
    # ponizej można zrobić to jedna linia
    # zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).delete()
    if not zadanie:
        print("Nie znaleziono takiego zadania")
        return
    
    db.delete(zadanie)
    db.commit()

def dodaj_zadanie(db: Session, nowy_opis: str):
    nowe_zadanie = Zadania(opis = nowy_opis)
    db.add(nowe_zadanie)
    db.commit()
    db.refresh(nowe_zadanie)

def edytuj_zadanie(db: Session, id_zadania: int, nowy_opis: str):
    zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).first()

    if not zadanie:
        print("Nie ma takiego zadania")
        return

    zadanie.opis = nowy_opis # type: ignore
    db.commit()
    print("Opis zadania został zaktualizowany")

def oznacz_jako_zrobione(db: Session, id_zadania: int):
    zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).first()

    if zadanie:
        zadanie.zrobione = True # type: ignore
        db.commit()
        print("Zadanie zaktualizowane")
    else:
        print("Nie ma takiego zadania")

def dodaj_tag(db: Session, nowa_nazwa: str):
    nowy_tag = Tag(nazwa = nowa_nazwa)

    db.add(nowy_tag)
    db.commit()

def powiaz_zadanie_z_tagiem(db: Session, id_zadania: int, id_tagu: int):
    nowe_powiazanie = ZadaniaTag(zadanie_id = id_zadania, tag_id = id_tagu)
    db.add(nowe_powiazanie)
    db.commit()
def main():
    db_generator = get_db()
    db = next(db_generator)

    while True:
        print("===============")
        print("Menu:")
        print("1 - Pokaż zadania")
        print("2 - Dodaj nowe zadanie")
        print("3 - Zaktualizuj zadanie")
        print("4 - filtruj zadania")
        print("5 - Usun zadanie")
        print("6 - Dodaj Tag")
        print("7 - Dodaj tag do zadania")
        print("8 - Edytuj zadanie")
        print("9 - Pokaz tagi")
        print("10 - Wyjście z programu")

        print("===============")

        choice = input("Wybierz opcję: ")
        
        if choice == '1':
            pokaz_zadania(db)
        elif choice == '2':
            opis = input("Podaj opis zadania: ")
            dodaj_zadanie(db, opis)
        elif choice == '3':
            id = int(input("Podaj numer zadania: "))
            oznacz_jako_zrobione(db, id)
        elif choice == '4':
            fraza = input("Podaj szukana fraze: ")
            filtruj_zadania_po_opisie(db, fraza)
        elif choice == '5':
            id = int(input("Podaj id zadania które chcesz usunac"))
            usun_zadanie(db, id)
        elif choice == '6':
            nowy_tag = input("Podaj nowy tag")
            dodaj_tag(db, nowy_tag)
        elif choice == '7':
            id_zadania = int(input("Podaj id zadania: "))
            id_tagu = int(input("Podaj id tagu: "))
            powiaz_zadanie_z_tagiem(db, id_zadania, id_tagu)
        elif choice == '8':
            id_zadania = int(input("Podaj id zadania do edycji: "))
            nowy_opis = input("Podaj nowy opis zadania: ")
            edytuj_zadanie(db, id_zadania, nowy_opis)
        elif choice == '9':
            pokaz_tagi(db)
        elif choice == '10':
            print("Koniec działania programu! ")
            break

if __name__ == "__main__":
    main()
