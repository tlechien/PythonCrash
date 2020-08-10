"""
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
current_users containing the lowercase versions of all existing users.)
"""
if __name__ == '__main__':
    curr_users = ['Paul', 'Pierre', 'Denis', 'Trey', 'admin']
    new_user = ['Martin', 'Donatello', 'Raphael', 'Trey', 'Pierre']

    new_user += list(map(lambda x: x.upper(), curr_users))  # upper coz it's move visible
    print(new_user)

    for user in new_user:
        if user in curr_users:
            print("The username {} already exists. Please pick another one".format(user))
        else:
            print("The username {} is available".format(user))
