# https://www.codewars.com/kata/574c5075d27783851800169e

def animals(heads, legs):
    chickens = heads * 2 - legs / 2
    cows = heads - chickens
    if any((chickens != int(chickens), chickens < 0, cows < 0 )):
        return "No solutions"
    return (chickens, cows)

