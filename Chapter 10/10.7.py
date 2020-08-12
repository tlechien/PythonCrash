"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
"""

if __name__ == '__main__':
    val = True
    total = 0
    while val:
        val = input("Please enter an integer: ")
        if not val:
            break
        try:
            val = int(val)
        except ValueError:
            print("You didn't enter an integer.")
        else:
            total += val
    print(f"total: {total}")