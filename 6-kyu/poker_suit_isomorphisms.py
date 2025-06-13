# https://www.codewars.com/kata/6847f6ebe89e0623fb5aa2c0

from itertools import permutations

def tokenize(suit_map, s):
    return sorted([('23456789TJQKA'.index(rank) , suit_map.index(suit)) for rank, suit  in zip(s[::2],s[1::2])])

def boards_isomorphic(s1, s2):
    suit_map_init = ('d', 'h', 'c', 's')
    variation1 = tokenize(suit_map_init, s1)
    for suit_map in permutations(suit_map_init):
        variation2  = tokenize(suit_map, s2)
        if variation2 == variation1:
            return True
    return False

