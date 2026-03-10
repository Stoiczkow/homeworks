def bezpieczne_dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero")
        return None

result= bezpieczne_dzielenie(10,2)
print(f"{result}\n")
result2 = bezpieczne_dzielenie(10,0)
print(result2)