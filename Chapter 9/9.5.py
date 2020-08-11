"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""
class User:
    def __init__(self, first_name, last_name, login_attempts, admin=False, gender=None):
        # self.first_name = first_name
        # self.last_name = last_name
        # self.login_attempts = login_attempts
        # self.admin = admin
        # self.gender = gender
        self.__dict__.update(locals())
        self.__dict__.pop("self")

    def describe_user(self):
        print(*map(lambda x: f"\n{x} : {self.__getattribute__(x)}", vars(self)))

    def greet_user(self):
        print(f"\nWelcome {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts= 0


if __name__ == '__main__':
    us = User("Marvin", "The Paranoid Android", 0, True, "robot")
    us.describe_user()
    us.increment_login_attempts()
    us.increment_login_attempts()
    us.increment_login_attempts()
    print(us.login_attempts)
    us.reset_login_attempts()
    print(us.login_attempts)
