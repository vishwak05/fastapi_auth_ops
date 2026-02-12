from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ.get("DATABASE_USERNAME")
password = os.environ.get("DATABASE_PASSWORD")
host = os.environ.get("DATABASE_HOST")
port = os.environ.get("DATABASE_PORT")
database = os.environ.get("DATABASE_NAME")

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()