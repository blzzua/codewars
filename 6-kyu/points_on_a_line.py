# https://www.codewars.com/kata/53b7bc844db8fde50800020a

import numpy as np

EPSILON = 10**-10

def on_line(points):
    if len(points) < 3:
        #0 - no points, 1 - single point, 2 - 2 points always on line.
        return True
    A = np.array(points)
    norm_vectors = [np.abs(a-b)/np.linalg.norm((a-b)) for a,b in zip(A, np.concatenate((A[1:], A[:1]))) if np.linalg.norm((a-b)) >0]
    if len(norm_vectors) < 2:
        #0 - no points, 1 - single point.
        return True
    #if any( all(v1 != v2) for v1,v2 in zip(norm_vectors[1:], norm_vectors)):
    if any(np.abs(np.linalg.norm(v1 - v2)) > EPSILON for v1,v2 in zip(norm_vectors[1:], norm_vectors)):
        return False
    return True

# clever solution was that cross_product of vectors is equal 0
# cross_product = lambda a, b, c: a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])
