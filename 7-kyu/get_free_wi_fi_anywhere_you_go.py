# https://www.codewars.com/kata/64fbf7eb2b610b1a6eff0e44

def nonstop_hotspot(area):
    l, _, r =  area.partition('P')
    return (l[::-1].partition('#')[0] + r.partition('#')[0]).count('*')
