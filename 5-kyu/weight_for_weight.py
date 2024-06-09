# https://www.codewars.com/kata/55c6126177c9441a570000cc

def order_key(s):
    return (sum(map(int,s)), s)
               
def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=order_key))

