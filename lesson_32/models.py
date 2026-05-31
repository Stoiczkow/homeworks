from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, select, ForeignKey
from typing import List



class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[int] = mapped_column(Integer())
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))

    user: Mapped["User"] = relationship(back_populates="products")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}

class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int] = mapped_column(Integer())

class User(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    products: Mapped[List["Product"]] = relationship(back_populates="user")