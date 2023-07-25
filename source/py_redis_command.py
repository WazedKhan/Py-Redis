capitals = {}

# single key value store

# redis: SET Bahamas Nassau => OK
capitals["Bahamas"] = "Nassau"

# redis: GET Bahamas => "Nassau"
print(capitals.get("Bahamas")) # "Nassau"


# multiple keys values store

# redis: MSET Lebanon Beirut Norway Oslo France Paris
capitals.update({
    "Lebanon": "Beirut",
    "Norway": "Oslo",
    "France": "Paris"
})

# redis: MGET Beirut France Bahamas
print([capitals[name] for name in ("Lebanon", "Norway", "France")])


# check if a key exists

# redis: EXISTS Norway => 1
# redis: EXISTS Sweden => 0
print("Norway" in capitals) # True
print("Sweden" in capitals) # False


