import unittest
from src.character_score_calculator import calculate_score
from parameterized import parameterized

class TestScoreCalculator(unittest.TestCase):  
    def test_canary(self):
        self.assertTrue(True)

    @parameterized.expand(['x', 'y', 'z'])
    def test_score_calculator_takes_consonant_and_returns_2(self, consonant):
        self.assertEqual(calculate_score(consonant), 2)

    @parameterized.expand(['a', 'e', 'i', 'o', 'u'])
    def test_score_calculator_takes_vowel_and_returns_1(self, consonant):
        self.assertEqual(calculate_score(consonant), 1)
