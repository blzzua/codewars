# https://www.codewars.com/kata/584f7b27d8912ab46e0000d5

def find_letter(_map,letter):
    for i, line in enumerate(_map.split('\n')):
        for j, char in enumerate(line):
            if char == letter:
                return [i,j]
    return None

def distribute_gifts(_map):
    res = 0
    nonempty = _map.replace('.','').replace('\n','')
    is_santa_here = nonempty.find('s')
    if is_santa_here == -1:
        return 'Where is Santa Claus?'
    children = sorted(list(nonempty))
    sy, sx = find_letter(_map, children.pop()) # santa coords
    for c in children:
        y, x = find_letter(_map,c)
        res += (abs(sy-y) + abs(sx-x))
        sy, sx = y, x
    return res

