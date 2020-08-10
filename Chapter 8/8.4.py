"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""
if __name__ == '__main__':
    def make_shirt(size="large", txt="I love Python"):
        print("Shirt size {} with \"{}\" printed on it.".format(size, txt))
    make_shirt("M", "Hello World")
    make_shirt(46, "ACDC")
    make_shirt()