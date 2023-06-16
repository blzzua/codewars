# https://www.codewars.com/kata/588422ba4e8efb583d00007d

def late_ride(n):
    return sum(sum(divmod(i, 10)) for i in divmod(n, 60) )
