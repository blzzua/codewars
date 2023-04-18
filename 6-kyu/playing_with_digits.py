# https://www.codewars.com/kata/5552101f47fc5178b1000050

def dig_pow(n, p):
    s = 0
    for i, dig in enumerate(str(n) , p):
        dig = int(dig)
        s += dig ** i
    dv, rem = divmod(s,n)
    if rem == 0:
        return dv
    else:
        return -1
