# https://www.codewars.com/kata/5da995d583326300293ce4cb

import numpy as np
   
def map_vector(vector, circle1, circle2):
    vec1 = np.array(vector) - np.array(circle1)[:2] 
    c2 = np.array(circle2)[:2]
    r1 = circle1[2]
    r2 = circle2[2]
    result = c2 + (vec1 / r1 * r2)
    return result

