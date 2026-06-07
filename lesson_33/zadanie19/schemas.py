from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    id: int
    name: str

class UserCreate(BaseModel):
    name: str

class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int

class PostBase(BaseModel):
    id: int
    title: str
    content: str
    author_id: int

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author_id: int

class CommentBase(BaseModel):
    content: str
    post_id: int

class CommentWithId(BaseModel):
    id: int
    content: str
    post_id: int

class SummaryBase(BaseModel):
    id: int
    content: str
    post_id: int