from random import sample

def scramble_word(word):
    return ''.join(sample(list(word), len(word)))
