import unittest
from src.random_word_selector import select_word
from unittest.mock import patch

class TestRandomWordSelector(unittest.TestCase):
    def test_random_word_selector_takes_a_list_with_one_string_and_returns_it(self):
        self.assertEqual(select_word(["monkey"]), "monkey")

    @patch("src.random_word_selector.choice", return_value='monkey')
    def test_random_word_selector_takes_a_list_with_two_strings_and_returns_random_one(self, mock_choice):
        words = ["monkey", "donkey"]
        
        self.assertEqual(select_word(words), "monkey")
        mock_choice.assert_called_once_with(words)

    def test_random_word_selector_takes_an_empty_list_and_raises_exception(self):
        self.assertRaisesRegex(IndexError, "Invalid input: expected a non-empty list of words to select from.", select_word, [])
