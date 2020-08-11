"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
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
        self.privileges = privileges

    def show_privileges(self):
        print(*self.privileges, sep="\n")


if __name__ == '__main__':
    toor = Admin("root", "toor", ["can invite", "can judge", "can mute", "can hammer"])
    toor.show_privileges()