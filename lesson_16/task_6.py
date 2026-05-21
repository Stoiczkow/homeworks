# 6. Klasa Request : Napisz klasę w Pythonie o nazwie HttpRequest .
# Konstruktor __init__ powinien przyjmować method , target oraz opcjonalnie
# headers (słownik) i body (string).
# Dodaj metodę display() , która będzie drukować sformatowane żądanie na konsoli w
# czytelnej formie, np.:
# --- HTTP Request ---
# Method: GET
# Target: /index.html
# Headers:
# Host: example.com
# User-Agent: PythonClient/1.0
# Body:
# (empty)
# --------------------

class HttpRequest:
        def __init__(self, method, target, headers={}, body=""):
            self.method = method
            self.target = target
            self.headers = headers
            self.body = body
            
        def display(self):
            print(f"""
                  --- HTTP Request ---
                  Method: {self.method}
                  Target: {self.target}
                  Headers: 
                    {self.headers}
                  Body:
                    {self.body}
                  """)
            
post_req = HttpRequest('POST',
                        'api.google.com',
                        {"Accept": "application/json",
                        "User-Agent": "python-script1.0"})
post_req.display()