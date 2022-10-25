# filename = "pi_digits.txt"
filename = "pi_million_digits.txt"
pi_string = ""

while True:
    birthday = input("Enter your birthday in `MMDDYYYY` format: ")

    if len(birthday) != 8:
        print("Invalid Input")

    else:
        with open(filename) as file_object:
            lines = file_object.readlines()

        for line in lines:
            pi_string += line.strip()

        if birthday in pi_string:
            print("HooRay! Your birthday is in the first million digits of Pi")
        else:
            print("Sorry, your birthday is not the first million digits of Pi")
