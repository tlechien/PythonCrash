"""
7-10. Dream Vacation: Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.
"""
if __name__ == '__main__':
    answers = {}

    while 1:
        name = input("What's your name? ")
        answers[name] = input("If you could visit one place in the world, where would you go? ")
        if input("Would you like to add another entry? ").lower() != "yes":
            break

    print(*map(lambda x: "\n{} would love to go to {}".format(x, answers[x]),answers))