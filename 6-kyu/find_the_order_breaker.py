# https://www.codewars.com/kata/5fc2a4b9bb2de30012c49609

def order_breaker(input):
    for j in range(len(input)):
        cand = input[:]
        cand.pop(j)
        if all( b-a > 0 for a,b in zip(cand, cand[1:])):
            return input[j]
