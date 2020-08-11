"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""


class Restaurant:

    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open.")


if __name__ == '__main__':
    r1 = Restaurant("Trattoria", "Italian")
    r2 = Restaurant("Jade Dragon", "Chinese")
    r3 = Restaurant("Chez Bily", "Snack")

    r1.describe_restaurant()
    r2.describe_restaurant()
    r3.describe_restaurant()
