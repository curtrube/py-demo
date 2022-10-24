from random import randint


class Dice:
    def __init__(self):
        self.sides = 6

    def roll_dice(self):
        """Roll the dice"""
        roll = randint(1, self.sides)

        return roll


my_roll = Dice()
my_roll.sides = 20

for i in range(10):
    print(my_roll.roll_dice())
