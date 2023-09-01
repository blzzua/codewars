# https://www.codewars.com/kata/52f3eeb274c7e693a600288e

def insert_at_indexes(phrase, word, indexes): 
    _is_zero=False
    if 0 in indexes:
        indexes = indexes[1:]
        _is_zero=True
    phrase=phrase[::-1]
    for i in indexes[::-1]: 
        phrase = phrase[:-i] + word[::-1] + phrase[-i:]
    if _is_zero:
        phrase = phrase + word[::-1]
    return phrase[::-1]
