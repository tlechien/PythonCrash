if __name__ == '__main__':
    ordinals = list(range(1, 10))
    end = ["st", "nd", "rd"]
    string = ""
    for x in ordinals:
        string += (str(x) + end[x - 1] + " ") if x <= len(end) else (str(x) + "th ")

    print(string.lstrip())

