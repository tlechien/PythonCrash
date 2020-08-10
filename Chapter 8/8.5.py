"""
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""
if __name__ == '__main__':
    def describe_city(name, country="Za Warudo"):
        print("{} is in {}.".format(name, country))
    describe_city("Paris")
    describe_city("Paris", "France")