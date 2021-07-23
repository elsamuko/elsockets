import unittest
import elsockets.utils

class TestUtils(unittest.TestCase):
    def test_utils(self):
        self.assertEqual(elsockets.utils.hello(), "hello")
