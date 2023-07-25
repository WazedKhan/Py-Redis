import redis
from redis.commands.json.path import Path
import redis.commands.search.reducers as reducers
import redis.commands.search.aggregation as aggregations
from redis.commands.search.query import NumericFilter, Query
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType

# Connecting to Redis database.
r = redis.Redis(host="localhost", port=6379)

# creating some test data to add in redis database
user1 = {
    "name": "Paul John",
    "email": "paul.john@example.com",
    "age": 42,
    "city": "London",
}
user2 = {
    "name": "Eden Zamir",
    "email": "eden.zamir@example.com",
    "age": 29,
    "city": "Tel Aviv",
}
user3 = {
    "name": "Paul Zamir",
    "email": "paul.zamir@example.com",
    "age": 35,
    "city": "Tel Aviv",
}

# Defining indexed fields and their data types using schema
schema = (
    TextField("$.name", as_name="name"),
    TagField("$.city", as_name="city"),
    NumericField("$.age", as_name="age"),
)

rs = r.ft("idx:users")
rs.create_index(
    schema, definition=IndexDefinition(prefix=["user:"], index_type=IndexType.JSON)
)

r.json().set("user:1", Path.root_path(), user1)
r.json().set("user:2", Path.root_path(), user2)
r.json().set("user:3", Path.root_path(), user3)

res = rs.search(Query("Paul @age:[30 40]"))

print(res)
