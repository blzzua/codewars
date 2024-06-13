# https://www.codewars.com/kata/5226eb40316b56c8d500030f

def pascals_triangle(p):
    line = [1]
    res  =  [1]
    for i in range(1, p):
        line = [1] + [a + b for a,b in zip(line,line[1:])] + [1]
        res.extend(line)
    return res

# math.comb
return [math.comb(a, b) for a in range(p) for b in range(a + 1)]
