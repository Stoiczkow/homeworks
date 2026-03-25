import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# ZADANIE 9
zadania_tagi = Table(
    'zadania_tagi',
    Base.metadata,
    Column('zadanie_id', ForeignKey('zadania.id'), primary_key=True),
    Column('tag_id', ForeignKey('tagi.id'), primary_key=True),
)
# koniec zadania

class Zadanie(Base):
    __tablename__ = 'zadania' # Nazwa tabeli w bazie danych
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    opis: Mapped[str] = mapped_column(String, nullable=False)
    zrobione: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    data_utworzenia: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
    # ZADANIE 9
    tagi: Mapped[list["Tag"]] = relationship(secondary=zadania_tagi, back_populates="zadania")
    # koniec zadania
    
    def __repr__(self):
        return f"<Zadanie(id={self.id}, opis='{self.opis}', zrobione={self.zrobione})>"


# ZADANIE 9
class Tag(Base):
    __tablename__ = 'tagi'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nazwa: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    zadania: Mapped[list["Zadanie"]] = relationship(secondary=zadania_tagi, back_populates="tagi")

    def __repr__(self):
        return f"<Tag(id={self.id}, nazwa='{self.nazwa}')>"
# koniec zadania