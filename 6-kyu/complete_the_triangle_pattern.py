# https://www.codewars.com/kata/58281843cea5349c9f000110

import numpy as np

def make_triangle(m,n):
    start, end, n = m, n, int(((8*(n - m + 1)+1)**(1/2)-1)/2)  # reverse triangualar number
    if n * (n+1) // 2 != (end - start + 1):
        return ''
    a = np.ndarray((n, 2 * n - 1),dtype=object)
    a[:] = ' '
    direction = 'down'
    cur_x = n-1
    cur_y = 0
    i = 1
    while i < sum(range(n+1)):
        a[cur_y, cur_x] = str((i+start-1)%10)
        if direction == 'down':
            cur_x  = cur_x + 1
            cur_y  = cur_y + 1
            if cur_y == n or a[cur_y, cur_x] != ' ':
                cur_y -= 1
                cur_x -= 1
                direction = 'left'
                continue
        if direction == 'left':
            cur_x  = cur_x - 2
            if cur_x < 0 or a[cur_y, cur_x] != ' ':
                cur_x  = cur_x + 2
                direction = 'up'
                continue
        if direction == 'up':
            cur_x  = cur_x + 1
            cur_y  = cur_y - 1
            if cur_x <= 0 or a[cur_y, cur_x] != ' ': 
                cur_x  = cur_x - 1
                cur_y  = cur_y + 1
                direction = 'down'
                continue
        i = i + 1
    a[cur_y, cur_x] = str((i+start-1)%10)
    return '\n'.join((''.join(line).rstrip() for line in  a.tolist()))
