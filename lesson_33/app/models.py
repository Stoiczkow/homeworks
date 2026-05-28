from sqlalchemy import JSON, Column, Float, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class UserORM(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    posts = relationship("PostORM", back_populates="author")
    comments = relationship("CommentORM", back_populates="author")
    
class PostORM(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    author = relationship("UserORM", back_populates="posts")
    comments = relationship("CommentORM", back_populates="post")
    
class CommentORM(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"))
    author_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    post = relationship("PostORM", back_populates="comments")
    author = relationship("UserORM", back_populates="comments")
    
class ProductORM(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    discount_percent = Column(Float, nullable=True)
    category = Column(Text, nullable=False)
    tags = Column(JSON, default=list)

class AuthorORM(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(255), unique=True, nullable=False)
    
    books = relationship(
        "BookORM", 
        back_populates="author", 
        cascade="all, delete"
        )
    
    
    
class BookORM(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    author_id = Column(
    Integer,
    ForeignKey("authors.id"),
    nullable=False)
    
    author = relationship("AuthorORM", back_populates="books")