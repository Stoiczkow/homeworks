# Napisz funkcję bezpieczne_dzielenie(a, b), która zwraca wynik dzielenia a / b. Użyj bloku
# try...except, aby obsłużyć błąd ZeroDivisionError. Jeśli wystąpi ten błąd, funkcja powinna
# zwrócić None i wyświetlić komunikat "Błąd: Dzielenie przez zero!".
# 5. ✏ Zadanie 5 – Odczyt pliku

def bezpieczne_dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero!")
        return None

# Przykład wykorzystania

bezpieczne_dzielenie(10, 0)