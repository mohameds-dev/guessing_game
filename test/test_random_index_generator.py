import unittest
from src.random_index_generator import random_index, next_index
from unittest.mock import patch

class TestRandomIndexGenerator(unittest.TestCase):

    @patch('src.random_index_generator.randint', return_value=2)
    def test_random_index_takes_list_size_and_returns_number_within_bounds(self, mock_randint):
        self.assertEqual(random_index(10), 2)
        mock_randint.assert_called_once_with(0, 9)

    def test_next_index_takes_1_and_10_and_returns_2(self):
        self.assertEqual(next_index(1, 10), 2)

    def test_next_index_takes_9_and_10_and_returns_0(self):
        self.assertEqual(next_index(4, 10), 5)
    
    def test_next_index_takes_9_and_10_and_returns_0(self):
        self.assertEqual(next_index(9, 10), 0)