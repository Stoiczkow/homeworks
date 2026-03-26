from sqlalchemy import Column, Integer, String, Boolean, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship

Base = declarative_base()

zadanie_tag = Table(
    'zadanie_tag',
    Base.metadata,
    Column('zadanie_id', Integer, ForeignKey('zadanie.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True)
)

class Zadanie(Base):
    __tablename__ = 'zadanie'

    id = Column(Integer, primary_key=True)
    opis = Column(String, nullable=False)
    zrobione = Column(Boolean, default=False, nullable=False)
    priorytet = Column(Integer, default=1, nullable=True)
    data_utworzenia = Column(DateTime, default=datetime.utcnow)
    tagi = relationship("Tag", secondary=zadanie_tag, back_populates="zadania")

    def __repr__(self):
        return f"<Zadanie(id={self.id}, opis={self.opis}, priorytet={self.priorytet}, zrobione={self.zrobione})>"


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    nazwa = Column(String, nullable=False, unique=True)

    zadania = relationship("Zadanie", secondary=zadanie_tag, back_populates="tagi")

    def __repr__(self):
        return f"<Tag(id={self.id}, nazwa={self.nazwa})>"