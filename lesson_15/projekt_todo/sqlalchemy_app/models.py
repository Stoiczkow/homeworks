from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Zadania(Base):
    __tablename__ = "zadania"

    id = Column(Integer, primary_key=True)
    opis = Column(String, nullable=False)
    zrobione = Column(Boolean, nullable=False, default=False)
    data_utworzenia = Column(DateTime, default=datetime.datetime.now())
    tags = relationship("Tag",
                        secondary="zadania_tags",
                        back_populates="zadania")
    
    def __repr__(self):
        return f"{self.opis}"

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    nazwa = Column(String, nullable=False)
    zadania = relationship("Zadania",
                        secondary="zadania_tags",
                        back_populates="tags")
    def __repr__(self):
        return f"{self.nazwa}"


class ZadaniaTag(Base):
    __tablename__ = "zadania_tags"

    id = Column(Integer, primary_key=True)
    zadanie_id = Column(Integer, ForeignKey("zadania.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))