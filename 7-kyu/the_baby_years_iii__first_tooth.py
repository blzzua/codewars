# https://www.codewars.com/kata/5bcac5a01cbff756e900003e

def first_tooth(array):
    t = [2*y-x-z for x,y,z in zip([array[0]]+array, array, array[1:]+[array[-1]])]
    c = max(t)
    if t.count(c) == 1:
        return t.index(c) 
    else:
        return -1


