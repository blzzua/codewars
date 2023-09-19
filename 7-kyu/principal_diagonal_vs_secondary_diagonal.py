# https://www.codewars.com/kata/5a8c1b06fd5777d4c00000dd

def diagonal(matrix):
    p, s = 0, 0
    for i in range(len(matrix)):
        p+= matrix[i][i]
        s+= matrix[i][-(i+1)]
    if p == s:
        return 'Draw!'
    return  'Principal Diagonal win!' if p > s else 'Secondary Diagonal win!' 
