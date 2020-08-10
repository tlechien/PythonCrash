"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""
if __name__ == '__main__':
    topping = None
    while topping != "quit":
        if topping:
            print("I'll add %s to your pizza!" % topping)
        topping = input("What topping would you like? (enter 'quit' when you are done.) ")