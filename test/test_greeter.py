import unittest
from src.greeter import greet

class TestGreet(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
        
    def test_greet_takes_name_and_returns_hello_name(self):
        self.assertEqual(greet("Mohamed"), "Hello, Mohamed!")
