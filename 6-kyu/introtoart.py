# https://www.codewars.com/kata/5d7d05d070a6f60015c436d1

def get_w(n):
    if n < 2:
        return []
    canvas = [ [' '] * (n*4-3) for i in range(n)]
    for i in range(n):
        canvas[i][i] = '*'
        canvas[i][2*n-i-2] = '*'
        canvas[i][2*n+i-2] = '*'
        canvas[i][4*n-i-4] = '*'
    return [''.join(line) for line in canvas]

