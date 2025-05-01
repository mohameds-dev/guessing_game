from src.input_reader import read_input_words
from src.random_word_selector import select_word
from word_scrambler import scramble_word
from src.guess_score_evaluator import evaluate_score

def run_game():
    words = read_input_words()
    word = select_word(words)
    scrambled_word = scramble_word(word)
    print(f"Guess the word: {scrambled_word}")
    user_guess = input("Your guess: ")
    perfect_score = evaluate_score(word, word)
    score = evaluate_score(user_guess, word)

    print(f"Your score: {score}/{perfect_score}")

if __name__ == "__main__":  
    run_game()

