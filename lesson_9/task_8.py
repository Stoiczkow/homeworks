"""
Wyszukiwarka logów:
Program pyta użytkownika o słowo (np. "ERROR") i zapisuje wszystkie linie
zawierające to słowo do pliku wyniki_wyszukiwania.txt.
"""

szukane = input("Podaj słowo do wyszukania: ")

with open("log.txt", "r", encoding="utf-8") as f, \
     open("wyniki_wyszukiwania.txt", "w", encoding="utf-8") as out:

    for linia in f:
        if szukane in linia:
            out.write(linia)
