from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime
import datetime
from sqlalchemy.orm import relationship
Base = declarative_base()

zadanie_tag = Table(
    "zadanie_tag",
    Base.metadata,
    Column("zadanie_id", Integer, ForeignKey("zadanie.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tagi.id"), primary_key=True)
)

class Tag(Base):
    __tablename__ = "tagi"

    id = Column(Integer, primary_key=True)
    nazwa = Column(String, nullable=False)
    zadania = relationship("Zadanie", secondary=zadanie_tag, back_populates="tagi")

class Zadanie(Base):
    __tablename__ = "zadanie"

    id = Column(Integer, primary_key=True)
    opis = Column(String, nullable=False)
    zrobione = Column(Boolean, default=False, nullable=False)
    data_utworzenia = Column(DateTime, default=datetime.datetime.utcnow)
    tagi = relationship("Tag", secondary=zadanie_tag, back_populates="zadania")

    def __repr__(self):
        return f"<Zadanie(id={self.id}, opis='{self.opis}', zrobione={self.zrobione})>"