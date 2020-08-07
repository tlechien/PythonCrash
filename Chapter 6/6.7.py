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
