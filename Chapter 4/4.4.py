"""
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window.)
"""
if __name__ == '__main__':
    million = list(range(1, 1000001))

    for i in million: print(i)
    #print(' '.join(map(str,million)))