import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)
r.set("foo", "bar")
value = r.get("foo")

r.hset("user-session:123", mapping={
    "name": "John",
    "surname": "Smith",
    "company": "Redis",
    "age": 29
})

user_123 = r.hgetall("user-session:123")

print(user_123)