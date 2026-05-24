from pydantic import BaseModel, EmailStr


class Author(BaseModel):
    name: str
    email: EmailStr


class Book(BaseModel):
    title: str
    author: Author
    price: float