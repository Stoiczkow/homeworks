# === file: schemas.py ===
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional

# Pydantic schemas - dla API (walidacja i serialization)


# Schema bazowa (wspólne pola)
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