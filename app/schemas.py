from pydantic import BaseModel
from typing import List, Optional

# --- Book Schemas ---

class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class Book(BaseModel):
    id: int
    title: str
    author: str

    model_config = {
        "from_attributes": True  # ✅ For using .from_orm()
    }


# --- Review Schemas ---

class ReviewBase(BaseModel):
    content: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True
