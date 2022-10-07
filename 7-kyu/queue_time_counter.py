# https://www.codewars.com/kata/5b538734beb8654d6b00016d

def queue(queuers,pos):
    d = dict(enumerate(queuers))
    res = []
    while len(res) < sum(queuers):
        for k, v in d.items():
            if d[k] > 0:
                res.append(k)
                d[k] = d[k] - 1
    return len(res) - res[::-1].index(pos)

