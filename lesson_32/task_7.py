from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
        }


if __name__ == "__main__":
    print("Model Product został zdefiniowany.")
    print("Tabela:", Product.__tablename__)
    print("Kolumny:", Product.__table__.columns.keys())