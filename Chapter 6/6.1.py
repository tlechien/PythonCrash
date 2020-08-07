if __name__ == '__main__':
    dic = {
        "first_name": "Spongebob",
        "last_name": "Squarepants",
        "city": "Bikini Bottom"
    }

    print(*dic.items())
    # or
    print(*dic.values())
