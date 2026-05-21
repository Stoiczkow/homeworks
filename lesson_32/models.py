from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer, select

# ✏7. (Proste) SQLAlchemy Async - Definicja Modelu: Zdefiniuj model Product używając
# DeclarativeBase z SQLAlchemy . Model powinien mieć pola: id (int, klucz główny),
# name (String(100)) oraz price (Integer, przechowujący cenę w groszach).

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    
    products = relationship("Product", back_populates="user")
    
    
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[int] = mapped_column(Integer())
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user = relationship("User", back_populates="products")
    
    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "user": self.user_id}
    
    
class Account(Base):
    __tablename__ = "accounts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int] = mapped_column(Integer())
    
    def to_dict(self):
        return {"id": self.id, "balance": self.balance}
