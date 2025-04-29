from random import choice

def select_word(words):
    try:
        return choice(words)
    except IndexError:
        raise IndexError("Invalid input: expected a non-empty list of words to select from.")