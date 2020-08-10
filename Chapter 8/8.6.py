"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
"""
if __name__ == '__main__':
    def city_country(name, country):
        return name + ", " + country
    print(city_country("Paris", "France"), city_country("Brussels", "Belgium"), city_country("Berlin", "Germany"),
          sep='\n')
