"""
4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.
"""
if __name__ == '__main__':
    cubes = [(x+1)**2 for x in range(10)]

    for x in cubes: print(x)