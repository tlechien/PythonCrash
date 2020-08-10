"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
"""
if __name__ == '__main__':
    favorite_fruits = ['banana', 'kiwi', "pear"]
    test_fruits = ("apple", "banana", "mango", "strawberry", "pear")

    for fruit in test_fruits:
        if fruit in favorite_fruits:
            print("Oh you like {}s too?".format(fruit))
