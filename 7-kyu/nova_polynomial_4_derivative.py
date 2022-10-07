# https://www.codewars.com/kata/571a2e2df24bdfd4e20001f5

def poly_derivative(p):
    return [c*p for c, p in enumerate(p[1:],1)]

