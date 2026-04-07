import unittest
import main

class TestA1(unittest.TestCase):
    def test_first(self):
        result = main.hello("Bob")
        self.assertEqual(result, "Hello Bob!")
