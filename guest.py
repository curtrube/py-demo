filename = "guest.txt"

name = input("Enter your name: ")

with open(filename, "a") as file_object:
    file_object.write(name)
