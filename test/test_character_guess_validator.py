import unittest
from src.character_guess_validator import validate_guess

class TestCharacterGuessValidator(unittest.TestCase):
    def test_validator_takes_monkey_and_index_0_and_m_and_returns_true(self):
        self.assertTrue(validate_guess("monkey", 0, 'm'))

    def test_validator_takes_monkey_and_index_0_and_k_and_returns_false(self):
        self.assertFalse(validate_guess("monkey", 0, 'k'))  

    def test_validator_takes_monkey_and_index_5_and_y_and_returns_true(self):
        self.assertTrue(validate_guess("monkey", 5, 'y'))
