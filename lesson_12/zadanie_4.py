def bezpieczne_dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Blad: Dzielenie przez zero!")
        return None


print(bezpieczne_dzielenie(10, 2))
print(bezpieczne_dzielenie(10, 0))
