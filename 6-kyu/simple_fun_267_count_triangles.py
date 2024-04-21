# https://www.codewars.com/kata/5913ffb2cb1475215c000039

def count_triangles(n):
    if n % 2:
        return (12*n**3 + 18*n**2 +4*n -2) /4
    else:
        return (12*n**3 + 18*n**2 +4*n) /4
