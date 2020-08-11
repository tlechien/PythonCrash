"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""
if __name__ == '__main__':
    def make_album(artist_name, album_title, count=None):
        album = {
            'artist_name': artist_name,
            "album_title": album_title
        }
        if count:
            album.update({"count": count})
        return album
    name = "placeholder"
    while name:
        name = input("What is the name of the artist? (leave empty to exit) ")
        if name:
            title = input("What's the title of the album? ")
            print(f"\n{make_album(name, title)}\n")
