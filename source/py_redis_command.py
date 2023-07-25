capitals = {}

# redis: SET Bahamas Nassau => OK
capitals["Bahamas"] = "Nassau"

# redis: GET Bahamas => "Nassau"
print(capitals.get("Bahamas")) # "Nassau"