# https://www.codewars.com/kata/567c26df18e9b1083a000049

def last_man_standing(n):
    mans = range(1, n + 1)
    side = 1
    while len(mans) > 1:
        if side == 1:
            mans = mans[1::2] 
        else: 
            mans = mans[-2::-2][::-1]
        side = 1 - side
    return mans[0]


