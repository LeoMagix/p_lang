import unittest
from city_function import city_name

class CityTestCase(unittest.TestCase):
    """Run a test for 'city_function.py'."""

    def test_city_country(self):
        """Does 'Santiago, Chile'"""
        format_name = city_name('dubai', 'saudi arabia')
        self.assertEqual(format_name, 'Dubai, Saudi Arabia')

    def test_city_country_population(self):
        """Does 'Santiago, Chile -population 5000000' work?"""
        format_name = city_name('santiago', 'Chile', population='5000000')
        self.assertEqual(format_name, 'Santiago, Chile -population 5000000')

if __name__ == '__main__':
    unittest.main()
