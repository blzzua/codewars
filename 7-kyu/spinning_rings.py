# https://www.codewars.com/kata/59afff65f1c8274f270020f5

def spinning_rings(inner_max, outer_max):
    i = 0
    inner, outer = 0, 0 
    while True:
        i += 1
        inner = (inner - 1) % (inner_max + 1) 
        outer = (outer + 1) % (outer_max + 1)
        if inner == outer:
            break
    return i

