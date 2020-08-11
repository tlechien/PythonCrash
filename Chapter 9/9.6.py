"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""


class Restaurant:
    def __init__(self, name, cuisine, number_served=0):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = number_served

    def describe_restaurant(self):
        print(*map(lambda x: f"\n{x} : {self.__getattribute__(x)}", vars(self)))

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, nbr):
        self.number_served = nbr

    def increment_number_served(self, nbr):
        self.number_served += nbr


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, flavor, number_served=0):
        super().__init__(name, cuisine, number_served)
        self.flavor = flavor

    def flavors(self):
        print(*self.flavor)


if __name__ == '__main__':
    ice = IceCreamStand("Ice", "gelato", ["Vanilla", "Chocolate", "Strawberry"])
    ice.flavors()