# https://www.codewars.com/kata/58b03e48a965cb194f0002bd

def gradient(c1, c2):
    # the color is represented with a tuple: (r, g, b)
    def internal(grad):
         return  tuple((grad* comp2 + (100-grad)*comp1)//100 for comp1, comp2 in zip(c1, c2))
    return internal
