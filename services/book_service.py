from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import HTTPException

from models.user import User as UserModel
from models.book import Book as BookModel
from schemas.book import Book, BookCreate, BookUpdate

class BookService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_book(self, book: BookCreate) -> Book:
        db_book = BookModel(**book.model_dump())
        
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        
        return db_book
    
    def create_multiple_books(self, books: list[BookCreate]) -> list[Book]:
        db_books = []

        for book in books:
            db_book = BookModel(**book.model_dump())

            self.db.add(db_book)
            self.db.commit()
            self.db.refresh(db_book)

            db_books.append(db_book)
        
        return db_books
    
    def get_all_books(self, skip: int = 0, limit: int = 100) -> List[Book]:
        return self.db.query(BookModel).offset(skip).limit(limit).all()
    
    def get_book(self, book_id: int) -> Optional[Book]:
        db_book = self.db.query(BookModel).filter(BookModel.book_id == book_id).first()

        if not db_book:
            raise HTTPException(status_code=404, detail="Book not found")
        
        return db_book
    
    def update_book(self, book_id: int, book: BookUpdate) -> Book:
        db_book = self.db.query(BookModel).filter(BookModel.book_id == book_id).first()

        if not db_book:
            raise HTTPException(status_code=404, detail="Book not found")
        
        update_data = book.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_book, key, value)
        
        self.db.commit()
        self.db.refresh(db_book)

        return db_book
    
    def delete_book(self, book_id: int) -> Book:
        db_book = self.db.query(BookModel).filter(BookModel.book_id == book_id).first()

        if not db_book:
            raise HTTPException(status_code=404, detail="Book not found")
        
        self.db.delete(db_book)
        self.db.commit()
        
        return db_book