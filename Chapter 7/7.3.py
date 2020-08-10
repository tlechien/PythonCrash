"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""
if __name__ == '__main__':
    number = ""
    while not number.isdigit():
        number = input("Enter a number: ")

    number = int(number)

    print("The number {} {} a multiple of 10.".format(number, ("isn't", "is")[number % 10 == 0]))
