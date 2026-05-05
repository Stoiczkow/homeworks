class CustomLogMiddelware:
    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        print(f"otrzymano zapytanie metodą {request.method}")
        
        response =  self.get_response(request)

        return response