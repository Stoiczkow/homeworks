class HttpRequest:
    def __init__(self, method: str, target: str, headers={}, body=""):
        self.method = method
        self.target = target
        self.headers = headers
        self.body = body
        
    def display(self):
        return f"""
                --- HTTP Request ---
                Method: {self.method}
                Target: {self.target}
                Headers:
                    {self.headers}
                Body:
                    {self.body}
                """
    

get_request = HttpRequest('GET', 
                          'api.google.com', 
                          {"Accept": "application/json",
                           "User-Agent": "python-script1.0"})


print(get_request.display())