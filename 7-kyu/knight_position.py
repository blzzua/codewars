# https://www.codewars.com/kata/5b5736abf1d553f844000050

def possible_positions(pos):
    l_map = {n: i for i, n in enumerate('abcdefgh',1)}
    x = l_map.get(pos[0])
    y = int(pos[1])
    d_pos = [i for i in range(-2,3) if i]
    res = []
    for dx in d_pos:
        for dy in d_pos:
            if abs(dx) != abs(dy) and 1 <= dx + x <= 8 and 1 <= dy + y <= 8:
                res.append( (dx + x, dy + y) )
    return [' abcdefgh'[x]+str(y)  for x, y in res]
