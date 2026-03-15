# Funkcja wyszukująca z JOIN
# Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.


import sqlite3
path = 'homeworks/lesson_13/'

def znajdz_sale_studenta(last_name: str):

    conn = sqlite3.connect(path + 'uczelnia.db')
    c = conn.cursor()

    c.execute(
        '''
            select a.numer_sali, a.nazwa_budynku from studenci s join przypisania p on p.id_studenta = s.id_studenta join audytoria a on a.id_audytorium = p.id_audytorium  where s.nazwisko = ?;
        ''',
        (last_name,)
    )

    audytoria = c.fetchall()
    for  sala, budynek in audytoria:
        print(f"student {last_name} ma zajęcia w budynku {budynek}, sala {sala}")
    
    if not audytoria:
        print(f"Nie znaleziono sali dla studenta {last_name}")

    conn.close()

znajdz_sale_studenta('I')
znajdz_sale_studenta('II')
znajdz_sale_studenta('III')

