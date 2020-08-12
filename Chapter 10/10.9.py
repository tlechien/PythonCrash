"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
"""

if __name__ == '__main__':
    try:
        with open("cat.txt", "r") as fcats:  # cat -> cats
            cats = fcats.readlines()
        with open("dogs.txt", "r") as fdogs:
            dogs = fdogs.readlines()
    except: pass
    else:
        print("".join(map(str, cats)), sep="\n")
        print("".join(map(str, dogs)), sep="\n")
