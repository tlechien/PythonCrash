"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.
"""
if __name__ == '__main__':

    def color_check(alien_color):
        if alien_color == "green":
            print("5 points.")
        elif alien_color == "orange":
            print("10 points.")
        else:
            print("15 points.")

    color_check("green")
    color_check("orange")
    color_check("red")
