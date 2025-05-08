# https://www.codewars.com/kata/58ad29bc4b852b14a4000050

from itertools import combinations
def counting_triangles(V):
    SV = sorted(V)
    return sum([1 for a,b,c in combinations(SV,3) if a + b > c])

