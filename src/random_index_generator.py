from random import randint

def random_index(list_size):
    return randint(0, list_size - 1)


def next_index(current_index, size):
    return (current_index + 1) % size
