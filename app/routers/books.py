from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database
from app.cache import get_cached_books, set_cached_books

router = APIRouter()

@router.get("/", response_model=list[schemas.Book])
def get_books(db: Session = Depends(database.get_db)):
    # Try cache first
    cached = get_cached_books()
    if cached:
        return cached

    # Fallback: fetch from DB
    books = crud.get_books(db)

    # Serialize for caching
    serialized_books = [schemas.Book.from_orm(book).dict() for book in books]
    set_cached_books(serialized_books)

    return books


@router.post("/", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db=db, book=book)
