import os

def read_input_words():
    words_file_path = os.path.join(os.path.dirname(__file__), "../data/words.txt")
    with open(words_file_path, 'r') as file:
        words = [line.strip() for line in file]
    return words
