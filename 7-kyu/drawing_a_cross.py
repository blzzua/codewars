# https://www.codewars.com/kata/5a036ecb2b651d696f00007c

# main diag where i==j, opposite diag where n-j == i+1

def draw_a_cross(n):
    if n < 3:
        return 'Not possible to draw cross for grids less than 3x3!'
    if n % 2 == 0:
        return 'Centered cross not possible!'
    return '\n'.join(''.join('x' if i == j or n-j == i+1 else ' ' for j in range(n)) for i in range(n))
