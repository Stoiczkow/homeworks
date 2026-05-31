# # task3

# http_get_request = {
#     "start_line": {
#         "method": "GET",
#         "target": "/api/articles",
#         "version": "HTTP/1.1"
#     },
#     "headers": {
#         "Host": "my-blog.com",
#         "Accept": "application/json"
#     },
# }

# #task6

# class HttpRequest:
#     def __init__(self, method: str, target: str, headers={}, body=""):
#         self.method = method
#         self.target = target
#         self.headers = headers
#         self.body = body
        
#     def display(self):
#         return f"""
#                 --- HTTP Request ---
#                 Method: {self.method}
#                 Target: {self.target}
#                 Headers:
#                     {self.headers}
#                 Body:
#                     {self.body}
#                 """
    

# get_request = HttpRequest('GET', 
#                           'api.google.com', 
#                           {"Accept": "application/json",
#                            "User-Agent": "python-script1.0"})


# print(get_request.display())

# # Zadanie 7

# def parse_url(url: str) -> dict:

#     dict_to_return = {}

#     url_split1 = url.split(sep="://", maxsplit=1)
#     dict_to_return.update({'protocol': url_split1[0]})

#     url_split2 = url_split1[1].split(sep="/", maxsplit=1)   
#     dict_to_return.update({'path': url_split2[1]})

#     domain_and_port_split = url_split2[0].split(sep=":", maxsplit=1)
#     if len(domain_and_port_split) == 1:
#         dict_to_return.update({'domain': domain_and_port_split[0]})
#     else:
#         dict_to_return.update({'domain': domain_and_port_split[0]})
#         dict_to_return.update({'port': domain_and_port_split[1]})

#     return dict_to_return

# url = "https://api.example.com:8080/users/search?active=true"
# url2 = "https://api.example.com/users/search?active=true"

# print(parse_url(url2))

# -----------------------------------------------------------------------------
# tasks 8


# class FakeServer:

#     def __init__(self):
#         self.db = {
#             "users": [{"id": 1, "name": "Jan"}, {"id": 2,"name": "Anna"}]} 


#     def handle_request(self, request: dict):

#         method = request.get("method")
#         target = request.get("target")
#         body = request.get("body")

#         if method == "GET" and target == "/users":
#             return {
#                 "status" : 200,
#                 "return_text" : "OK",
#                 "body" : self.db["users"]
#             }

#         elif method == "POST" and target == "/users":
            
#             new_id = len(self.db["users"]) + 1
#             new_user = {"id" : new_id, "name" : body.get("name", "empty")}
            
#             self.db["users"].append(new_user)

#             return{
#                 "status" : 201,
#                 "return_text" : "Created",
#                 "body" : new_user
#             }

#         else:
#             return {"status" : 404,
#                      "return_text" : "Not Found",
#                      "body" : "nie utworzono"
#                     }

# class FakeClient:
#     def send(self, server ,request):

#         result =    server.handle_request(request)

#         print(f"kod statusu to: {result["status"]}")
#         print(f"status textowo: {result["return_text"]}")
#         print(f"uzytkownik {result["body"]}")


# server = FakeServer()
# client = FakeClient()

# test_1 = {
#     "method": "GET",
#     "target": "/users"
# }
# client.send(server, test_1)


# test_2 = {
#     "method": "POST",
#     "target": "/users",
#     "body": {"name": "Lukasz"}
# }
# client.send(server, test_2)

# test_3 = {
#     "method": "GET",
#     "target": "/photos"
# }
# client.send(server, test_3)


# #task 9

# # metoda PUT 

# {
# "name": "Kasia", 
# "email":"k.nowak@example.com", 
# "city": "Warszawa"
# }
# metoda Patch
# {"name": "Kasia"}

# Odpowiedz:
# - bardziej oszczedna jest oczywiscie metoda Patch poniewaz podmienia tylko wskazane zasoby/zasob
# dzieki czemu nie trzeba nadpisywac pozostalych, natomiast metoda Put wymaga od nas ponownego nadpisania wszystkich zasobow

#task 10

http_get_request = {
    "start_line": {
        "method": "GET",
        "target": "/api/products/42",
        "version": "HTTP/1.1"
    },
    "headers": {
        "Host": "example-store.com",
        "User-Agent": "MyCoolBrowser/1.0",
        "Accept": "application/json"
    },
    "body": None
}


def validate_request(request_dict: dict):

    if "headers" not in request_dict:
        raise ValueError("Brak headers!!")

    value = http_get_request["headers"]

    if 'Host' not in value:
        raise ValueError("Brak wymaganego nagłówka: Host")

    if 'User-Agent' not in value:
        raise ValueError("Brak wymaganego nagłówka: User-Agent")

    print("Walidacja zakonczyla sie sukcesem!!!" )

try:
    validate_request(http_get_request)
except ValueError as e:
    print(e)










