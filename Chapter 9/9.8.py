"""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""


class User:
    def __init__(self, first_name, last_name, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def describe_user(self):
        print(*map(lambda x: f"\n{x} : {self.__getattribute__(x)}", vars(self)))

    def greet_user(self):
        print(f"\nWelcome {self.first_name} {self.last_name}")


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(*self.privileges, sep="\n")


if __name__ == '__main__':
    toor = Admin("root", "toor", ["can invite", "can judge", "can mute", "can hammer"])
    toor.privileges.show_privileges()