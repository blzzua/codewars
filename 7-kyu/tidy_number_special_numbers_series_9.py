# https://www.codewars.com/kata/5a87449ab1710171300000fd

def tidyNumber(n):
    s = ''.join(sorted([*str(n)]))
    return n == int(s)

