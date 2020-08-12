"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize.
"""

import random

if __name__ == '__main__':
    lottery = [random.randint(0, 9) for i in range(10)]
    for x in range(5): lottery.append(chr(random.randint(0, 26) + 97))
    random.shuffle(lottery)
    print(f"The winning ticket is {''.join(map(str, random.sample(lottery,4)))}")
