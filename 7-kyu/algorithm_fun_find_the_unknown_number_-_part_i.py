# https://www.codewars.com/kata/59cdb2b3a25c8c6d56000005

def find_unknown_number(x,y,z):
    return next(filter(lambda i: ((i % 3 == x) and (i % 5 == y) and (i % 7 == z)), range(1,105+1)))

# clever math solution (x*70 + y*21 + z*15) % 105 or 105

