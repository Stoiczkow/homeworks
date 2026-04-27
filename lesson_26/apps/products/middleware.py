"""
Stwórz prosty, własny middleware, który dla każdego przychodzącego zapytania będzie
dodawał do konsoli (użyj print()) informację o metodzie HTTP, z jakiej skorzystano (np.
"Otrzymano zapytanie metodą GET"). Pamiętaj, aby dodać swoje middleware do listy
MIDDLEWARE w settings.py
"""


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Otrzymano zapytanie metodą {request.method}")

        return self.get_response(request)
    