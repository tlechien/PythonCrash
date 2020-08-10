"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""
if __name__ == '__main__':
    dic = {
        "first_name": "Spongebob",
        "last_name": "Squarepants",
        "city": "Bikini Bottom"
    }

    print(*dic.items())
    # or
    print(*dic.values())
