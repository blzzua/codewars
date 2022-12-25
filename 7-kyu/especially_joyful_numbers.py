# https://www.codewars.com/kata/570523c146edc287a50014b1

def number_joy(n):
    dig_sum = sum(map(int,str(n)))
    if dig_sum * int(str(dig_sum)[::-1]) == n:
        return True
    else:
        return False
