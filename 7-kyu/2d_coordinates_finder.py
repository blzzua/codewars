# https://www.codewars.com/kata/639ac3ded3fb14000ed38f31

def find_coords(plane):
    res = []
    lines = plane.split('\n')[::-1]
    for _x in range(10):
        d = str(_x)
        for x, line in enumerate(lines):
            ind = line.find(d)
            if ind >=0:
                res.append( (x, (ind - x - 1 ) // 2) )
    return res

