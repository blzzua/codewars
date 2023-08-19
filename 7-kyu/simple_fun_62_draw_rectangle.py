# https://www.codewars.com/kata/5889ae4f7af7f99a9a000019

import numpy as np
def draw_rectangle(canvas, rectangle):
    x1,y1,x2,y2 = rectangle
    A = np.array(canvas)
    for x in range(x1+1,x2):
        A[y1,x] = '-'
        A[y2,x] = '-'
    for y in range(y1+1,y2):
        A[y,x1] = '|'
        A[y,x2] = '|'
    A[y1,x1] = '*'
    A[y2,x1] = '*'
    A[y1,x2] = '*'
    A[y2,x2] = '*'
    return A.tolist()
