# https://www.codewars.com/kata/64087fd72daf09000f60dc26

def cute_pattern(tiles):
    s = tiles.splitlines()
    for l1,l2 in zip(s, s[1:]):
        for a,b,c,d in zip(l1, l1[1:], l2, l2[1:]):
            if a == b == c == d:
                return False
    return True
