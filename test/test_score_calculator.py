import unittest
from src.score_calculator import calculate

class TestScoreCalculator(unittest.TestCase):        
    def test_score_calculator_takes_x_and_returns_2(self):
        self.assertEqual(calculate('x'), 2)

    def test_score_calculator_takes_a_and_returns_1(self):
        self.assertEqual(calculate('a'), 1)
    
    def test_score_calculator_takes_i_and_returns_1(self):
        self.assertEqual(calculate('i'), 1)
