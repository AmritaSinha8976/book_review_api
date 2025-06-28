from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()

@router.get("/{book_id}/reviews", response_model=list[schemas.Review])
def get_reviews(book_id: int, db: Session = Depends(database.get_db)):
    return crud.get_reviews_for_book(db, book_id=book_id)


@router.post("/{book_id}/reviews", response_model=schemas.Review, status_code=201)
def create_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(database.get_db)):
    return crud.create_review_for_book(db=db, book_id=book_id, review=review)
