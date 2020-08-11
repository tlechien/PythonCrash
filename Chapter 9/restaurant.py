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