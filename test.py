import unittest
from app import home_page


class HomePageMethodTest(unittest.TestCase):

    def test_hello_words(self):
        web_app_value = home_page()
        self.assertEqual(web_app_value, 'Hello World')