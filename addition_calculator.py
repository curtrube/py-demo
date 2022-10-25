from multiprocessing.sharedctypes import Value


print("Enter two numbers and I'll add them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nEnter a number: ")
    if first_number == 'q':
        break
    second_number = input("Enter a second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Error, that's not a number")
    else:
        print(f"\nThe answer is: {answer}")