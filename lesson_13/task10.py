# Zadanie 10 – Funkcja wyszukująca z JOIN
# Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko
# studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i
# wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.

import sqlite3

def znajdz_sale_studenta(nazwisko):
    connection = sqlite3.connect('uczelnia.db')
    cur = connection.cursor()

    cur.execute('''
                SELECT prz.id_audytorium FROM studenci AS st JOIN przypisania AS prz ON st.id_studenta = prz.id_studenta WHERE st.nazwisko = ?
                ''', (nazwisko,))

    audytorium_found = cur.fetchone()

    if not audytorium_found:
        print("Nie znaleziono sali dla tego studenta bądź student nie istnieje")
    else:
        cur.execute('''
                    SELECT nazwa_budynku, numer_sali FROM audytorium WHERE id_audytorium = ?
                    ''', audytorium_found,)
        
        room = cur.fetchone()
        print(f"Student ma zajęcia w budynku {room[0]} w sali {room[1]}")

cmd = input("Podaj nazwisko studenta aby znaleźć jego salę: ")
znajdz_sale_studenta(cmd)