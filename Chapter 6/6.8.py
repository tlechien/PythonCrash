if __name__ == '__main__':
    dic1 = {
        'name' : 'SpongeBob Squarepants' ,
        'pet' : 'Snail',
    }
    dic2 = {
        'name' : 'Cruella De vil',
        'pet' : None,
    }
    dic3 = {
        'name': 'Dr. Evil',
        'pet': 'MiniMe',
    }
    dic4 = {
      'name': 'John Wick',
      'pet': 'dog',
    }
    pets = [dic1, dic2, dic3, dic4]
    for dic in pets:
        print("{} & {}".format(dic['name'], dic['pet']))
