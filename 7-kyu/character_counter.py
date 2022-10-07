# https://www.codewars.com/kata/56786a687e9a88d1cf00005d

from collections import Counter
def validate_word(word):
    return len(set(Counter(word.lower()).values())) < 2

