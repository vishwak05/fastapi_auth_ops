from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.dependencies import get_current_user
from auth.database import get_db
from schemas.book import Book, BookCreate, BookUpdate
from models.user import User as UserModel
from services.book_service import BookService

router = APIRouter()

def get_book_service(db: Session = Depends(get_db)):
    return BookService(db)

@router.post("/books/", response_model=Book)
def create_book(
    book: BookCreate, 
    current_user: UserModel = Depends(get_current_user),
    service: BookService = Depends(get_book_service)
):
    return service.create_book(book)

@router.post("/books/batch/", response_model=list[Book])
def create_multiple_books(
    books: list[BookCreate],
    current_user: UserModel = Depends(get_current_user),
    service: BookService = Depends(get_book_service)
):
    return service.create_multiple_books(books)

@router.get("/books/", response_model=list[Book])
def get_all_books(
    skip: int = 0, 
    limit: int = 100, 
    current_user: UserModel = Depends(get_current_user),
    service: BookService = Depends(get_book_service)
):
    return service.get_all_books(skip, limit)

@router.get("/books/{book_id}", response_model=Book)
def get_book(
    book_id: int, 
    current_user: UserModel = Depends(get_current_user),
    service: BookService = Depends(get_book_service)
):
    return service.get_book(book_id)

@router.put("/books/{book_id}", response_model=Book)
def update_book(
    book_id: int, 
    book: BookUpdate, 
    current_user: UserModel = Depends(get_current_user),
    service: BookService = Depends(get_book_service)
):
    return service.update_book(book_id, book)

@router.delete("/books/{book_id}", response_model=Book)
def delete_book(
    book_id: int, 
    current_user: UserModel = Depends(get_current_user),
    service: BookService = Depends(get_book_service)
):
    return service.delete_book(book_id)