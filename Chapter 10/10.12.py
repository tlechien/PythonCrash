"""
10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
"""
import json


def ask_user():
    val = ""
    while not val.isdigit():
        val = input("What's your favorite number? ")
    with open("dump.json", 'r+') as dp:
        if not dp.read().count('\"'+val+'\"'):
            json.dump(val, dp)
        else:
            print("(That number is already registered)")


def get_info():
    with open("dump.json", 'r') as dp:
        print(dp.read().strip('"').replace('""', '\n'))


if __name__ == '__main__':
    ask_user()
    get_info()
