import unittest
from city_country import get_formatted_city_country


class CityCountryTestCase(unittest.TestCase):
    """Test case for city_country.py"""

    def test_city_country(self):
        """Does a city, country like Santiago, Chile work?"""
        city_country = get_formatted_city_country("santiago", "chile")
        self.assertEqual(city_country, "Santiago, Chile")

    def test_city_country_population(self):
        """Does a city, country and population like Santiago, Chile - population 500000 work?"""
        city_country = get_formatted_city_country("santiago", "chile", "5000000")
        self.assertEqual(city_country, "Santiago, Chile - Population 5000000")


if __name__ == "__main__":
    unittest.main()
