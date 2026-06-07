from fastapi import FastAPI, HTTPException, Path, Query, Header, Depends
from datetime import datetime
import random
from pydantic import BaseModel, computed_field, EmailStr
from typing import Dict, Optional


app = FastAPI(title="Zadania lekcja 33",
                summary='''Ta aplikacja zawiera różnorodne endpointy
                które są wykonane zgodnie z instrukcjami
                podanymi w lekcji 33''',
                version="1.0.0")

class Product(BaseModel):
    id: int
    name: str
    price: int
    quantity: int

    @computed_field
    def total_price(self) -> float:
        return self.price * self.quantity
    
class Book(BaseModel):
    id: int
    name: str
    author: str
    year: int

class BookResponse(BaseModel):
    name: str
    author: str
    year: int

class User(BaseModel):
    email: EmailStr


BOOKS_DB: Dict[int, dict] = {
    1: {"id": 1, "name": "Zielona książka", "author": "Tomasz Kowal", "year": 1999},
    2: {"id": 2, "name": "Czarna książka", "author": "Bożydar Waleczny", "year": 2004}
}

# Import routerów dla books

from routers import books
app.include_router(books.router)

# Funkcje depends

async def verify_token(x_token: str = Header(...)):
    if x_token != "secret-token-123":
        raise HTTPException(status_code=401, detail="Invalid token")
    return x_token

# endpointy główne

@app.get("/", tags=["Basic Functions"])
async def hello(token: str = Depends(verify_token)):
    return {"message": "hello"}

@app.get("/time", tags=["Basic Functions"])
async def returntime(token: str = Depends(verify_token)):
    return {"current time": f"{datetime.now()}"}

@app.get("/randomint", tags=["Basic Functions"])
async def randomint(token: str = Depends(verify_token)):
    return {"random int": f"{random.randint(1,100)}"}

@app.get("/greet/{name}", tags=["Basic Functions"])
async def greet_name(name: str = Path(..., min_length=2)):
    return {"message": f"Hello {name}"}

@app.get("/calculate", tags=["Basic Functions"])
async def calculate(a: int, b: int, operation: str = "add"):
    """Funkcjonalny kalkulator, który możesz wykorzystać do
    prostych obliczeń. Wystarczy podać w zapytaniu parametr a i b oraz operation
    
    Dostępne operation:

    -> add

    -> substract

    -> multiply

    -> divide

    przykład: /calculate?a=10&b=10&operation=multiply
    """
        
    result = None
    if operation == "add":
        result = a + b
    elif operation == "substract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        try:
            result = a / b
        except ZeroDivisionError:
            raise HTTPException(detail="Cannot divide by zero")

    return {"result": result}

@app.post("/product", response_model=Product, status_code=201, tags=["Objects"])
async def returnproduct(product: Product):
    return product




@app.post("/users", status_code=201, tags=["Objects"])
async def post_user(user: User):
    print(user.model_dump())
    return None