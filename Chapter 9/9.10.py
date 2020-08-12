"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working
properly.
"""

from src import Restaurant

if __name__ == '__main__':
    r1 = Restaurant("Leonidas", "Greek")
    r1.describe_restaurant()
