"""
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

if __name__ == '__main__':
    with open("guest_book.txt", "a") as file:
        name = True
        while name:
            name = input("What's your name? ")
            if name: file.write(name + "\n")
