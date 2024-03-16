import unittest
from unittest.mock import patch

import functions


class MyTestCase(unittest.TestCase):
    @patch('builtins.input', return_value='martin')
    def test_get_user_name(self, _):
        self.assertEqual(functions.accept_users_name(), "Martin")

    @patch('builtins.input', return_value='25')
    def test_get_user_age_valid_input_type(self, _):
        self.assertIsInstance(functions.accept_users_age(), int)

    @patch('builtins.input', return_value='')
    def test_get_user_age_empty_input(self, _):
        self.assertIsNone(functions.accept_users_age())

    @patch('builtins.input', return_value='25')
    def test_get_user_age_valid_input(self, _):
        self.assertEqual(functions.accept_users_age(), 25)

    @patch('builtins.input', return_value='not_an_age')
    def test_get_user_age_invalid_input(self, _):
        self.assertIsNone(functions.accept_users_age())


if __name__ == '__main__':
    unittest.main()
