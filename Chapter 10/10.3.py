"""
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""

if __name__ == '__main__':
    name = input("What's your name? ")
    with open("guess.txt", "w") as file:
        file.write(name)