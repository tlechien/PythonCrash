if __name__ == '__main__':
    animals = [
        "Cat",
        "Dog",
        "Raccoon"
    ]

    print(*animals)

    for animal in animals:
        print("A {} would make a great pet.".format(animal))

    print("\nAny of these animals would make a great pet!")