from fastapi import FastAPI, status
from pydantic import BaseModel, field_validator
import re

app = FastAPI(
    title="Product API",
    description="Walidacja modelu Product",
    version="1.0.0"
)


ALLOWED_CATEGORIES = [
    "Electronics",
    "Books",
    "Clothing"
]


class Product(BaseModel):
    name: str
    price: float
    category: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
   

        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError(
            )

        return value

    @field_validator("price")
    @classmethod
    def validate_price(cls, value):


        if value <= 0 or value > 10000:
            raise ValueError(

            )

        return value

    @field_validator("category")
    @classmethod
    def validate_category(cls, value):


        if value not in ALLOWED_CATEGORIES:
            raise ValueError(
                f"Category must be one of: {ALLOWED_CATEGORIES}"
            )

        return value


@app.post(
    "/products",
    status_code=status.HTTP_201_CREATED,
    tags=["Products"]
)
async def create_product(product: Product):


    return {
        "message": "Product created",
        "data": product
    }