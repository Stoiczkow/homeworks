# Walidator nagłówków: Napisz funkcję validate_request(request_dict: dict) ,
# która sprawdza, czy w słowniku reprezentującym żądanie HTTP znajdują się kluczowe
# nagłówki: Host i User-Agent .
# Jeśli któregoś z nagłówków brakuje w kluczu headers , funkcja powinna podnieść wyjątek ValueError z odpowiednim komunikatem (np. "Brak wymaganego nagłówka:
# Host").
# Użyj bloku try...except , aby przetestować działanie funkcji z poprawnym i
# niepoprawnym słownikiem żądania. To ćwiczenie łączy wiedzę o sieciach z obsługą wyjątków.

def validate_request(request_dict: dict):
    if "Host" not in request_dict["headers"]:
        raise ValueError("Brak wymaganego nagłówka: Host")
    if "User-Agent" not in request_dict["headers"]:
        raise ValueError("Brak wymaganego nagłówka: User-Agent")
    
good_request = {
    "headers": {
        "Host": "example.com",
        "User-Agent": "PythonClient/1.0"
    }
}

bad_request = {
    "headers": {
        "Host": "example.com"
    }
}
    
try:
    validate_request(good_request)
    print("Request poprawny")
except ValueError as e:
    print(e)

try:
    validate_request(bad_request)
    print("Request poprawny")
except ValueError as e:
    print(e)