import unittest
from unittest.mock import patch

import functions


class MyTestCase(unittest.TestCase):
    @patch('builtins.input', return_value='martin')
    def test_get_user_name(self, _):
        self.assertEqual(functions.accept_users_name(), "Martin")


if __name__ == '__main__':
    unittest.main()
