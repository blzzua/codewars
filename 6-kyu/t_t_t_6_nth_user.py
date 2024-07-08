# https://www.codewars.com/kata/5768b217b8ed4a77c0000c46

def user_number(n):
    # from decimal to octal with special alphabet
    res = ''
    al = '01235678'
    while n > 0:
        n, rem = divmod(n, 8)
        res = al[rem] + res
    return res or '0'
  
