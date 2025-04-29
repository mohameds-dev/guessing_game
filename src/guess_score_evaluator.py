from src.character_guess_validator import validate_guess
from src.score_calculator import calculate_score

def evaluate_score(correct_word, guessed_word):
    score = 0
    for i, (correct_char, guessed_char) in enumerate(zip(correct_word, guessed_word)):
        if not validate_guess(correct_word, i, guessed_char): break
        score += calculate_score(correct_char)

    return score
