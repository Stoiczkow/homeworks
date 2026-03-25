# Walidator nagłówków: Napisz funkcję validate_request(request_dict: dict) ,
# która sprawdza, czy w słowniku reprezentującym żądanie HTTP znajdują się kluczowe
# nagłówki: Host i User-Agent .
# Jeśli któregoś z nagłówków brakuje w kluczu headers , funkcja powinna podnieść
# wyjątek ValueError z odpowiednim komunikatem (np. "Brak wymaganego nagłówka:
# Host").
# Użyj bloku try...except , aby przetestować działanie funkcji z poprawnym i
# niepoprawnym słownikiem żądania. To ćwiczenie łączy wiedzę o sieciach z obsługą
# wyjątków.

def validate_request(request_dict: dict):
    headers = request_dict.get("headers", {})
    
    if "Host" not in headers:
        raise ValueError("Brak wymaganego nagłówka: Host")
    
    if "User-Agent" not in headers:
        raise ValueError("Brak wymaganego nagłówka: User-Agent")
    
    return True

# Testowanie funkcji validate_request
valid_request = {"headers": {"Host": "example.com", "User-Agent": "Python"}}
invalid_request = {"headers": {"Host": "example.com"}}

try:
    validate_request(valid_request)
    print("Poprawne żądanie")
except ValueError as e:
    print(f"Błąd: {e}")

try:
    validate_request(invalid_request)
    print("Poprawne żądanie")
except ValueError as e:
    print(f"Błąd: {e}")

    

