# https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca

def solve(arr):
    dirs, points = [], []
    for i in arr:
        d,_,p = i.partition(' on ')
        dirs.append(d)
        points.append(p)
    points.reverse()
    rev = {'Right':'Left', 'Left':'Right'}
    dirs = [dirs[0],] + list(map(rev.get, dirs[1:][::-1]))
    return [f"{d} on {p}" for d, p in zip(dirs, points)]
