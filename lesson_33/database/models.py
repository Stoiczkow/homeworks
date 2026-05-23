# === file: models.py ===
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.database import Base


# Model SQLAlchemy - reprezentuje tabelę w bazie
class UserORM(Base):
    """
    Model ORM użytkownika.
    Definiuje strukturę tabeli 'users' w bazie danych.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    age = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relacja do zamówień (One-to-Many)
    orders = relationship("OrderORM", back_populates="user")


class OrderORM(Base):
    """Model ORM zamówienia."""

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relacja do użytkownika (Many-to-One)
    user = relationship("UserORM", back_populates="orders")