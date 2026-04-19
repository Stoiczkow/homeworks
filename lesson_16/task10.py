#  Walidator nagłówków: Napisz funkcję validate_request(request_dict: dict) ,
# która sprawdza, czy w słowniku reprezentującym żądanie HTTP znajdują się kluczowe
# nagłówki: Host i User-Agent .
# Jeśli któregoś z nagłówków brakuje w kluczu headers , funkcja powinna podnieść
# wyjątek ValueError z odpowiednim komunikatem (np. "Brak wymaganego nagłówka:
# Host")
# Użyj bloku try...except , aby przetestować działanie funkcji z poprawnym i
# niepoprawnym słownikiem żądania. To ćwiczenie łączy wiedzę o sieciach z obsługą
# wyjątków.

def validate_request(request_dict: dict):
    # check headers
    
    
    headers = request_dict["headers"] # wejscie do środka słownika i wyciągniecie headers

    # Check host
    if "Host" not in headers:
        raise ValueError("Brak wymaganego nagłówka: Host")
    # check user agnet
    if "User-Agent" not in headers:
        raise ValueError("Brak wymaganego nagłówka: User-Agent")
    
    return True
 
 
 # Żądania

# Poprawne żądanie
try:
    print(validate_request({
        "headers": {
            "Host": "Google.com",
            "User-Agent": "Chrome"
        }
    }))
    print("poprawne żądanie")
except ValueError as e:
    print("Błąd:", e)

# Niepoprawne żądanie
try:
    print(validate_request({
        "headers": {
            "Host": "Google.com"
        }
    }))
    print("niepoprawne żądanie")
except ValueError as e:
    print("Błąd:", e)

