import unittest
from io import StringIO
from unittest.mock import patch
import main  # Make sure to import the main file that contains the core code


class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', return_value='Ana')  # Simulates user input (name is 'Ana')
    @patch('sys.stdout', new_callable=StringIO)  # Captures the program's output
    def test_greeting(self, mock_stdout, mock_input):
        # Executes the main function
        main.main()

        # Verifies if the output is as expected
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, 'Hello, Ana')  # We expect the greeting to be 'Hello, Ana'

    @patch('builtins.input', return_value='')  # Simulates an empty input
    @patch('sys.stdout', new_callable=StringIO)  # Captures the output
    def test_empty_input(self, mock_stdout, mock_input):
        # Executes the main function
        main.main()

        # Verifies if the output is as expected with empty input
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, 'Hello,')  # We expect a generic or empty greeting


if __name__ == '__main__':
    unittest.main()
