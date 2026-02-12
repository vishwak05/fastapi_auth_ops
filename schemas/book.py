from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    isbn: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    publication_year: Optional[int] = None
    genre: Optional[str] = None
    price: Optional[float] = None
    language: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class Book(BookBase):
    book_id: int

    class config:
        from_attributes = True