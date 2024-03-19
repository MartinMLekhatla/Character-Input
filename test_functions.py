import io
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

    def test_display_turns_100_message_valid_input(self):
        # Test for valid input
        age = 25
        name = "John"
        year_hundred = datetime.now().year
        expected_message = (f'Hello, {name}! You will turn 100 years old in the year {year_hundred} since you are '
                            f'currently {age}.')
        self.assertEqual(functions.display_turns_100_message(name, age, year_hundred), expected_message)

    def test_display_turns_100_message_invalid_age(self):
        # Test for invalid age input
        name = "Alice"
        age = -5
        year_hundred = datetime.now().year
        expected_message = "Invalid age input. Please enter a valid age."
        self.assertEqual(functions.display_turns_100_message(name, age, year_hundred), expected_message)

    @patch('functions.accept_users_name', return_value='Alice')
    @patch('functions.accept_users_age', return_value=25)
    @patch('functions.calculate_year_turns_100', return_value=2097)
    @patch('functions.display_turns_100_message', return_value="Hello, Alice! You will turn 100 years old in the year 2097 since you are currently 25.")
    def test_run_application(self, mock_display, mock_calculate, mock_age, mock_name):
        expected_output = "Hello, Alice! You will turn 100 years old in the year 2097 since you are currently 25.\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            functions.run_application()
            self.assertEqual(fake_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
