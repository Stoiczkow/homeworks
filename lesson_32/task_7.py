"""
Zdefiniuj model Product używając DeclarativeBase z SQLAlchemy.
Pola:
- id: int, klucz główny
- name: String(100)
- price: Integer (cena w groszach)
"""

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer) 
