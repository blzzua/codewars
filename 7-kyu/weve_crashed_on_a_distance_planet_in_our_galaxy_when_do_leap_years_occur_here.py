# https://www.codewars.com/kata/5af43416882143534300142c

def is_leap_year(d, y):
    return y % (1/(d-int(d))) == 0
    
# clever
def is_leap_year(d, y):
    return (d * y).is_integer()
