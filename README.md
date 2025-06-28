# 📚 Book Review API

A simple and efficient backend service to manage books and their reviews, built using **FastAPI**, **SQLAlchemy**, **Redis** (for caching), and **Pytest** (for testing).

---

## 📁 Project Structure

```bash
book_review_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app and router inclusion
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic models for request/response
│   ├── crud.py              # CRUD logic
│   ├── cache.py             # Redis cache handler
│   └── routers/
│       ├── __init__.py
│       ├── books.py         # Books endpoints
│       └── reviews.py       # Reviews endpoints
│
├── tests/
│   ├── __init__.py
│   └── test_books.py        # Unit tests for the books module
│
├── venv/                    # Python virtual environment
├── requirements.txt         # Python dependencies
└── README.md                # Project overview and setup guide
```

---

## 🚀 Features

- Add, list books and reviews.
- Caching support using Redis.
- Graceful fallback when Redis is down.
- Interactive API docs with Swagger (OpenAPI).
- Pytest-based test suite with mocking.

---

## 🛠️ Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/book_review_api.git
cd book_review_api
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Redis

Make sure Redis server is running locally:
```bash
# Windows
redis-server
```

Check it:
```bash
redis-cli
```

If installed, you should enter the Redis prompt.

### 5. Run the API server

```bash
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📦 API Endpoints

### 📘 Books

| Method | Endpoint         | Description       |
|--------|------------------|-------------------|
| GET    | `/books/`        | Get list of books |
| POST   | `/books/`        | Add a new book    |

### 📝 Reviews

| Method | Endpoint                         | Description                  |
|--------|----------------------------------|------------------------------|
| GET    | `/books/{book_id}/reviews`       | Get reviews for a book       |
| POST   | `/books/{book_id}/reviews`       | Add a review to a book       |

---

## 📄 Example Request (POST /books/)

```json
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
}
```

### Response:

```json
{
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
}
```

---

## 🧪 Running Tests

```bash
pytest tests/
```

### Sample Output

```
tests/test_books.py::test_create_book PASSED
tests/test_books.py::test_get_books PASSED
tests/test_books.py::test_cache_miss_fallback PASSED
```

---

## 💾 Caching with Redis

- GET `/books/` checks Redis for a cached response.
- If Redis is unreachable or key is not found, it fetches from DB and updates the cache.
- Helps reduce DB load and improve performance.

---

## ⚠️ Pydantic v2 Notice

To use `.from_orm()` in Pydantic v2, make sure your schema includes:

```python
class Book(BaseModel):
    title: str
    author: str
    id: int

    model_config = ConfigDict(from_attributes=True)
```

---

## 🔍 Future Improvements

- Add pagination to GET endpoints.
- Authentication for admin operations.
- Frontend for interacting with the API.
- Dockerize for deployment.

---

## 🧑‍💻 Author

**Amrita Sinha**  
📧 amrittasinha45@gmail.com  
🔗 GitHub: [github.com/amritasinha](https://github.com/AmritaSinha8976)
