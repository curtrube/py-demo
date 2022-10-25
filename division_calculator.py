print("Enter two numbers and I'll divide them!")
print("Enter 'q' to quit")

while True:
    first_number = input("\nEnter first number: ")
    if first_number == "q":
        break
    second_number = input("Enter second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(f"Answer: {answer}")
