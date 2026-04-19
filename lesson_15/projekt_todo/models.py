from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey # typy danych
import datetime
from sqlalchemy.orm import relationship # import relationship

Base = declarative_base() # klasa bazowa dla tabel

#c. Zdefiniowania relacji relationship w modelach Zadanie i Tag. od tags i w klasie tag

class Zadania(Base):
    __tablename__ = "zadania"

    id = Column(Integer, primary_key=True)
    opis = Column(String, nullable=False) 
    zrobione = Column(Boolean, nullable=False, default=False)
    tags = relationship("Tag", 
                        secondary="zadania_tags", 
                        back_populates="zadania")
    
    def __repr__(self):
        return f"{self.opis}"

    # Zadanie 5 – Dodanie daty utworzenia (SQLAlchemy)
    # W pliku sqlalchemy_app/models.py, do klasy Zadanie dodaj nową kolumnę: data_utworzenia = Column(DateTime, default=datetime.datetime.utcnow). Nie zapomnij o imporcie from sqlalchemy import DateTime i import datetime. Następnie wygeneruj i zastosuj nową migrację Alembic.

    data_utworzenia = Column(DateTime, default=datetime.datetime.now())
    # datetime.now() - metoda

# Zadanie 9 – Dodanie tagów do zadań (SQLAlchemy)
# Rozbuduj aplikację ORM o system tagów. Będziesz potrzebować:
# a. Nowego modelu Tag (id, nazwa).
# b. Tabeli pośredniej do obsługi relacji wiele-do-wielu między zadaniami a tagam

# Stworzenie nowej kolumny w bazie

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    nazwa = Column(String, nullable=False)
    zadania = relationship("Zadania",
                           secondary="zadania_tags",
                           back_populates="tags")

    def __repr__(self):
        return f"{self.nazwa}"

# Jak zrobić relację
# Jedno zadanie może mieć wiele tagów 
# tablea powiazan z 2 poprzednich tabel

class ZadaniaTag(Base):
    __tablename__ = "zadania_tags"

    id = Column(Integer, primary_key=True)
# dodanie klucza obcego # stworzenie relacji
    zadanie_id = Column(Integer, ForeignKey("zadania.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))
