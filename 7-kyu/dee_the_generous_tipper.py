# https://www.codewars.com/kata/568c3498e48a0231d200001f

def calc_tip(p, r):
    PT = p // 10 + int(p % 10 >= 5) 
    PT += {1: 1, 0: -1, -1: -(sum(divmod(PT,2)))-1}[r]
    return max(0, PT)
