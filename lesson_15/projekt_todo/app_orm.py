from sqlalchemy.orm import Session

from database import get_db
from models import Zadania, Tag, ZadaniaTag

#Zadanie 3 – Wyświetlanie ID
# Zmodyfikuj funkcję pokaz_zadania w obu aplikacjach tak, aby oprócz opisu i statusu, wyświetlała również ID każdego zadania. (W wersji ORM już to zrobiliśmy, upewnij się, że wiesz dlaczego to działa).

# Zad 5 data utworzenia
 # W pliku sqlalchemy_app/models.py, do klasy Zadanie dodaj nową kolumnę: data_utworzenia = Column(DateTime, default=datetime.datetime.utcnow). Nie zapomnij o imporcie from sqlalchemy import DateTime i import datetime. Następnie wygeneruj i zastosuj nową migrację Alembic.
# Musimy jeszcze raz utworzyć skrypt migracyjny
# 2 plecenie w konsoli że to co mamy w pliku przeniósł do bazy danych

# e. Zmodyfikowania logiki aplikacji, aby można było dodać taga do zadania

def pokaz_zadania(db: Session):
    zadania = db.query(Zadania).all() # zwraca obiekty klasy Zadania
    
    print('--- Twoje zadania ---')
    
    for zadanie in zadania: # każdy zad ma pola jak normalny obiekt, id, opis,zrobio 
        print(f"ID {zadanie.id} - {zadanie.opis} - Zrobione {zadanie.zrobione}, data utworzenia {zadanie.data_utworzenia}, Tagi {zadanie.tags}")

# Zadanie 2 – Usuwanie zadań (SQLAlchemy)
# Zrób to samo dla aplikacji app_orm.py. Funkcja w warstwie danych powinna znaleźć obiekt zadania, a następnie użyć db.delete(obiekt_zadania) i db.commit().

def usun_zadanie(db: Session, id_zadania: int):
    zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).first()
    #zrobione to w 1 lini
    # zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).delete()
    if not zadanie:
        print("Nie znaleziono zadania")
        return

    db.delete(zadanie)
    db.commit()

def dodaj_zadanie(db: Session, nowy_opis: str):
    nowe_zadanie = Zadania(opis=nowy_opis)
    
    db.add(nowe_zadanie)
    db.commit()

# Zadanie 7 – Wyszukiwanie po opisie (SQLAlchemy)
# Zaimplementuj tę samą funkcjonalność w aplikacji ORM. Użyj metody .filter() oraz metody .contains() na kolumnie, np. db.query(Zadanie).filter(Zadanie.opis.contains(fraza)).all()

def filtruj_zadania_po_opisie(db: Session, fraza:str):
    zadania = db.query(Zadania).filter(Zadania.opis.contains(fraza)).all()

    if zadania: 
        print('--- Twoje zadania ---')
    
        for zadanie in zadania:
             # każdy zad ma pola jak normalny obiekt, id, opis,zrobio 
            print(f"ID {zadanie.id} - {zadanie.opis} - Zrobione {zadanie.zrobione}")
    else:
        print(f"Nie znaleziono zadan z fraza {fraza} w opisie")

#e. Zmodyfikowania logiki aplikacji, aby można było dodać taga do zadania

def dodaj_tag(db: Session, nowa_nazwa: str):
    nowy_tag = Tag(nazwa=nowa_nazwa)

    db.add(nowy_tag)
    db.commit()

#e. Zmodyfikowania logiki aplikacji, aby można było dodać taga do zadania
#Powiązanie tagu z zadaniem

def powiaz_zadanie_z_tagiem_(db: Session, id_zadania: int, id_tagu: int):
    nowe_powiazanie = ZadaniaTag(zadanie_id=id_zadania,
                                 tag_id = id_tagu)
    
    # Zapisanie nowego obiektu w bazie 

    db.add(nowe_powiazanie)
    db.commit()



def oznacz_jako_zrobione(db: Session, id_zadania: int):
    zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).first()
    # zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).update({"zrobione": True})
    # db.commit() update przy użyciu jednego zapytania
    if zadanie:
        zadanie.zrobione = True
        db.commit()
        print("Zadanie zostało zaktualizowane!")
    else:
        print(f"Nie znaleziono zadania o id {id_zadania}")

#Zadanie 10 – Interaktywna edycja (dowolna aplikacja)
# W wybranej przez siebie aplikacji (Raw SQL lub ORM) dodaj funkcję "Edytuj zadanie". Po jej wybraniu, użytkownik powinien podać ID zadania, a następnie wpisać nowy opis. Zaktualizuj odpowiedni wpis w bazie danych
def edytuj_zadanie(db: Session, id_zadania: int, nowy_opis: str):
    zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).first()

# sprawdzenie czy zadanie istnieje
    if not zadanie:
        print("Nie znaleziono zadania")
        return
# nowy opis do zadania
    zadanie.opis = nowy_opis
    db.commit() # zapis w bazie danych
    print("Zadanie zostało zaktualizowane!")


# Funkcja pokaz tagi:
def pokaz_tagi(db: Session):
    tags = db.query(Tag).all()

    print("===== Twoje tagi ======")

    for tag in tags:
        print(f"ID {tag.id} - {tag.nazwa} - {tag.zadania}")

def main():
    db = get_db()
    
    while True:
        print('==================')
        print('Menu: ')
        print('1 - Pokaż zadania')
        print('2 - Dodaj zadanie')
        print('3 - Zaktualizuj zadanie')
        print("4 - Usun zadanie")
        print("5 - Filtruj zadania")
        print("6 - Dodaj nowy Tag")
        print("7 - Dodaj tag do zadania")
        print("8 - Pokaz tagi")
        print("9 - Edytuj zadanie")
        print('10 - Wyjdź')
        
        choice = input('Wybierz opcję: ')
        
        if choice == '1':
            pokaz_zadania(db)
        elif choice == '2':
            nowy_opis = input('Podaj opis zadania: ')
            dodaj_zadanie(db, nowy_opis)
        elif choice == '3':
            try:
                id = int(input('Podaj numer zadania'))
                oznacz_jako_zrobione(db, id)
            except ValueError:
                print(f"Nieprawidłowy format ID. Musi być podany int")
        elif choice == "4":
            id = int(input("Podaj id zadania które chcesz usnąć "))
            usun_zadanie(db, id)
        elif choice == "5":
            fraza = input("Podaj szukaną frazę:")
            filtruj_zadania_po_opisie(db, fraza)
        elif choice == "6":
            nowy_tag = input("Podaj nazwę tagu: ")
            dodaj_tag(db, nowy_tag)
        elif choice == "7":
            id_zadania = int(input("Podaj id zadania: "))
            id_tagu = int(input("Podaj id tagu: "))
            powiaz_zadanie_z_tagiem_(db, id_zadania, id_tagu) # wywołanie funkcji
        elif choice == "8":
            pokaz_tagi(db)
        elif choice == "9":
            try:
                id_zadania = int(input("Podaj ID zadania do edycji: "))
                nowy_opis = input("Podaj nowy opis: ")
                edytuj_zadanie(db, id_zadania, nowy_opis)
            except ValueError:
                print("ID musi być liczbą!")
        elif choice == '10':
            print('Koniec działania programu')
            break


if __name__ == "__main__":
    main()