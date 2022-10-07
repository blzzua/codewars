# https://www.codewars.com/kata/5668e3800636a6cd6a000018

def ghostbusters(building):
    res = building.replace(' ', '')
    if building == res:
        return "You just wanted my autograph didn't you?"
    else: 
        return res

