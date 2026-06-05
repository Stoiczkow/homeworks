'''
    Zadanie 6. - Klasa Request : Napisz klasę w Pythonie o nazwie HttpRequest .

    Konstruktor __init__ powinien przyjmować method , target oraz opcjonalnie
        headers (słownik) i body (string).

    Dodaj metodę display() , która będzie drukować sformatowane żądanie na konsoli w
        czytelnej formie, np.:
        --- HTTP Request ---
        Method: GET
        Target: /index.html
        Headers:
        Host: example.com
        User-Agent: PythonClient/1.0
        Body:
        (empty)

    Przetestuj klasę, tworząc obiekt dla żądania POST z przykładowymi danymi.
'''

class HttpRequest:
    def __init__(self, method, target, headers=None, body=None):
        self.method = method
        self.target = target
        self.headers = headers if headers is not None else {}
        self.body = body if body is not None else ""

    def display(self):
        print("--- HTTP Request ---")
        print(f"Method: {self.method}")
        print(f"Target: {self.target}")
        print("Headers:")
        if self.headers:
            for key, value in self.headers.items():
                print(f"{key}: {value}")
        else:
            print("(none)")
        print("Body:")
        if self.body:
            print(self.body)
        else:
            print("(empty)")

request = HttpRequest(
    method="POST",
    target="/submit",
    headers={
        "Host": "example.com",
        "Content-Type": "application/json",
        "User-Agent": "PythonClient/1.0"
    },
    body='{"name": "Jan", "age": 30}'
)

request.display()

