'''
Analiza stringa: Utwórz zmienną z łańcuchem znaków " Python jest super! " .
Wykonaj następujące działania i wyświetl wynik każdego kroku:
- Usuń zbędne białe znaki na początku i na końcu.
- Przekształć cały ciąg na małe litery.
- Zamień słowo "super" na "świetny".
- Wyświetl na ekranie znak pod indeksem 4 
'''

tekst = " Python jest super! "

# 1. Usunięcie białych znaków
krok1 = tekst.strip()

# 2. Zamiana na małe litery
krok2 = krok1.lower()

# 3. Zamiana słowa "super" na "świetny"
krok3 = krok2.replace("super", "świetny")

# 4. Znak pod indeksem 4
znak4 = krok3[4]

print("Po strip():", krok1)
print("Po lower():", krok2)
print("Po replace():", krok3)
print("Znak o indeksie 4:", znak4)
