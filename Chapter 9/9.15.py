"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket.
Write a loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning ticket.
"""
import random

if __name__ == '__main__':
    lottery = [random.randint(0, 9) for i in range(10)]
    for x in range(5): lottery.append(chr(random.randint(0, 26) + 97))
    random.shuffle(lottery)
    ticket = ['d','e', 2, 9]

    i = 0
    while ticket != random.sample(lottery, 4):
        i += 1
    print(f"total: {i}")
