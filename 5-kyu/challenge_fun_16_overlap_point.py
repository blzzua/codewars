# https://www.codewars.com/kata/58b3c7b9917a5cb4aa0000c5

import numpy as np
def too_slow_overlap_point(c1, c2):
    x_min = min((c1[0]-c1[2], c2[0]-c2[2]))
    x_max = max((c1[0]+c1[2], c2[0]+c2[2]))
    x_len = x_max - x_min+1

    y_min = min((c1[1]-c1[2], c2[1]-c2[2]))
    y_max = max((c1[1]+c1[2], c2[1]+c2[2]))
    y_len = y_max - y_min+1
    
    A = np.zeros( (y_len, x_len), dtype=np.int8 )
    for iy, ix in np.ndindex(A.shape):
        A[iy, ix] += (ix + x_min - c1[0])**2 + (iy + y_min - c1[1])**2 <= c1[2]**2
        A[iy, ix] += (ix + x_min - c2[0])**2 + (iy + y_min - c2[1])**2 <= c2[2]**2
    #from matplotlib import pyplot as plt
    #plt.imshow(A, interpolation='nearest')
    #plt.show()
    return len(A[A==2])

def overlap_point(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    min_y = max(y1 - r1, y2 - r2)
    max_y = min(y1 + r1, y2 + r2)
    res = 0
    for y in range(min_y, max_y + 1):
        if r1**2 >= (y - y1)**2:
            line_dist = np.sqrt(r1**2 - (y - y1)**2)
            x1_min = x1 - line_dist
            x1_max = x1 + line_dist
        else:
            x1_min = x1
            x1_max = x2

        if r2**2 >= (y - y2)**2:
            line_dist = np.sqrt(r2**2 - (y - y2)**2)
            x2_min = x2 - line_dist
            x2_max = x2 + line_dist
        else:
            x2_min = x2
            x2_max = x2

        x_min = max(x1_min, x2_min)
        x_max = min(x1_max, x2_max)
        if x_min <= x_max:
            res += np.floor(x_max) - np.ceil(x_min) + 1
    
    return res

