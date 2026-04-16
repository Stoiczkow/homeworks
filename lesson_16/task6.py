# Zadanie 6. Klasa Request : Napisz klasę w Pythonie o nazwie HttpRequest.

class HttpRequest:
    def __init__(self, method, target, headers=None, body=None):
        self.method = method
        self.target = target
        if headers is None:
            self.headers = {}
        else:
            self.headers = headers
        self.body = body
    
    def display(self):
        print("--- HTTP Request ---")
        print(f"Method: {self.method}")
        print(f"Target: {self.target}")
        print("Headers:")
        for key, value in self.headers.items():
            print(f" {key}: {value}")
        print("Body:")
        if self.body is None:
            print(" (empty)")
        else:
            print(f" {self.body}")
        print("--------------------")


request = HttpRequest(
    "POST",
    "/index.html",
    {"Host": "example.com", "User-Agent": "PythonClient/1.0"},
    '{"title": "Nowy wpis", "content": "Treść"}'
)

request.display()