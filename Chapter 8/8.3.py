"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments
"""
if __name__ == '__main__':
    def make_shirt(size, txt):
        print("Shirt size {} with \"{}\" printed on it.".format(size, txt))
    make_shirt("M", "Hello World")
    make_shirt(46, "ACDC")
