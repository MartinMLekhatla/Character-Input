import unittest
from unittest.mock import patch
from src.user_input import accept_user_name, accept_user_age
from io import StringIO
import sys

class TestUserInput(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    @patch('builtins.input', return_value='John')
    def test_accept_user_name_valid_input(self, mock_input):
        """
        Test that accept_user_name returns a properly capitalized name when provided a valid name.
        """
        self.assertEqual(accept_user_name(), 'John')

    @patch('builtins.input', side_effect=['-1', 'twenty', '', '30'])
    def test_accept_user_age_valid_input(self, mock_input):
        """
        Test that accept_user_age returns a valid age after multiple invalid attempts.
        """
        self.assertEqual(accept_user_age(), 30)

    def tearDown(self):
        sys.stdout = self.held    

if __name__ == '__main__':
    unittest.main()
