from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

__SQLALCHEMY_DATABASE_URL = "sqlite:///./instance/database.db"

__engine = create_engine(__SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=__engine)

Base = declarative_base()

engine = __engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db_and_tables():
    Base.metadata.create_all(bind=__engine)