import json

filename = "favorite_number1.json"

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    print("Error: file not found")
else:
    print(f"Your favorite number is: {number}")
