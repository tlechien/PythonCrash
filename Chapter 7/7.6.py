"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
"""
if __name__ == '__main__':
    def get_price(_age):
        if _age < 3:
            ret = 0
        elif _age < 12:
            ret = 10
        else:
            ret = 15
        return ret
    age = ""
    i = 0
    while not age.isdigit() and i < 3:
        age = input("How old are you? (you can exit by writing 'quit') ")
        if age == "quit":
            break
        i += 1

    if age.isdigit():
        print("Your ticket will cost you {}.".format(get_price(int(age))))