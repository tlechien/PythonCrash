if __name__ == '__main__':
    dic = {
        "loop": "cycle repeating itself",
        "alien": "they are green and slow",
        "ternary": "functionality Python could improve",
        "c": "segfault",
        "python": "when monty, their jokes are great"
    }

    print(*map(lambda x : "\n{}: {}".format(x[0],x[1]), dic.items()))