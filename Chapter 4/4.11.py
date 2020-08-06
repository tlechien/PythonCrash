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