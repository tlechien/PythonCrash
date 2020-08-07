if __name__ == '__main__':
    users = ['Paul', 'Pierre', 'Denis', 'Trey', 'admin']

    users = []

    for user in users:
        print("Hello God." if user == "admin" else "Hello %s."%user)
    if not users:
        print("We need to find some users!")