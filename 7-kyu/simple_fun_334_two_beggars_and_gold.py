# https://www.codewars.com/kata/59547688d8e005759e000092

def distribution_of(golds):
    n = len(golds)
    res = [0, 0]
    turn = 0
    while len(golds) > 0:
        a, b = golds[0], golds[-1]
        res[turn] += golds.pop(0 if a >= b else -1)
        turn = 1 - turn
    return res
