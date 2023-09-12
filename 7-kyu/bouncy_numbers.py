# https://www.codewars.com/kata/5769a78c6f2dea72b3000027

def is_bouncy(number):
    s = str(number)
    return not (all(a<=b for a,b in zip(s,s[1:])) or all(a>=b for a,b in zip(s,s[1:])))
