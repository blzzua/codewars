# https://www.codewars.com/kata/58870402c81516bbdb000088

from collections import Counter
def strings_construction(a, b):
    ac = Counter(a)
    bc = Counter(b)
    return min(bc.get(letter, 0) // ac.get(letter) for letter in ac)
