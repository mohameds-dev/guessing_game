import random

def shuffle_word(word):
    chars = list(word)
    random.shuffle(chars)

    return ''.join(chars)