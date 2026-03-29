class HttpRequest:
    def __init__(self, method, target, headers=None, body=None):
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
                print(f"  {key}: {value}")
        else:
            print("  (none)")
        print(f"Body: {self.body if self.body else '(empty)'}")
        print("--------------------")


request = HttpRequest(
    method="POST",
    target="/api/login",
    headers={
        "Host": "example.com",
        "Content-Type": "application/json",
        "User-Agent": "PythonClient/1.0"
    },
    body='{"username": "jan", "password": "haslo123"}'
)

request.display()