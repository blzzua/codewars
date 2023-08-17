# https://www.codewars.com/kata/6347f9715467f0001b434936

from math import sqrt

def thin_or_fat(matrix):
    try:
        t = sum(sqrt(i) for i in [sum(matrix[i][j] for j in range(len(matrix))) for i in range(len(matrix))])
        f = sum(sqrt(i) for i in [sum(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix))])
    except ValueError as e:
        return None
    return {t == f: 'perfect', t < f: 'thin', t > f: 'fat'}[True]
