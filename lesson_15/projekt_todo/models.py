from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

zadania_tagi = Table(
    'zadania_tagi',
    Base.metadata,
    Column('zadanie_id', Integer, ForeignKey('zadania.id')),
    Column('tag_id', Integer, ForeignKey('tagi.id'))
)


class Zadanie(Base):
    __tablename__ = 'zadania'

    id = Column(Integer, primary_key=True)
    opis = Column(String, nullable=False)
    zrobione = Column(Boolean, nullable=False, default=False)
    priorytet = Column(Integer, default=1)
    data_utworzenia = Column(DateTime, default=datetime.utcnow)
    tagi = relationship('Tag', secondary=zadania_tagi, back_populates='zadania')


class Tag(Base):
    __tablename__ = 'tagi'

    id = Column(Integer, primary_key=True)
    nazwa = Column(String, nullable=False, unique=True)
    zadania = relationship('Zadanie', secondary=zadania_tagi, back_populates='tagi')
