# https://www.codewars.com/kata/58d5e6c114286c8594000027

def array_manip(array):
    res = []
    for i, e in enumerate(array,1):
        right = [*filter(lambda x: x > e, array[i:])]
        if right:
            res.append(min(right))
        else:
            res.append(-1)
    return res
