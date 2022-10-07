# https://www.codewars.com/kata/551204b7509063d9ba000b45

from math import prod
def main_diagonal_product(mat):
    return prod(m[i] for i, m in enumerate(mat))


