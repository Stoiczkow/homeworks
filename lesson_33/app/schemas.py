# === file: schemas.py ===

import re

from pydantic import BaseModel, ConfigDict, EmailStr, Field, computed_field, field_validator
from datetime import datetime
from typing import List, Literal, Optional

# Pydantic schemas - dla API (walidacja i serialization)


# Schema bazowa (wspólne pola)

# 4. Zdefiniuj model Product z polami: name, price, quantity.
# Utwórz endpoint POST /products który przyjmuje Product i zwraca go z total_price

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, le=10000)
    quantity: int
    category: str
    
    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    
    @field_validator('name')
    def name_must_be_alphanumeric(cls, name):
        if not re.match(r'^[a-zA-Z0-9\s]+$', name):
            raise ValueError('Name must contains only letters, numbers and spaces')
        return name.strip().title()
    
    @field_validator('category')
    def category_must_be_valid(cls, category):
        valid_categories = [
            'Electronics', 
            'Clothing', 
            'Books'
            ]
        
        if category not in valid_categories:
            raise ValueError(f'Category must be one of: {valid_categories}')
        return category
    
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=18, le=120)


# Schema dla tworzenia użytkownika (bez ID i created_at)
class UserCreate(UserBase):
    pass


# Schema dla aktualizacji (wszystkie pola opcjonalne)
class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=18, le=120)
    is_active: Optional[bool] = None


# Schema dla odpowiedzi (z ID i created_at)
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    # Konfiguracja dla kompatybilności z ORM
    class Config:
        from_attributes = True  # Pozwala tworzyć z ORM objects


# Schema zamówienia
class OrderBase(BaseModel):
    product_name: str
    quantity: int = Field(..., ge=1)
    price: float = Field(..., gt=0)


class OrderCreate(OrderBase):
    user_id: int


class OrderResponse(OrderBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Schema użytkownika z zamówieniami (zagnieżdżone)
class UserWithOrders(UserResponse):
    orders: List[OrderResponse] = []


class User(BaseModel):
    email: EmailStr

class AuthorCreate(BaseModel):
    name: str
    email: EmailStr

class AuthorResponse(BaseModel):    
    id: int
    name: str
    email: EmailStr
    
    model_config = ConfigDict(from_attributes=True)
    
class BookBase(BaseModel):
    title: str
    price: float
    category: str
    year: int
    author_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    year: Optional[int] = None
    author_id: Optional[int] = None


class BookResponse(BookBase):
    id: int
    title: str
    year: int
    author: AuthorResponse

    model_config = ConfigDict(from_attributes=True)

class BookFilter(BaseModel):
    category: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    sort_by: Optional[Literal["price", "title"]] = None
    
class PaginationParams(BaseModel):
    skip: int = Field(0, ge=0)
    limit: int = Field(10, ge=1)
        
class BooksResponse(BaseModel):
    pagination: PaginationParams
    books: List[BookResponse]