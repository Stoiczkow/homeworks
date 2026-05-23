from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Nested Models API",
    description="desciprtion",
    version="1.0.0"
)


class Author(BaseModel):
    name: str
    email: EmailStr


class Book(BaseModel):
    title: str
    author: Author
    price: float


@app.post(
    "/books",
    status_code=status.HTTP_201_CREATED,
    tags=["Books"]
)
async def create_book(book: Book):

    return {
        "message": "Book created",
        "data": book
    }