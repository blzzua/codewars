# https://www.codewars.com/kata/64b779a194167920ebfbdd2e

def len_longest_chain(pairs):
    pairs = sorted(pairs, key=lambda p: p[1])
    res = [pairs[0]]
    for p1, p2 in pairs[1:]:
        if p1 > res[-1][1]:
            res.append([p1, p2]) 
    return len(res)
