import json

filename = "favorite_number.json"


def save_number(favorite_number):
    """Save favorite number to disk"""
    with open(filename, "w") as f:
        json.dump(favorite_number, f)


def get_favorite_number():
    """Read favorite number from disk"""
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def print_favorite_number():
    """Prints the favorite number"""
    favorite_number = get_favorite_number()
    if favorite_number:
        print(f"I know your favorite number is {favorite_number}")
    else:
        favorite_number = input("What is your favorite number? ")
        save_number(favorite_number)
        print(f"We'll remember your favorite number is: {favorite_number}")


print_favorite_number()
