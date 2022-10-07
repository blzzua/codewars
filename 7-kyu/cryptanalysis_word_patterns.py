# https://www.codewars.com/kata/5f3142b3a28d9b002ef58f5e

def word_pattern(word):
    word = word.lower()
    d = {}
    i = 0
    for c in word:
        if not c in d:
            d[c] = i
            i = i + 1
    return '.'.join([f'{d[c]}' for c in word])

