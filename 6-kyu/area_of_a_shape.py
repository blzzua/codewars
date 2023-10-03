# https://www.codewars.com/kata/5474be18b2bc28ff92000fbd

import numpy as np
def area_of_the_shape(f):
    cnt = 500
    step = 1/cnt
    X, Y = np.mgrid[-1:1+step:step, 0:1+step:step]
    res = sum([int(f(x,y)) for x,y in np.vstack((X.flatten(), Y.flatten())).T])/(cnt+1)/(cnt+1)
    return res

# best practics via np:
def area_of_the_shape(f):
    cnt = 500
    xy, step = np.linspace(0., 1., 100, endpoint=False, retstep=True)
    X, Y = np.meshgrid(xy + step/2, xy + step/2)
    values = np.vectorize(f)(X, Y)
    return np.mean(values)
