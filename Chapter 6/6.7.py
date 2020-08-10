"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""
if __name__ == '__main__':
    dic1 = {
        "first_name": "Spongebob",
        "last_name": "Squarepants",
        "city": "Bikini Bottom"
    }
    dic2 = {
        "first_name": "Patrick",
        "last_name": "Star",
        "city": "Bikini Bottom"
    }
    dic3 = {
        "first_name": "Mr.",
        "last_name": "Krabs",
        "city": "Bikini Bottom"
    }
    people = [dic1, dic2, dic3]

    print(*map(lambda x: "\n{}".format(x), people))
