"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.
"""
if __name__ == '__main__':
    favorite_places = {
        "Matthias": "Paris",
        "Albert": "Rio",
        "Eric": "Rome"
    }

    print(*map(lambda x: "\n{} likes {}".format(x, favorite_places[x]), favorite_places))
