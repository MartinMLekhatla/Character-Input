import unittest
from datetime import datetime
from unittest.mock import patch

import functions


class MyTestCase(unittest.TestCase):
    @patch('builtins.input', return_value='martin')
    def test_get_user_name(self, _):
        self.assertEqual("Martin", functions.accept_users_name())

    @patch('builtins.input', return_value='25')
    def test_get_user_age_valid_input_type(self, _):
        self.assertIsInstance(functions.accept_users_age(), int)

    @patch('builtins.input', return_value='')
    def test_get_user_age_empty_input(self, _):
        self.assertIsNone(functions.accept_users_age())

    @patch('builtins.input', return_value='25')
    def test_get_user_age_valid_input(self, _):
        self.assertEqual(25, functions.accept_users_age())

    @patch('builtins.input', return_value='not_an_age')
    def test_get_user_age_invalid_input(self, _):
        self.assertIsNone(functions.accept_users_age())

    def test_calculate_year_turns_100(self):
        # Test for a user who is currently 25 years old
        current_age = 25
        expected_year = datetime.now().year + (100 - current_age)
        self.assertEqual(expected_year, functions.calculate_year_turns_100(current_age))

    def test_calculate_year_turns_100_newborn(self):
        # Test for a newborn (age 0)
        current_age = 0
        expected_year = datetime.now().year + 100
        self.assertEqual(expected_year, functions.calculate_year_turns_100(current_age))

    def test_calculate_year_turns_100_centenarian(self):
        # Test for a centenarian (age 100)
        current_age = 100
        expected_year = datetime.now().year
        self.assertEqual(expected_year, functions.calculate_year_turns_100(current_age))

    def test_calculate_year_turns_100_near_boundary(self):
        # Test for an age near the lower boundary (age 1)
        current_age_lower_boundary = 1
        expected_year = datetime.now().year + (100 - current_age_lower_boundary)
        self.assertEqual(expected_year, functions.calculate_year_turns_100(current_age_lower_boundary))

        # Test for an age near the upper boundary (age 99)
        current_age_upper_boundary = 99
        expected_year = datetime.now().year + (100 - current_age_upper_boundary)
        self.assertEqual(expected_year, functions.calculate_year_turns_100(current_age_upper_boundary))

    def test_calculate_year_turns_100_negative_age(self):
        # Test for a negative age
        current_age = -1
        self.assertIsNone(functions.calculate_year_turns_100(current_age))

    def test_calculate_year_turns_100_non_numeric_input(self):
        # Test for a non-numeric input
        current_age = 'abc'
        self.assertIsNone(functions.calculate_year_turns_100(current_age))


if __name__ == '__main__':
    unittest.main()
