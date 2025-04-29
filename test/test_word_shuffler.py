import unittest
from src.word_shuffler import shuffle_word
from unittest.mock import patch

class TestWordShuffler(unittest.TestCase):
    @patch('random.shuffle')
    def test_shuffle_word_takes_donkey_and_returns_it_shuffled(self, mock_shuffle):
        mock_shuffle.side_effect = lambda word: word.reverse()

        self.assertEqual(shuffle_word("donkey"), "yeknod")

    @patch('random.shuffle')
    def test_shuffle_word_takes_monkey_and_returns_it_shuffled(self, mock_shuffle):
        mock_shuffle.side_effect = lambda word: word.reverse()

        self.assertEqual(shuffle_word("monkey"), "yeknom")