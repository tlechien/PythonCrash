"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
"""
if __name__ == '__main__':
    def favorite_book(title):
        print("One of my favorite books is %s." % title)
    favorite_book("Alice in Wonderland")
    favorite_book("Monogatari serie")