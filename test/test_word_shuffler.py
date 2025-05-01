import unittest
from src.word_shuffler import shuffle_word
from unittest.mock import patch

class TestWordShuffler(unittest.TestCase):
    @patch('src.word_shuffler.sample')
    def test_shuffle_word_takes_donkey_and_returns_it_shuffled(self, mock_sample):
        mock_sample.side_effect = lambda iterable, len: list(reversed(iterable))

        self.assertEqual(shuffle_word("donkey"), "yeknod")
        mock_sample.assert_called_once_with(list("donkey"), 6)


    @patch('src.word_shuffler.sample')
    def test_shuffle_word_takes_monkey_and_returns_it_shuffled(self, mock_sample):
        mock_sample.side_effect = lambda iterable, len: list(reversed(iterable))

        self.assertEqual(shuffle_word("monkey"), "yeknom")
        mock_sample.assert_called_once_with(list("monkey"), 6)

