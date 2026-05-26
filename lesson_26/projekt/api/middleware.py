# Zadanie 7 – własny middleware logujący metodę HTTP każdego żądania

class LogMethodMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Otrzymano zapytanie metodą {request.method}")
        response = self.get_response(request)
        return response
