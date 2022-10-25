filename = "programming_poll.txt"

while True:
    answer = input("Why do you like programming? ")
    if not answer:
        print("No Input")
    else:
        with open(filename, "a") as file_object:
            file_object.write(f"{answer}\n")
