import redis
import json

# Connect to local Redis server
try:
    redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    redis_client.ping()
    print("✅ Redis connected")
except redis.exceptions.ConnectionError:
    redis_client = None
    print("❌ Redis not available")


def get_cached_books():
    if redis_client:
        cached = redis_client.get("books")
        if cached:
            return json.loads(cached)
    return None


def set_cached_books(books):
    if redis_client:
        redis_client.set("books", json.dumps(books), ex=60)  # cache for 60 seconds
