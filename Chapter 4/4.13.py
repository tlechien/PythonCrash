if __name__ == '__main__':
    buffet = ("bread", "corn", "rice", "salad", "sandwich")

    for x in buffet: print(x)

    try:
        buffet[2] = "POTATO"
    except TypeError:
        print("Python cannot do that!")
