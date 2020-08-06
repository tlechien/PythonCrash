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