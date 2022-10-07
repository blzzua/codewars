# https://www.codewars.com/kata/54d22119beeaaaf663000024

def shades_of_grey(n):
    n = min(max(n, 0), 254)
    return ['#{0}{0}{0}'.format(hex(i)[2:].zfill(2)) for i in range(1,-~n)]
 

