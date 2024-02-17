# test_hello.py

import hello
import io
import sys
import unittest

class TestHello(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to a StringIO object
        self.stdout = io.StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        # Restore original stdout
        sys.stdout = sys.__stdout__

    def test_hello_world(self):
        # Call the main function
        hello.main()

        # Get the printed output
        output = self.stdout.getvalue().strip()

        # Assert that the output is "Hello, world!"
        self.assertEqual(output, "Hello, world!")

if __name__ == '__main__':
    unittest.main()
