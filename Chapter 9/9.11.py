"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
"""

from src import Admin

if __name__ == '__main__':
    Admin("Neo", "The chosen one", ["controls the matrix"]).privileges.show_privileges()
