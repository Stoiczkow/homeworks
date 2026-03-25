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
    headers: dict = request_dict.get('headers')
    if not headers.get('Host'):
        raise ValueError("Brak wymaganego nagłówka: Host")
    
    if not headers.get('User-Agent'):
        raise ValueError("Brak wymaganego nagłówka: User-Agent")

# Przykład użycia

good_request = {
    "start_line": {
        "method": "GET",
        "target": "/api/articles",
        "version": "HTTP/1.1"
        },
    "headers": {
        "Host": "my-blog.com",
        "User-Agent": "python-requests",
        "Accept": "application/json"
        },
    "body": None
    }

bad_request = {
    "start_line": {
        "method": "GET",
        "target": "/api/articles",
        "version": "HTTP/1.1"
        },
    "headers": {
        "Accept": "application/json"
        },
    "body": None
    }

try:
    validate_request(good_request)
except ValueError as e:
    print(f"Nieprawidłowy nagłówek. {e}")
else:
    print("Nagłówek prawidłowy")


try:
    validate_request(bad_request)
except ValueError as e:
    print(f"Nieprawidłowy nagłówek. {e}")
else:
    print("Nagłówek prawidłowy")