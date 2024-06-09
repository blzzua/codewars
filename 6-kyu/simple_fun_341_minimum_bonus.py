# https://www.codewars.com/kata/595ef0c7458ad5facc000019

def calc_bonus(scores, res):
    for i, cur in enumerate(scores[1:-1], 1):
        prev = scores[i-1]
        next = scores[i+1]
        if cur < prev and cur < next:
            res[i] = 1
        else:
            if cur > prev:
                res[i] = max(res[i], res[i-1] + 1)
            elif cur > next:
                res[i] = max(res[i], res[i+1] + 1)
    
def minimum_bonus(scores):
    res = [1] * len(scores)
    calc_bonus(scores, res) # calc middle bonus (left to right)
    scores = scores[::-1]
    res = res[::-1]
    calc_bonus(scores, res) # calc middle bonus (right to left)
    scores = scores[::-1]
    res = res[::-1]

    if scores[0] > scores[1]:  # calc bonus on edges
        res[0] = res[1] + 1 
    if scores[-1] > scores[-2]:
        res[-1] = res[-2] + 1 

    return sum(res)
