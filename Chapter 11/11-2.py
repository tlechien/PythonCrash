"""
11-2. Population: Modify your function so it requires a third parameter,
population. It should now return a single string of the form City, Country –
population xxx, such as Santiago, Chile – population 5000000. Run test
_cities.py again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run test
_cities.py again, and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that verifies
you can call your function with the values 'santiago', 'chile', and
'population=5000000'. Run test_cities.py again, and make sure this new test
passes.
"""
import unittest


def city_country(name, country, population):
    return name + ", " + country + " - population " + str(population)


def city_country2(name, country, population=500000):
    return name + ", " + country + " - population " + str(population)


class TestCityCountry(unittest.TestCase):
    def test_string(self):
        a_output = city_country("Santiago", "Chile", 500000)
        self.assertEqual(a_output, "Santiago, Chile")

    def test_string2(self, ):
        b_output = city_country2("Santiago", "Chile")
        self.assertEqual(b_output, "Santiago, Chile - population 500000")

    def test_optional(self):
        c_output = city_country2("Santiago", "Chile", population=500000)
        self.assertEqual(c_output, "Santiago, Chile - population 500000")


if __name__ == '__main__':
    unittest.main()
