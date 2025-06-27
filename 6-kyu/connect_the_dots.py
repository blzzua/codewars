# https://www.codewars.com/kata/5d6a11ab2a1ef8001dd1e817
import numpy as np
from string import ascii_lowercase

def mkline(A, a_coord, b_coord):
    ay, ax = a_coord
    by, bx = b_coord
    if ay != by:
        dy = (by - ay)//abs(ay - by)
    else:
        dy = 0
    if ax != bx:
        dx = (bx - ax)//abs(ax - bx)
    else:
        dx = 0
    
    x, y = ax, ay
    while True:
        A[y,x] = '*'
        x = x+dx; y = y + dy
        if (x,y) == (bx, by):
            A[y,x] = '*'
            break


def connect_the_dots(paper):
    A = np.array([list(line) for line in paper.strip('\n').split('\n')], dtype=object)
    letters_coord = []
    for letter in list(ascii_lowercase):
        if (A == letter).any():
            where_letter = np.where(A == letter)
            if where_letter:
                letters_coord.append((where_letter[0][0],  where_letter[1][0]))
    for a,b in zip(letters_coord,letters_coord[1:]):
        mkline(A, a, b)
    return '\n'.join([''.join(line) for line in A.tolist()])+'\n'
