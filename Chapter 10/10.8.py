"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block
executes properly.
"""

if __name__ == '__main__':
    try:
        with open("cat.txt", "r") as fcats:  # cat -> cats
            cats = fcats.readlines()
        with open("dogs.txt", "r") as fdogs:
            dogs = fdogs.readlines()
    except:
        print("There has been an issue with the files.")
    else:
        print("".join(map(str, cats)), sep="\n")
        print("".join(map(str, dogs)), sep="\n")