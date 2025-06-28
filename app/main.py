from fastapi import FastAPI
from app.routers import books, reviews
from app.database import Base, engine

app = FastAPI(
    
    title="Book Review API",
    description="A simple backend to manage books and reviews.",
    version="1.0.0"
)

# Create tables at startup
Base.metadata.create_all(bind=engine)

# Include routes from routers
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(reviews.router, prefix="/books", tags=["Reviews"])
