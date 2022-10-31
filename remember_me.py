import json


def get_stored_username(filename):
    """Get stored username if avaiable"""
    try:
        with open(filename) as f:
            username = json.load(f)

    except FileNotFoundError:
        return None

    else:
        return username


def get_new_username(filename):
    """Prompt user for name and save to disk"""
    username = input("What is your name? ")

    with open(filename, "w") as f:
        json.dump(username, f)

    return username


def greet_user(filename):
    """Greet user by name"""
    username = get_stored_username(filename)

    if username:
        is_current_user = input(f"Are you {username.title()} Y/N ")

        if is_current_user.lower() == "y":
            print(f"Welcome back, {username.title()}")

        else:
            username = get_new_username(filename)
            print(f"We'll remember you when you come back, {username.title()}!")


def main():
    """Main function"""
    filename = "username.json"
    greet_user(filename)


if __name__ == "__main__":
    main()
