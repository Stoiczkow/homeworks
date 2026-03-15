#  Zadanie 4 – Bezpieczne dzielenie
# Napisz funkcję bezpieczne_dzielenie(a, b), która zwraca wynik dzielenia a / b. Użyj bloku try...except, aby obsłużyć błąd ZeroDivisionError. Jeśli wystąpi ten błąd, funkcja powinna zwrócić None i wyświetlić komunikat "Błąd: Dzielenie przez zero!"

# bok try ..except


# funkcja       # bok try ..except wewnąrz funkcji

def bezpieczne_dzielenie(a, b):
    try:
        return a / b

    except ZeroDivisionError:
       # komunikat
        print("Nie można dzielić przez 0 ")
        # zwrócenie none
        return None

# argumenty funkcji
result = bezpieczne_dzielenie(10,2)
print(result)
result_2 = bezpieczne_dzielenie(30,0)
print(result_2)

# w funkcji przechwci dzielenie przez 0
