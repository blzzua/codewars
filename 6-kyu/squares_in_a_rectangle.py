# https://www.codewars.com/kata/5a62da60d39ec5d947000093

def find_squares(x,y):
    m, d = min(x,y), abs(x-y)
    return (m+1)*m * (3*d + 2*m + 1) // 6
    
# clever: sum( (x-i) * (y-i) for i in range(min(x,y)) )
