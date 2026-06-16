"""
Zdefiniuj model Product z polami: name, price, quantity.
Utwórz endpoint POST /products który przyjmuje Product i zwraca go z total_price.
(proste)
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Zadanie 4 - Pydantic Model")


class Product(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)


class ProductWithTotal(Product):
    total_price: float


@app.post("/products", response_model=ProductWithTotal)
async def create_product(product: Product):
    total = product.price * product.quantity
    return ProductWithTotal(**product.model_dump(), total_price=total)
