# https://www.codewars.com/kata/5a74d00c0025e979c9000145

def getVertex(a,b,c):
    h = (-1 * b ) / (2 * a)
    k = ( c - ( h ** 2) * a  ) 
    return [h, k]
