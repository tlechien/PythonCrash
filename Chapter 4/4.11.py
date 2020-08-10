"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite
pizzas are:, and then use a for loop to print the first list. Print the message
My friend’s favorite pizzas are:, and then use a for loop to print the second
list. Make sure each new pizza is stored in the appropriate list.
"""
if __name__ == '__main__':
    pizzas = [
        "Calzone",
        "Campagnarde",
        "Carbonara"
    ]

    friend_pizzas = pizzas.copy()
    friend_pizzas.append("Peperonni")
    if pizzas == friend_pizzas:
        print("same")
    else:
        print("different")

    print(*pizzas)
    print(*friend_pizzas)

    for pizza in pizzas :
        print("I like {} pizza.".format(pizza))

    print("\nI really love pizza!")