import unittest
from src.character_guess_validator import validate_guess

class TestCharacterGuessValidator(unittest.TestCase):
    def test_validator_takes_m_and_m_and_returns_true(self):
        self.assertTrue(validate_guess('m', 'm'))

    def test_validator_takes_M_and_m_and_returns_true(self):
        self.assertTrue(validate_guess('M', 'm')) 
 
    def test_validator_takes_x_and_y_and_returns_false(self):
        self.assertFalse(validate_guess('x', 'y'))
