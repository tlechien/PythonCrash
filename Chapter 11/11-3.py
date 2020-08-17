"""
11-3. Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.
Write a test case for Employee. Write two test methods, test_give_default
_raise() and test_give_custom_raise(). Use the setUp() method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass.
"""
import unittest


class Employee:
    def __init__(self, f_name, l_name, a_salary):
        self.f_name = f_name
        self.l_name = l_name
        self.a_salary = a_salary

    def give_raise(self, amount=5000):
        self.a_salary += amount


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Mary", "Shelley", 0)

    def test_give_default(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.a_salary, 5000)

    def test_give_custom_raise(self):
        self.employee.give_raise(9999)
        self.assertEqual(self.employee.a_salary, 9999)


if __name__ == '__main__':
    unittest.main()
