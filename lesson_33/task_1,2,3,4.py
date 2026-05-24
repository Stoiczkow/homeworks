# 1. ✏ Zadanie 1 – Pierwsze API
# Stwórz aplikację FastAPI z trzema endpoints:
# (proste)

from fastapi import FastAPI, Path, HTTPException
from datetime import datetime
from random import randint
from pydantic import BaseModel, computed_field

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello"}

@app.get("/time")
async def time():
    return {"current_time": datetime.now()}

@app.get("/random")
async def random():
    return {"number": randint(1, 100)}


# 2. ✏ Zadanie 2 – Path Parameters
# Utwórz endpoint GET /greet/{name} który zwraca powitanie dla danej osoby.
# Dodaj walidację: imię musi mieć min 2 znaki.
# (proste)

@app.get("/greet/{name}")
async def greet(name: str = Path(..., min_lenght=2)):
    return {"message": f"Hello {name}"}

# 3. ✏ Zadanie 3 – Query Parameters
# Stwórz endpoint GET /calculate który przyjmuje query params:
# a: int (wymagany)
# b: int (wymagany)
# operation: str (domyślnie "add")
# Zwraca wynik operacji: add, subtract, multiply, divide.
# (proste)

@app.get("/calculate")
async def calculate(a: int, b: int, operation: str = "add"):
    result = None
    if operation == "add":
        result = a + b
    if operation == "substract":
        result = a - b
    if operation == "multiply":
        result = a * b
    elif operation == "divide":
        try:
            result = a / b
        except ZeroDivisionError:
            raise HTTPException(detail="Cannot divide by zero")
        
    return {"result": result}


# 4. ✏ Zadanie 4 – Pydantic Model
# Zdefiniuj model Product z polami: name, price, quantity.
# Utwórz endpoint POST /products który przyjmuje Product i zwraca go z total_price.
# (proste)

class ProductResponse(BaseModel):
    name: str
    price: float
    quantity: int

    @computed_field
    def total_price(self) -> float:
        return self.price * self.quantity

@app.post("/products", response_model=ProductResponse, status_code=201)
async def add_product(product: ProductResponse):
    return product