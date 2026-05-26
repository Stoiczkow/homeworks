def validate_request(request_dict: dict):
    headers = request_dict.get("headers", {})
    for wymagany in ("Host", "User-Agent"):
        if wymagany not in headers:
            raise ValueError(f"Brak wymaganego naglowka: {wymagany}")


poprawne_zadanie = {
    "method": "GET",
    "target": "/index.html",
    "headers": {
        "Host": "example.com",
        "User-Agent": "PythonClient/1.0"
    }
}

niepoprawne_zadanie = {
    "method": "GET",
    "target": "/index.html",
    "headers": {
        "Host": "example.com"
    }
}

try:
    validate_request(poprawne_zadanie)
    print("Zadanie poprawne.")
except ValueError as e:
    print(f"Blad: {e}")

try:
    validate_request(niepoprawne_zadanie)
    print("Zadanie poprawne.")
except ValueError as e:
    print(f"Blad: {e}")
