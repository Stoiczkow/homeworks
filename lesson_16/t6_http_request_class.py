"""
6. 
Klasa Request : Napisz klasę w Pythonie o nazwie HttpRequest .
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
--------------------
Przetestuj klasę, tworząc obiekt dla żądania POST z przykładowymi danymi.
"""


class HttpRequest:
    def __init__(self, method, target, headers=None, body=""):
        self.method = method
        self.target = target
        self.headers = headers or {}
        self.body = body

    def display(self):
        print("--- HTTP Request ---")
        print(f"Method: {self.method}")
        print(f"Target: {self.target}")
        print("Headers:")
        if self.headers:
            for key, value in self.headers.items():
                print(f"{key}: {value}")
        else:
            print("(empty)")
        print("Body:")
        print(self.body if self.body else "(empty)")
        print("--------------------")


if __name__ == "__main__":
    post_request = HttpRequest(
        method="POST",
        target="/api/articles",
        headers={
            "Host": "my-blog.com",
            "User-Agent": "PythonClient/1.0",
            "Content-Type": "application/json",
        },
        body='{"title":"HTTP basics","content":"Intro to requests"}',
    )
    post_request.display()
