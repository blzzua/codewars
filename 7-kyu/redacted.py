# https://www.codewars.com/kata/5b662d286d0db722bd000013

from itertools import zip_longest
def redacted(doc1, doc2): 
    for a,b in zip_longest(doc1, doc2):
        if a == 'X' and b == '\n':
            return False
        if a != 'X' and a != b:
            return False
    return True
