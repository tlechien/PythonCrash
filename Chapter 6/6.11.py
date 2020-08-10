"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.
"""
if __name__ == '__main__':
    cities = {
        "Paris" : {"country": "France", "population": 52, "fact": "baguette"},
        "Rio": {"country": "Bresil", "population": 170, "fact": "They got Jesus"},
        "Rome": {"country": "Italy", "population": 35, "fact": "Pretty nice"},
    }

    print(*map(lambda x: "\n{} in {} with {} residents. {}!".format(x , *list(cities[x].values())), cities))