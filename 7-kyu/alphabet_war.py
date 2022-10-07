# https://www.codewars.com/kata/59377c53e66267c8f6000027

def alphabet_war(fight):
    power = { 'w': -4, 'p': -3, 'b': -2, 's': -1, 'm': 4, 'q': 3, 'd': 2, 'z': 1 }
    res = sum(power.get(c, 0) for c in fight)
    if res < 0:
        res = 'Left side wins!'
    elif res > 0:
        res = 'Right side wins!'
    else:
        res = 'Let\'s fight again!'
    return res

