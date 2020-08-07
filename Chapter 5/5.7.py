if __name__ == '__main__':
    favorite_fruits = ['banana', 'kiwi', "pear"]
    test_fruits = ("apple", "banana", "mango", "strawberry", "pear")

    for fruit in test_fruits:
        if fruit in favorite_fruits:
            print("Oh you like {}s too?".format(fruit))
