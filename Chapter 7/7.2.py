"""
7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready.
"""
if __name__ == '__main__':
    count = ""
    while not count.isdigit():
        count = input("How many people? ")

    if int(count) > 8:
        print("You'll have to wait for a table.")
    else:
        print("The table is ready.")
