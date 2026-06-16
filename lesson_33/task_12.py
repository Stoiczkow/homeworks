"""
Dla modelu Product dodaj validators:
· name: tylko litery i cyfry
· price: musi być > 0 i <= 10000
· category: tylko z listy ["Electronics", "Books", "Clothing"]
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from typing import List
import re

app = FastAPI(title="Zadanie 12 - Custom Validators")


class Product(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0, le=10000)
    category: str
    tags: List[str] = []

    @field_validator("name")
    def name_alphanumeric(cls, v: str):
        if not re.match(r"^[a-zA-Z0-9\s]+$", v):
            raise ValueError("Name must contain only letters, numbers and spaces")
        return v.strip()

    @field_validator("category")
    def category_allowed(cls, v: str):
        allowed = ["Electronics", "Books", "Clothing"]
        if v not in allowed:
            raise ValueError(f"Category must be one of: {allowed}")
        return v


@app.post("/products")
async def create_product(product: Product):
    return product
