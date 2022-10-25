filename = "guest_book.txt"


def greet_user():
    name = input("Enter your name: ")

    if not name:
        print("No input detected")

    else:
        name.lower()
        print(f"Hello, {name.title()}")

    return name


def main():

    while True:
        name = greet_user()

        with open(filename, "a") as file_object:
            file_object.write(f"{name}\n")


if __name__ == "__main__":
    main()
