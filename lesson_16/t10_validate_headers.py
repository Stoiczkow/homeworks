"""
10.

Walidator nagłówków: Napisz funkcję validate_request(request_dict: dict) ,
która sprawdza, czy w słowniku reprezentującym żądanie HTTP znajdują się kluczowe
nagłówki: Host i User-Agent .
Jeśli któregoś z nagłówków brakuje w kluczu headers , funkcja powinna podnieść
wyjątek ValueError z odpowiednim komunikatem (np. "Brak wymaganego nagłówka:
Host").
Użyj bloku try...except , aby przetestować działanie funkcji z poprawnym i
niepoprawnym słownikiem żądania. To ćwiczenie łączy wiedzę o sieciach z obsługą
wyjątków.
"""


def validate_request(request_dict: dict):
    headers = request_dict.get("headers")
    if not isinstance(headers, dict):
        raise ValueError("Brak klucza headers lub niepoprawny format danych.")

    required_headers = ["Host", "User-Agent"]
    for header in required_headers:
        if header not in headers:
            raise ValueError(f"Brak wymaganego naglowka: {header}")

    return True


if __name__ == "__main__":
    good_request = {
        "method": "GET",
        "target": "/api/articles",
        "headers": {
            "Host": "my-blog.com",
            "User-Agent": "PythonClient/1.0",
        },
    }

    bad_request = {
        "method": "GET",
        "target": "/api/articles",
        "headers": {
            "Host": "my-blog.com",
        },
    }

    try:
        validate_request(good_request)
        print("Poprawne zadanie: walidacja OK")
    except ValueError as error:
        print(f"Blad walidacji (poprawne): {error}")

    try:
        validate_request(bad_request)
        print("Nie powinno sie wydrukowac dla niepoprawnego zadania")
    except ValueError as error:
        print(f"Blad walidacji (niepoprawne): {error}")
