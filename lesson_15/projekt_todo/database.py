from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite:///todo.db"

engine = create_engine(DB_URL) # Jak dodamy tutaj w nawiasie echo = True będziemy mieć pokazane zapytania SELECT jakie wykonuje program

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    return db