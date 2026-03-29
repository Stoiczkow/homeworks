def validate_request(request_dict: dict) -> bool:
    required_headers = ["Host", "User-Agent"]
    headers = request_dict.get("headers", {})

    for header in required_headers:
        if header not in headers:
            raise ValueError(f"Brak wymaganego naglowka: {header}")

    return True


requests = [
    {
        "label": "Poprawne zadanie (wszystkie naglowki)",
        "request": {
            "method": "GET",
            "target": "/index.html",
            "headers": {
                "Host": "example.com",
                "User-Agent": "PythonClient/1.0",
                "Accept": "text/html"
            }
        }
    },
    {
        "label": "Brak naglowka User-Agent",
        "request": {
            "method": "GET",
            "target": "/index.html",
            "headers": {
                "Host": "example.com"
            }
        }
    },
    {
        "label": "Brak naglowka Host",
        "request": {
            "method": "POST",
            "target": "/api/data",
            "headers": {
                "User-Agent": "PythonClient/1.0"
            }
        }
    },
]

for test in requests:
    print(f"Test: {test['label']}")
    try:
        validate_request(test["request"])
        print("Wynik: OK - zadanie jest poprawne")
    except ValueError as e:
        print(f"Wynik: BLAD - {e}")
    print()