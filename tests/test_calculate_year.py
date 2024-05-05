import unittest
from src.calculate_year import calculate_year_turns_100
from datetime import datetime

class TestCalculateYear(unittest.TestCase):
    def test_calculate_year_turns_100_positive_age(self):
        """
        Test that calculate_year_turns_100 correctly calculates the year someone turns 100 for positive ages.
        """
        current_year = datetime.now().year
        self.assertEqual(calculate_year_turns_100(25), current_year + 75)

    def test_calculate_year_turns_100_zero_age(self):
        """
        Test that calculate_year_turns_100 handles an age of zero correctly.
        """
        current_year = datetime.now().year
        self.assertEqual(calculate_year_turns_100(0), current_year + 100)

    def test_calculate_year_turns_100_negative_age(self):
        """
        Test that calculate_year_turns_100 raises a ValueError when given a negative age.
        """
        with self.assertRaises(ValueError):
            calculate_year_turns_100(-1)

if __name__ == '__main__':
    unittest.main()
