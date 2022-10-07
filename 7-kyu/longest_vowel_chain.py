# https://www.codewars.com/kata/59c5f4e9d751df43cf000035

from itertools import groupby
def solve(s):
    return max(len(''.join(g)) for i,g in groupby(s.translate(str.maketrans('aeiou','_____'))) if i == '_')

