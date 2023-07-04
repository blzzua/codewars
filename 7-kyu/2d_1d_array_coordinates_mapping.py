# https://www.codewars.com/kata/588dd9c3dc49de0bd400016d

def to_1D(x, y, size):
    return y * size[0] + x
    
def to_2D(n, size):
    return divmod(n, size[0])[::-1]
