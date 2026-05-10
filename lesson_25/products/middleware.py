class CustomLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Otrzemano zapytanie metodą: {request.method}")


        response = self.get_response(request)
        # print(f"Response status code: {response.status_code}")

        return response
    
    