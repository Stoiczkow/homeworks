import sqlite3

#1
conn = sqlite3.connect("sklep.db")

cursor = conn.cursor()
query = """
SELECT 
COUNT(nazwa_produktu)
FROM Produkty
"""
cursor.execute(query)
wynik = cursor.fetchone()
print(wynik)

conn.commit()
conn.close()

#2

import sqlite3

conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

cursor.execute("SELECT nazwa_produktu, cena FROM Produkty")
produkty = cursor.fetchall()
conn.close()

if produkty:
    najdrozszy = max(produkty, key=lambda p: p[1])
    
    nazwa, cena = najdrozszy
    print(f"Najdroższy produkt to: {nazwa}")
    print(f"Cena: {cena} zł")
else:
    print("Baza produktów jest pusta.")

#4

import sqlite3

conn = sqlite3.connect("sklep.db")

cursor = conn.cursor()


cursor.execute("""
    SELECT AVG(cena) FROM Produkty as p
    JOIN Kategorie as k
    ON p.id_kategorii = k.id_kategorii
    WHERE k.nazwa_kategorii = "Książki"
""")

download = cursor.fetchone()
print(download[0])



conn.commit()

conn.close()

#5

import sqlite3

conn = sqlite3.connect("sklep.db")

cursor = conn.cursor()

cursor.execute("""
SELECT imie, email FROM Klienci
""")

download = cursor.fetchall()
for x in download:
    print(f"{x[0]:<20}{x[1]}")


conn.commit()
conn.close()

#6

import sqlite3

conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

query = """
SELECT nazwa_produktu, cena FROM Produkty as p
WHERE p.cena > (SELECT AVG(cena) FROM produkty)
"""

cursor.execute(query)
result = cursor.fetchall()

for index, x in enumerate(result):
    print(f"{x[0]:<15} {x[1]}")



conn.commit()
conn.close()

#7

import sqlite3

conn = sqlite3.connect("sklep.db")

cursor = conn.cursor()

query = """
SELECT nazwa_produktu 
FROM Produkty as p
JOIN Zamowienia_Produkty as zp ON zp.id_produktu = p.id_produktu
JOIN Zamowienia as z ON z.id_zamowienia = zp.id_zamowienia
JOIN Klienci as k ON k.id_klienta = z.id_klienta
WHERE k.imie = "Anna Nowak" 

"""

cursor.execute(query)
result = cursor.fetchall()

print(result)



conn.commit()
conn.close()

#8

query_kategorie = """
SELECT k.nazwa_kategorii, COUNT(p.id_produktu)
FROM Kategorie k
JOIN Produkty p ON k.id_kategorii = p.id_kategorii
GROUP BY k.nazwa_kategorii
"""

cursor.execute(query_kategorie)
for nazwa, ilosc in cursor.fetchall():
    print(f"Kategoria: {nazwa} | Liczba produktów: {ilosc}")

#9

import sqlite3


def znajdz_produkty_w_kategorii(nazwa_kategorii):

    conn = sqlite3.connect("sklep.db")

    cursor = conn.cursor()

    cursor.execute("""
            SELECT nazwa_produktu, cena 
                FROM Produkty as p
                JOIN Kategorie as k ON k.id_kategorii = p.id_kategorii
                WHERE k.nazwa_kategorii = ?
        """, (nazwa_kategorii,))  

    result = cursor.fetchall()

    conn.commit()
    conn.close()

    return result


result = znajdz_produkty_w_kategorii("Elektronika")
print(result)


