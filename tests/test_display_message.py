import unittest
from src.display_message import display_turns_100_message

class TestDisplayMessage(unittest.TestCase):
    def test_display_turns_100_message_valid_input(self):
        """
        Test that display_turns_100_message returns the correct message for valid name, age, and year inputs.
        """
        message = display_turns_100_message('John', 25, 2098)
        expected_message = "Hello, John! You will turn 100 years old in the year 2098, since you are currently 25."
        self.assertEqual(message, expected_message)

if __name__ == '__main__':
    unittest.main()
