from sqlalchemy.orm import Session

from database import get_db
from models import Zadania

def pokaz_zadania(db: Session):
    zadania = db.query(Zadania).all()
    
    print('--- Twoje zadania ---')

    for zadanie in zadania:
        print(f"ID {zadanie.id} - {zadanie.opis} - Zrobione {zadanie.zrobione}, data utworzenia {zadanie.data_utworzenia}")

def dodaj_zadanie(db: Session, nowy_opis: str):
    nowe_zadanie = Zadania(opis=nowy_opis)

    db.add(nowe_zadanie)
    db.commit()

def filtruj_zadania_po_opisie(db: Session, fraza: str):
    zadania = db.query(Zadania).filter(Zadania.opis.contains(fraza)).all()

    if zadania:
        print('--- Twoje zadania ---')

        for zadanie in zadania:
            print(f"ID {zadanie.id} - {zadanie.opis} - Zrobione {zadanie.zrobione}, data utworzenia {zadanie.data_utworzenia}")
    else:
        print(f"Nie znaleziono zadań z frazą {fraza} w opisie.")


def usun_zadanie(db: Session, id_zadania: int):
    zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).first()
    # zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).delete()
    if not zadanie:
        print("Nie znaleziono takiego zadania.")
        return
    
    db.delete(zadanie)
    db.commit()

def oznacz_jako_zrobione(db: Session, id_zadania: int):
    zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).first()
    # zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).update({"zrobione": True})
    # db.commit()
    if zadanie:
        zadanie.zrobione = True
        db.commit()
        print("Zadanie zostało zaktualizowane!")
    else:
        print(f"Nie znaleziono zadania o id {id_zadania}")

def edytuj_zadanie(db: Session, id_zadania: int, edytowany_opis: str):
    zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).first()
                                       
    if zadanie:
        zadanie.opis = edytowany_opis
        db.commit()
        print(f"Zaktualizowano opis zadania ID: {id_zadania}")
    else:
        print(f"Nie znaleziono zadania ID: {id_zadania} ")
        

def main():
    db = get_db()

    while True:
        print('=================')
        print('Menu:')
        print('1 - Pokaż zadania')
        print('2 - Dodaj zadanie')
        print('3 - Zaktualizuj zadanie')
        print('4 - Usuń zadanie')
        print('5 - Filtruj zadania')
        print('6 - Edytuj opis zadania')
        print('7 - Wyjdź')

        choice = input('Wybierz opcję: ')

        if choice == '1':
            pokaz_zadania(db)
        elif choice == '2':
            nowy_opis = input('Podaj opis zadania: ')
            dodaj_zadanie(db, nowy_opis)
        elif choice == '3':
            try:
                id = int(input('Podaj numer zadania: '))
                oznacz_jako_zrobione(db, id)
            except ValueError:
                print(f"Nieprawidłowy format ID. Musi być int")
        elif choice == '4':
            id = int(input('Podaj id zadania które chcesz usunąć: '))
            usun_zadanie(db, id)
        elif choice == '5':
            fraza = input('Podaj szukaną frazę: ')
            filtruj_zadania_po_opisie(db, fraza)
        elif choice == '6':
            try:
                id = int(input('Podaj numer zadania do edycji: '))
                edytowany_opis = input('Podaj nowy opis: ')
                edytuj_zadanie(db, id, edytowany_opis)
            except ValueError:
                print(f"Nieprawidłowy format ID. Musi być int")
        elif choice == '7':
            print('Koniec działania programu.')
            break


if __name__ == '__main__':
    main()