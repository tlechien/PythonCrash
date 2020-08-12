"""
10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate program
that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
"""
import json

# functions will do..


def ask_user():
    val = ""
    while not val.isdigit():
        val = input("What's your favorite number? ")
    with open("dump.json", 'w') as dp:
        json.dump(val, dp)


def get_info():
    with open("dump.json", 'r') as dp:
        print(dp.read())


if __name__ == '__main__':
    ask_user()
    get_info()
