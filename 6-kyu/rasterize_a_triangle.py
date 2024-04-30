# https://www.codewars.com/kata/621ab012ed37430016df15c0

import numpy as np

def point_in_triangle (v, v1, v2, v3):
    d1 = (v[0] - v2[0]) * (v1[1] - v2[1]) - (v1[0] - v2[0]) * (v[1] - v2[1]) # d1 = np.cross(v2 - v1, v - v2)
    d2 = (v[0] - v3[0]) * (v2[1] - v3[1]) - (v2[0] - v3[0]) * (v[1] - v3[1]) # d2 = np.cross(v3 - v2, v - v3)
    d3 = (v[0] - v1[0]) * (v3[1] - v1[1]) - (v3[0] - v1[0]) * (v[1] - v1[1]) # d3 = np.cross(v1 - v3, v - v1)
    return (d1 >= 0 and d2 >= 0 and d3 >= 0) or (d1 <= 0 and d2 <= 0 and d3 <= 0)

def draw_triangle(triangle, n):
    (x1, y1), (x2, y2), (x3, y3) = triangle
    a = np.ndarray((n, n), dtype=int) 
    for x, y in np.ndindex(a.shape):
        a[y, x] = point_in_triangle ((x, y), (x1, y1), (x2, y2), (x3, y3))
    return a.tolist()
  

# works but timing:
import numpy as np
def point_in_triangle (v, triangle):
    v, v1, v2, v3 =  map(np.array, [v] + triangle)
    d1 = np.cross(v2 - v1, v - v2)
    d2 = np.cross(v3 - v2, v - v3)
    d3 = np.cross(v1 - v3, v - v1)
    return (d1 >= 0 and d2 >= 0 and d3 >= 0) or (d1 <= 0 and d2 <= 0 and d3 <= 0)
def draw_triangle(triangle, n):
    (x1, y1), (x2, y2), (x3, y3) = triangle
    a = np.zeros((n, n), dtype=int) 
    for x,y in np.ndindex(a.shape):
        a[y,x] = point_in_triangle ((x,y), triangle)
    return a.tolist()

