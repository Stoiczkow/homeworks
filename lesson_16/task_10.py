# 10. Walidator nagłówków: Napisz funkcję validate_request(request_dict: dict) ,
# która sprawdza, czy w słowniku reprezentującym żądanie HTTP znajdują się kluczowe
# nagłówki: Host i User-Agent .
# Jeśli któregoś z nagłówków brakuje w kluczu headers , funkcja powinna podnieść
# wyjątek ValueError z odpowiednim komunikatem (np. "Brak wymaganego nagłówka:
# Host")
# Użyj bloku try...except , aby przetestować działanie funkcji z poprawnym i
# niepoprawnym słownikiem żądania. To ćwiczenie łączy wiedzę o sieciach z obsługą
# wyjątków

def validate_request(request_dict: dict):
    headers_to_check = ["Host", "User-Agent"]
    missing_headers = []
    
    for header in headers_to_check:
        if header not in request_dict.get("headers"):
            missing_headers.append(header)
            
    if missing_headers:
        raise ValueError(f"Brak wymaganego nagłówka: {missing_headers}")
    else:
        print("Prawidłowe żądanie")

invalid_req_1 = {
    "start_line": {
        "method": "GET",
        "target": "/api/articles"
    },
    "headers": {
        "Host": "my-blog.com",
        "Accept": "application/json"
    }
}

invalid_req_2 = {
    "start_line": {
        "method": "GET",
        "target": "/api/articles"
    },
    "headers": {
        "Accept": "application/json"
    }
}

valid_req = {
    "start_line": {
        "method": "GET",
        "target": "/api/articles"
    },
    "headers": {
        "Host": "my-blog.com",
        "User-Agent": "MyCoolBrowser/1.0",
        "Accept": "application/json"
    }
}

try:
    validate_request(valid_req)
except ValueError as e:
    print(e)
    
try:
    validate_request(invalid_req_1)
except ValueError as e:
    print(e)
    
try:
    validate_request(invalid_req_2)
except ValueError as e:
    print(e)