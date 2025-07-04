# https://www.codewars.com/kata/54c14c1b86b33df1ff000026

def int_to_negabinary(i):
    res = []
    while i :
        i , r = divmod(i, -2)
        if r < 0 :
            i, r = i + 1, r + 2 
        res.append(r)
    return  ''.join(map(str, res[::-1])) or '0'
    
def negabinary_to_int(s):
    return sum(int(b) * (-2) ** i  for i, b in enumerate(s[::-1]))


# clever: https://stackoverflow.com/questions/37637781/calculating-the-negabinary-representation-of-a-given-number-without-loops/37643731#37643731
def int_to_negabinary(i):
    return '{:b}'.format((0xAAAAAAAA + i) ^ 0xAAAAAAAA)

def negabinary_to_int(n):
    return (int(n, 2) ^ 0xAAAAAAAA) - 0xAAAAAAAA
