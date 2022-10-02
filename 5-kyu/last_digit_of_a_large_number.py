# https://www.codewars.com/kata/5511b2f550906349a70004e1

def last_digit(n1, n2):
    if n2 == 0:
        return 1
    ld_map = {2: [2,4,8,6], 3: [3,9,7,1], 4: [4,6,4,6], 7: [7,9,3,1], 8: [8,4,2,6], 9: [9,1,9,1]}
    if n1 % 10 in (0,1,5,6):
        return n1 % 10 
    return ld_map[n1 % 10][n2 % 4 - 1]
