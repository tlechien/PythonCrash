if __name__ == '__main__':
    dic = {
        'Amazon' : 'Bresil',
        'Nile' : 'Egypt',
        'Danube': 'Germany'
    }

    for river in dic:
        print("The {} runs through {}.".format(river, dic[river]))

    for river in dic:
        print(river)

    for river in dic:
        print(dic[river])