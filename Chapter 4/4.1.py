if __name__ == '__main__':
    pizzas = [
        "Calzone",
        "Campagnarde",
        "Carbonara"
    ]

    print(*pizzas)

    for pizza in pizzas :
        print("I like {} pizza.".format(pizza))

    print("\nI really love pizza!")