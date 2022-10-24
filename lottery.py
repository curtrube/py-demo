from random import choice

lottery_selection = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")


def lottery():
    winnning_ticket = []

    for i in range(4):
        winnning_ticket.append(choice(lottery_selection))

    return winnning_ticket


my_ticket = [1, "a", 5, "e"]
count = 0

while True:
    winning_ticket = lottery()
    print(f"The lottery numbers are: {winning_ticket}")
    count += 1
    if my_ticket == winning_ticket:
        print(f"YOU WON!\n The winning ticket: {winning_ticket}")
        print(f"It took {count} tries to win.")
        break
