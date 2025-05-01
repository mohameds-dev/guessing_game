from random import sample

def shuffle_word(word):
    return ''.join(sample(list(word), len(word)))
