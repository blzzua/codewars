# https://www.codewars.com/kata/595e9f258b763bc2d2000032

import string

def battle(x: str, y: str) -> str:
    score = {}
    for i, c in enumerate(string.ascii_lowercase, 1):
        score[c.lower()], score[c.upper()] = i/2, i
    xc, yc = sum(map(score.get,x)), sum(map(score.get,y))
    return {xc == yc: 'Tie!', xc > yc: x,  xc < yc: y}[True]


