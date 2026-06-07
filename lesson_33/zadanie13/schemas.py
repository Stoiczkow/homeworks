from pydantic import BaseModel, Field
from typing import Optional, List


class Book(BaseModel):
    id: int
    name: str
    author_id: int
    year: int
    price: float
    category: str

class BookResponse(BaseModel):
    id: int
    name: str
    author: AuthorResponse
    year: int
    price: float
    category: str

    class Config:
        from_attributes = True

class BookCreate(BaseModel):
    name: str
    author_id: int
    year: int
    price: float
    category: str

class BookUpdate(BaseModel):
    name: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    price: Optional[float] = None
    category: Optional[str] = None

class BookNoAuthorResponse(BaseModel):
    id: int
    name: str
    year: int
    price: float
    category: str

    class Config:
        from_attributes = True

class AuthorCreate(BaseModel):
    name: str

class AuthorResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True