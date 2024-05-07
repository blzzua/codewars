# https://www.codewars.com/kata/57aae4facf1fa57b3300005d

def four_piles(n,y):
    x = (y*n)/((y+1)**2)
    if y >= x or int(x)!=x:
        return []
    return [x+y, x-y, x*y, x//y]
