# https://www.codewars.com/kata/577b9960df78c19bca00007e

def find_digit(num, nth):
    if nth <= 0:
        return -1
    num = str(abs(num))
    if nth > len(num):
        return 0
    return int(num[-nth])

