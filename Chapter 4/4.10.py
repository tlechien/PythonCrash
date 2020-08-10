"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Use a slice to
print three items from the middle of the list.
• Print the message The last three items in the list are:. Use a slice to print the
last three items in the list.
"""
if __name__ == '__main__':
    pizzas = [
        "Calzone",
        "Campagnarde",
        "Carbonara",
        "Peperonni",
        "Marinara",
        "Primavera",
        "Capricciosa"
    ]

    print(*pizzas)

    for pizza in pizzas :
        print("I like {} pizza.".format(pizza))

    print("\nI really love pizza!")

    print("The first 3 items in the list are: {}".format(pizzas[:3]))
    print("The middle 3 items in the list are: {}".format(pizzas[len(pizzas)//2-1:(len(pizzas)//2)+2]))
    print("The last 3 items in the list are: {}".format(pizzas[-3:]))