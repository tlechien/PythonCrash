"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""


class User:
    def __init__(self, first_name, last_name, admin=False, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.admin = admin
        self.gender = gender

    def describe_user(self):
        print(*map(lambda x: f"\n{x} : {self.__getattribute__(x)}", vars(self)))

    def greet_user(self):
        print(f"\nWelcome {self.first_name} {self.last_name}")


if __name__ == '__main__':
    us = User("Marvin", "The Paranoid Android", True, "robot")
    us.describe_user()
    us.greet_user()
