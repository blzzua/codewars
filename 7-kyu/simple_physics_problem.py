# https://www.codewars.com/kata/57c3eb9fd6cf0ffd68000222

def solveit(vi, vf, t):
    a = (vf-vi)/t
    d = vi*t + 0.5*a*(t**2)
    if a > 0:
        return [round(a,2), round(d,2)]
    else:
        return []
