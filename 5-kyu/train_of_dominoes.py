# https://www.codewars.com/kata/5c356d3977bd7254d7191403

def domino_train(n):
    res = []
    for i in range(n, 0, -1):
        res.append(0)
        for j in range(i, 0, -1):
            res.extend([j,i])
    res.extend([0,0])
    return res
