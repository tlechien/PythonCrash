if __name__ == '__main__':
    users = ['Paul', 'Pierre', 'Denis', 'Trey', 'admin']

    for user in users:
        print("Hello God." if user == "admin" else "Hello %s."%user)