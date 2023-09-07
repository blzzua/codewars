# https://www.codewars.com/kata/5e81303e7bf0410025e01031

def is_not_right(a,b,c):
    a,b,c = sorted((a,b,c))
    return  a**2 + b**2 != c**2

def is_triangle(a,b,c):
    a,b,c = sorted((a,b,c))
    return  a + b > c

def side_len(a,b):
    return [c for c in range(1, a + b + 1) if is_triangle(a,b,c) and is_not_right(a,b,c)]

# math clever replacement is_triangle(): [c for c in range(abs(b-a)+1,a+b) if is_not_right(a,b,c)]
