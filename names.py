from name_function import get_formatted_name

print("Enter 'q' anytime to quit.")

while True:
    first_name = input("\nPlease enter first name: ")
    if first_name == "q":
        break
    last_name = input("\nPlease enter last name: ")
    if last_name == "q":
        break

    print(get_formatted_name(first_name, last_name))
