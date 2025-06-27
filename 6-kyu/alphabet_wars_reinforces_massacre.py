# https://www.codewars.com/kata/593e2077edf0d3e2d500002d

def make_strike(bf, strike):
    if len(strike) < len(bf):
        strike = strike + ' ' * (len(bf) - len(strike))
    for i, val in enumerate(strike):
        l = max(i-1,0); r = min(len(strike) - 1, i+1)
        if strike[l] == '*' or strike[i] == '*' or strike[r] == '*':
            bf[i] = '_'

def make_reinforce(bf, reinforces):
    for ri, reinforce in enumerate(reinforces):
        for i, (b,r) in enumerate(zip(bf, reinforce)):
            if b == '_' and r != '_':
                bf[i] = r
                reinforces[ri][i] = '_'

def alphabet_war(reinforces, airstrikes):
    bf = list(reinforces.pop(0)) # battlefield
    reinforces = [list(r) for r in  reinforces]
    for strike in airstrikes:
        make_strike(bf, strike)
        make_reinforce(bf, reinforces)
    return ''.join(bf)

