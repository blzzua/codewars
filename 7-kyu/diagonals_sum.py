# https://www.codewars.com/kata/5592fc599a7f40adac0000a8

def sum_diagonals(matrix):
    n = len(matrix[0])
    if n == 0:
        return 0
    if n == 1:
        return 2*matrix[0][0]
    return sum(matrix[i][j] + matrix[i][n-j-1]  for i, j in zip(range(n), range(n))) 
