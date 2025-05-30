# https://www.codewars.com/kata/57630df805fea67b290009a3

from string  import ascii_lowercase as al
def permutation_position(perm):
    res = 1
    for i, c in enumerate(perm[::-1]):
        res += 26**i * al.index(c)
    return res
