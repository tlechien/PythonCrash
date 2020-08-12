"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


if __name__ == '__main__':
    die1 = Die()
    print(f"\nSides:{die1.sides}\n")
    for x in range(10): die1.roll_die()
    die2 = Die(10)
    die3 = Die(20)
    print(f"\nSides:{die2.sides}\n")
    for x in range(10): die2.roll_die()
    print(f"\nSides:{die3.sides}\n")
    for x in range(10): die3.roll_die()
