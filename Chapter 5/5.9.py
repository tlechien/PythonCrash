if __name__ == '__main__':
    users = ['Paul', 'Pierre', 'Denis', 'Trey', 'admin']

    users = []

    if users:
        for user in users:
            print("Hello God." if user == "admin" else "Hello %s."%user)
    else:
        print("We need to find some users!")