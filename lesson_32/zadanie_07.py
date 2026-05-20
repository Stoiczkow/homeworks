from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "price": self.price}


if __name__ == "__main__":
    p = Product(id=1, name="Klawiatura", price=14999)
    print(f"Produkt: {p.to_dict()}")
    print(f"Tabele w metadata: {list(Base.metadata.tables.keys())}")