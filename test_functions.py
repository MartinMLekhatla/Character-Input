import unittest
from unittest.mock import patch

import functions


class MyTestCase(unittest.TestCase):
    @patch('builtins.input', return_value='martin')
    def test_get_user_name_string(self, _):
        self.assertEqual("Martin", functions.accept_users_name())


if __name__ == '__main__':
    unittest.main()
