# https://www.codewars.com/kata/59c62f1bdcc40560a2000060

def solve(a):
    even, odd = 0, 0
    for i in a:
        if isinstance(i , int):
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return even - odd
