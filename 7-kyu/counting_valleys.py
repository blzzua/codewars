# https://www.codewars.com/kata/5da9973d06119a000e604cb6

def counting_valleys(s): 
    change = {'U': 1,'F': 0, 'D': -1}
    level = 0
    valleys = 0
    in_valley = False
    for c in s:
        level += change.get(c)
        if level < 0:
            in_valley = True
        if level == 0 and in_valley:
            valleys += 1
            in_valley = False
    return valleys

