import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Janis Japlin' work?"""
        formatted_name = get_formatted_name('Janis', 'Japlin')
        self.assertEqual(formatted_name, 'Janis Japlin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('Wolfgang', 'Mozart', 'Amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
