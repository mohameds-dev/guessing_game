import unittest
from src.word_shuffler import shuffle_word
from unittest.mock import patch

class TestWordShuffler(unittest.TestCase):
    @patch('src.word_shuffler.shuffle')
    def test_shuffle_word_takes_donkey_and_returns_it_shuffled(self, mock_shuffle):
        mock_shuffle.side_effect = lambda iterable: list(reversed(iterable))

        self.assertEqual(shuffle_word("donkey"), "yeknod")
        mock_shuffle.assert_called_once_with(list("donkey"))


    @patch('src.word_shuffler.shuffle')
    def test_shuffle_word_takes_monkey_and_returns_it_shuffled(self, mock_shuffle):
        mock_shuffle.side_effect = lambda iterable: list(reversed(iterable))

        self.assertEqual(shuffle_word("monkey"), "yeknom")
        mock_shuffle.assert_called_once_with(list("monkey"))

