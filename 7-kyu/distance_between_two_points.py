# https://www.codewars.com/kata/5a0b72484bebaefe60001867

def distance(p1, p2):
    if len(p1) != len(p2) or len(p1) * len(p2) == 0:
        return -1
    return sum((a-b)**2 for a,b in zip(p1,p2))**0.5
