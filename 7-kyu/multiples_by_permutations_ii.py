# https://www.codewars.com/kata/5ba178be875de960a6000187

def find_lowest_int(k):
    lowest_int = 1
    while sorted(str(lowest_int * k)) != sorted(str(lowest_int * (k+1))):
        lowest_int += 1
    return lowest_int

