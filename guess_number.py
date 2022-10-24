from random import randint


def guess_number(answer):
    while True:
        guess = input("Guess a number between 1 and 3: ")

        if guess.isdigit():
            guess = int(guess)

            if answer != guess:
                print("Sorry, You Lost")

                continue_game = play_again()

                if continue_game != True:
                    break

            elif answer == guess:
                print(f"YOU WON!\nThe answer was {answer}")

                continue_game = play_again()

                if continue_game != True:
                    break

        else:
            print(f"Invalid input detected `{guess}` is not a number")
            break


def play_again():
    play_again = input("Would you like to play again? y/n ")

    if play_again.lower() == "y":
        guess_number(randint(1, 3))

    else:
        print("Game Over")

        return False


def main():
    guess_number(randint(1, 3))


if __name__ == "__main__":
    main()
