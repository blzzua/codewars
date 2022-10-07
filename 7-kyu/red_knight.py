# https://www.codewars.com/kata/5fc4349ddb878a0017838d0f

def red_knight(N, P):
    col = 'White' if P % 2 == N else 'Black'
    pos = P*2
    return col, pos

