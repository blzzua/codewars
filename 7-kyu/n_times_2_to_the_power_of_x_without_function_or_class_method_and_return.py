# https://www.codewars.com/kata/57b971f68f58135e840001cc

class C:
    def __init__(self):
        pass

C.__call__ = lambda self, n, x: n.__mul__(int(2).__pow__(x))
puzzle = C()

# clever from operator import lshift as puzzle
