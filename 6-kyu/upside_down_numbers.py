# https://www.codewars.com/kata/59f7597716049833200001eb

rotatemap = {'1': '1','6':'9', '8':'8', '9':'6', '0': '0'}
upsidedown_numpers = []
for i in range(130_000):
    s = str(i)
    if any(char not in rotatemap for char in s):
        continue
    else:
        if s == ''.join(map(rotatemap.get, s[::-1])):
            upsidedown_numpers.append(i)
            
def solve(a, b):
    return sum([a <= x < b for x in upsidedown_numpers])
