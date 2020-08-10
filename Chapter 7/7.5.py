"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""
if __name__ == '__main__':

    def get_price(age):
        if age < 3:
            ret = 0
        elif age < 12:
            ret = 10
        else:
            ret = 15
        return ret
    age = ""
    while not age.isdigit():
        age = input("How old are you? ")

    print("Your ticket will cost you {}.".format(get_price(int(age))))
