#Zadanie 4 – Średnia cena książki

# Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().
import sqlite3

Connection = sqlite3.connect("sklep.db") # połączenie z bazą danych
cursor = Connection.cursor() # tworzenie obiektu kursora
# musimy przy join uzyc tej pragmy
cursor.execute("PRAGMA foreign_keys = ON")

# uzywamy AVG()

cursor.execute("""
          SELECT AVG(cena) FROM Produkty AS p
        JOIN Kategorie AS k
               ON k.id_kategorii = p.id_kategorii
            WHERE k.nazwa_kategorii = "Książki"
               
                     
                """)
# JOIN - kategorie

#Korzystamy teraz z produkty i kategori dokladnie z Ksiazki

result = cursor.fetchone() # wyświetla 1 wynik

print(result[0])
# sumuje przedmioty z id 1 bo elektronika  
# [0] Zwraca nam tuple z 1 elementem zeby podac 1 element

Connection.commit()# połączenie z bazą + wykonywanie SQL, zatwierdza zmiany w bazie danych po co commit dane są trwale zapisane w bazie
Connection.close()