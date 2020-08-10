"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""
if __name__ == '__main__':
    sandwich_orders = ["Tuna", "Pastrami", "Parma", "Dagobert", "Pastrami", "Veggie", "Parma", "Americano", "Pastrami"]
    finished_sandwiches = []
    print("Deli has ran out of Pastrami.")
    while "Pastrami" in sandwich_orders:
        sandwich_orders.remove("Pastrami")

    while sandwich_orders:
        print("I made your {}".format(sandwich_orders[0]))
        finished_sandwiches.append(sandwich_orders[0])
        sandwich_orders.pop(0)

    print(*finished_sandwiches)