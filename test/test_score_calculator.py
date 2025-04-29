import unittest
from src.score_calculator import calculate
from parameterized import parameterized

class TestScoreCalculator(unittest.TestCase):  

    @parameterized.expand(['x', 'y', 'z'])
    def test_score_calculator_takes_consonant_and_returns_2(self, consonant):
        self.assertEqual(calculate(consonant), 2)

    @parameterized.expand(['a', 'e', 'i', 'o', 'u'])
    def test_score_calculator_takes_vowel_and_returns_1(self, consonant):
        self.assertEqual(calculate(consonant), 1)
