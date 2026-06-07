from fastapi import FastAPI, HTTPException, Path, Query, Header, Depends
from datetime import datetime
import random
from pydantic import BaseModel, computed_field, EmailStr, field_validator
from typing import Dict, Optional


app = FastAPI(title="Zadanie 11")

CATEGORY_LIST: list = ["Electronics", "Books", "Clothing"]

class Book(BaseModel):
    title: str
    author: Author
    price: float

class Author(BaseModel):
    name: str
    email: EmailStr

class Product(BaseModel):
    name: str
    price: float
    category: str

    @field_validator("name")
    def only_letters_and_numbers(cls, name: str) -> str:
        if name.isalnum():
            return name
        else:
            raise ValueError("Nazwa musi być literami bądź liczbami")
        
    @field_validator("price")
    def at_least_zero_and_no_more_then_10000(cls, price: float) -> float:
        if price > 0 and price < 10000:
            return price
        else:
            raise ValueError("Liczba musi być większa od 0 oraz mniejsza niż 10000")

    @field_validator("category")
    def only_specific_category(cls, category: str) -> str:
        
        if category in CATEGORY_LIST:
            return category
        else:
            raise ValueError("Category not allowed")

BOOKS_DB: Dict[int, dict] = {
    1: {"name": "Zielona książka", "author": {"name": "Tomasz Kowal", "email": "tom@smith.com"}, "year": 1999},
    2: {"name": "Czarna książka", "author": {"name": "Krzysztof Piecuch", "email": "piecuch@krzysztof.com"}, "year": 2004}
}

@app.post("/books", status_code=201)
async def addbook(book: Book):
    id = len(BOOKS_DB) + 1
    BOOKS_DB[id] = book.model_dump()
    print(BOOKS_DB)
    return None

@app.post("/products", status_code=201)
async def addproduct(product: Product):
    return None