from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# Zadanie 20 – User (twórca produktu)
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    products: Mapped[list['Product']] = relationship(back_populates='user')


# Zadanie 7 (model) / Zadania 9-15, 17, 20 (CRUD)
class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)  # cena w groszach
    user_id: Mapped[int | None] = mapped_column(ForeignKey('users.id'), nullable=True)
    user: Mapped['User | None'] = relationship(back_populates='products')


# Zadanie 16 – konto bankowe do transakcji
class Account(Base):
    __tablename__ = 'accounts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    balance: Mapped[int] = mapped_column(Integer, default=0)
