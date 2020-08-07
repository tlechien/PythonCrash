if __name__ == '__main__':
    age = None
    while type(age) != int:
        age = int(input("How old are you"))

    if age < 2:
        print("You're a baby.")
    elif age > 4:
        print("You're a toddler.")
    elif age < 13:
        print("You're a kid.")
    elif age < 65:
        print("You're an adult.")
    else:
        print("You're an elder.")
