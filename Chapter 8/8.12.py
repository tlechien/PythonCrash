"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that’s being ordered. Call the function three times, using a different number
of arguments each time.
"""
if __name__ == '__main__':
    def saaaaandwiiich(*orders):
        print("\nMaking a sandwich with")
        print("", *orders, sep="\n - ")

    saaaaandwiiich("tuna", "corn", "mayonnaise", "cheese")
    saaaaandwiiich("tuna", "corn", "ham", "mustard", "salad")
    saaaaandwiiich("ham", "ketchup", "cheese")
