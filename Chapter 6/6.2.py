"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
"""
if __name__ == '__main__':
    dic = {
        'Paul': 6,
        'Pierre': 45,
        'Denis': 43,
        'Trey': 23,
        'Amin': 4
    }

    print(*dic.items(), sep='\n')