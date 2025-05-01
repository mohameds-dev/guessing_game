from src.input_reader import read_input_words
# from src.random_word_selector import select_word
from src.random_index_generator import random_index, next_index
from src.word_scrambler import scramble_word
from src.guess_score_evaluator import evaluate_score

def run_game():
    words = read_input_words()
    word_index = random_index(len(words))
    while True:
        word = words[word_index]
        scrambled_word = scramble_word(word)

        print(f"Guess the word: {scrambled_word}")
        
        user_guess = input("Your guess: ")
        perfect_score = evaluate_score(word, word)
        score = evaluate_score(user_guess, word)

        print(f"Your score: {score}/{perfect_score}")
        if score == perfect_score:
            print("Congratulations! You guessed the word correctly.")
            break
        print("Try again!")
        word_index = next_index(word_index, len(words))

if __name__ == "__main__":  
    run_game()

