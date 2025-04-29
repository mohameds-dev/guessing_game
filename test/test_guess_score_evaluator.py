import unittest
from src.guess_score_evaluator import evaluate_score


class TestScoreEvaluator(unittest.TestCase):
    def test_guess_evaluator_takes_monkey_and_monkey_and_returns_10(self):
        return self.assertEqual(evaluate_score("monkey", "monkey"), 10)
    
    def test_guess_evaluator_takes_monkey_and_monk_and_returns_7(self):
        return self.assertEqual(evaluate_score("monkey", "monk"), 7)
    
    def test_guess_evaluator_takes_monkey_and_kom_and_returns_0(self):
        return self.assertEqual(evaluate_score("monkey", "kom"), 0)

    def test_guess_evaluator_takes_monkey_and_kom_and_returns_0(self):
        return self.assertEqual(evaluate_score("monkey", "mono"), 5)
