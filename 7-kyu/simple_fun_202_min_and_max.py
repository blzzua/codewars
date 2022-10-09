# https://www.codewars.com/kata/58fd52b59a9f65c398000096

def min_and_max(l, d, x):
    res = [i for i in range(l, -~d) if sum(map(int,str(i))) == x]
    return [min(res), max(res)]
    
    
