import unittest
from src.input_reader import read_input_words
from unittest.mock import mock_open, patch

class TestInputReader(unittest.TestCase):
    def test_read_input_words_success(self):
        mock_data = "word1\nword2\nword3\n"
        with patch("builtins.open", mock_open(read_data=mock_data)):
            words = read_input_words()
            self.assertEqual(words, ["word1", "word2", "word3"])

    def test_read_input_reads_empty_file_and_propagates_IndexError(self):
        mock_data = ""
        with patch("builtins.open", mock_open(read_data=mock_data)):
            words = read_input_words()
            self.assertEqual(words, [])