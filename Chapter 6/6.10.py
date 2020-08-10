"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
so each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""
if __name__ == '__main__':
    dic = {
        'Paul': [6],
        'Pierre': [45, 46 ,48],
        'Denis': [43],
        'Trey': [23, 99],
        'Amin': [4]
    }

    print(*dic.items(), sep='\n')