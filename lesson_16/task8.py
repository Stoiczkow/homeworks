# Symulacja Klient-Serwer: Stwórz prostą symulację interakcji Klient-Serwer przy użyciu
# klas.
# Napisz klasę FakeServer , która w __init__ tworzy "bazę danych" w postaci
# słownika, np. self.db = {"users": [{"id": 1, "name": "Jan"}, {"id": 2,
# "name": "Anna"}]} .
# Klasa FakeServer powinna mieć metodę handle_request(request: dict) , która
# analizuje żądanie (reprezentowane przez słownik).
# Jeśli metoda to GET a cel to /users , powinna zwrócić słownik-odpowiedź z
# kodem 200 i listą użytkowników w ciele.
# Jeśli metoda to POST a cel to /users , powinna dodać nowego użytkownika z
# ciała żądania do self.db i zwrócić odpowiedź z kodem 201 (Created).
# Dla każdego innego żądania, zwróć odpowiedź z kodem 404 (Not Found).
# Napisz klasę FakeClient z metodą send(server, request) , która "wysyła" żądanie
# do obiektu serwera i drukuje otrzymaną odpowiedź.
# Przetestuj scenariusze: pobranie wszystkich użytkowników, dodanie nowego
# użytkownika i próbę dostępu do nieistniejącego zasobu.

class FakeServer:
    def __init__(self): # metoda
        # obiekt baza danych  # Start serwera
        self.db = {
            "users": 
            [{"id": 1, "name": "Jan"}, 
             {"id": 2,"name": "Anna"}
            ]
        }
    def handle_request(self, request: dict): # przyjecie żadań od klienta
        method = request["method"]  # wyciągniecie wartosci GET
        path = request["path"] # /users

# Dla GET/ users

        if method == "GET" and path == "/users":
            return {
                "status": 200,
                "data": self.db["users"]
            }
        
# For POST
        if method == "POST" and path =="/users":
            new_user = request["body"]

            # add user
            self.db["users"].append(new_user)

            return{
                "status": 201,
                "message": "add user"
            }
# Dla każdego innego żądania, zwróć odpowiedź z kodem 404 (Not Found)

        return {
            "status": 404,
            "message": "Not Found"

        }
    
# Napisz klasę FakeClient z metodą send(server, request) , która "wysyła" żądanie do obiektu serwera i drukuje otrzymaną odpowiedź

class FakeClient:
    def send(self, server, request):
        response = server.handle_request(request) # wywołaj metode serwera i zapisz odpowiedz
        print("Answear", response) 

####
server = FakeServer()
client = FakeClient()

#1. take user
client.send(server, {"method": "GET", "path": "/users"})

#2. add user
client.send(server, {
    "method": "POST","path": "/users", "body": {"id": 3, "name": "Krzysztof"}})

# 3 check wywołanie
client.send(server,{"method": "GET", "path": "/users"})

# 4 Wrong adres
client.send(server,{"method": "GET", "path": "/other"})

