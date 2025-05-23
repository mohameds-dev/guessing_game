from src.character_guess_validator import validate_guess
from src.character_score_calculator import calculate_score

def evaluate_score(correct_word, guessed_word):
    score = 0
    for correct_char, guessed_char in zip(correct_word, guessed_word):
        if not validate_guess(correct_char, guessed_char): break
        score += calculate_score(correct_char)

    return score
