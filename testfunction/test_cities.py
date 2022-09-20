import unittest
from city_functions import City_Country


class City_Country_test(unittest.TestCase):
    def test_City_Country(self):
        cc = City_Country('guangzhou','china')
        self.assertEqual(cc,'Guangzhou,China')

if __name__ == 'main':
    unittest.main()