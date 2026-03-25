from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = 'sqlite:///todo.db'

# silnik db
engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()