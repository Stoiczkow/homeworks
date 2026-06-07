from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class BookORM(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=False, index=True, nullable=False)
    author = relationship("AuthorORM", back_populates="books")
    year = Column(Integer, unique=False, index=True)
    price = Column(Float, unique=False, index=True, nullable=False)
    category = Column(String(50), unique=False, index=True, nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

class AuthorORM(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=False, index=True, nullable=False)
    books = relationship("BookORM", back_populates="author")

class StatsORM(Base):
    __tablename__ = "stats"
    id = Column(Integer, primary_key=True, autoincrement=True)
    deleted_books_count = Column(Integer)