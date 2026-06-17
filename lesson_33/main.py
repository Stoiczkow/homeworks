from fastapi import FastAPI, Path, HTTPException, status
from datetime import datetime
import random
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(
    title="Lesson 33 FastAPI",
    description="Ćwiczeniowe API z lekcji 33: endpointy, parametry, Pydantic i CRUD.",
    version="1.0.0",
)

class Product(BaseModel):
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=1)

class Book(BaseModel):
    id: int | None = None
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=2)
    year: int | None = None

books_db: dict[int, Book] = {}
book_id_counter = 1

class User(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr




@app.get("/books", tags=["Books"])
async def get_books():
    """
    Zwraca listę wszystkich książek zapisanych w pamięci aplikacji.
    """
    return list(books_db.values())

@app.post("/users")
async def create_user(user: User):
    return {
        "message": "User created",
        "user": user
    }

@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    global book_id_counter

    book.id = book_id_counter
    books_db[book_id_counter] = book
    book_id_counter += 1

    return book


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")

    return books_db[book_id]



@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")

    books_db.pop(book_id)

    return None

@app.post("/products")
async def create_product(product: Product):
    total_price = product.price * product.quantity

    return {
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "total_price": total_price,
    }

@app.get("/", tags=["Basic"])
async def root():
    """
    Zwraca prostą wiadomość powitalną.

    Example response:
    {"message": "Hello"}
    """
    return {"message": "Hello"}



@app.get("/time")
async def get_time():
    return {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


@app.get("/random")
async def get_random_number():
    return {"number": random.randint(1, 100)}

@app.get("/greet/{name}")
async def greet_user(name: str = Path(..., min_length=2)):
    return {"message": f"Hello, {name}!"}

@app.get("/calculate", tags=["Calculator"])
async def calculate(a: int, b: int, operation: str = "add"):
    """
    Wykonuje proste działania matematyczne.

    Dostępne operacje:
    - add
    - subtract
    - multiply
    - divide
    """
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Nie można dzielić przez zero")
        result = a / b
    else:
        raise HTTPException(
            status_code=400,
            detail="Nieznana operacja. Użyj: add, subtract, multiply albo divide"
        )

    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result
    }