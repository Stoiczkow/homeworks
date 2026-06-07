from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base


class UsersORM(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    posts = relationship("PostORM", back_populates="author", cascade="all, delete-orphan")

class PostORM(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), unique=False, index=True, nullable=False)
    content = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    author = relationship("UsersORM", back_populates="posts")
    comments = relationship("CommentORM", back_populates="post", cascade="all, delete-orphan")
    summary = relationship("SummaryORM", back_populates="post", cascade="all, delete-orphan")

class CommentORM(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String(250), unique=False, index=True, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    sentiment = Column(String, unique=False, nullable=True)

    post = relationship("PostORM", back_populates="comments")

class SummaryORM(Base):
    __tablename__ = "summary"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String(250), unique=False, index=True, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    post = relationship("PostORM", back_populates="summary")