# https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f

def compute_sum(n):
    return sum(sum(map(int,i)) for i in map(str,range(1,-~n)))
