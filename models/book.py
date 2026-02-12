from sqlalchemy import Column, Integer, String, Numeric
from auth.database import Base

class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    isbn = Column(String, unique=True, index=True)
    author = Column(String, index=True)
    publisher = Column(String)
    publication_year = Column(Integer)
    genre = Column(String, index=True)
    price = Column(Numeric(10, 2))
    language = Column(String, index=True)
