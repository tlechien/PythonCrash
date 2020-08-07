if __name__ == '__main__':
    curr_users = ['Paul', 'Pierre', 'Denis', 'Trey', 'admin']
    new_user = ['Martin', 'Donatello', 'Raphael', 'Trey', 'Pierre']

    new_user += list(map(lambda x: x.upper(), curr_users))
    print(new_user)

    for user in new_user:
        if user in curr_users:
            print("The username: {} already exists. Please pick another one".format(user))
        else:
            print("The username {} is available".format(user))
