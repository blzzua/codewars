# https://www.codewars.com/kata/5650f1a6075b3284120000c0

def checkered_board(n):
    X = '□■'
    res = []
    for i in range(n):
        res.append(' '.join(X[((j + i + n) % 2) ] for j in range(n)))
    return '\n'.join(res)
