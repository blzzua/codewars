# https://www.codewars.com/kata/5635e7cb49adc7b54500001c

def solve(n):
    res = 0
    for banknote in [500,200,100,50,20,10]:
        cnt, n =divmod(n, banknote)
        res = res + cnt
    if n > 0: 
        return -1
    else:
        return res

