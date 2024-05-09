# https://www.codewars.com/kata/5947d86e07693bcf000000c4

def puzzle_tiles(width, height):
    n = width + 1
    head = '  ' + '_( )__'.join([' '] * (n))[:-1]
    line1 = [
    ' ' +'     '.join(['_|'] * (n)) ,
    '   _ '.join(['(_'] * (n)) ,
    ' ' +'__( )_'.join(['|'] * (n)) ,
    ]
    line2 = [
        ' ' +'     '.join(['|_'] * (n)),
        '  ' +' _   '.join(['_)'] * (n)),
        ' ' +'__( )_'.join(['|'] * (n)) 
    ]
    lines= [line1, line2] 
    res = [head]
    for i in range(height):
        res.extend(lines[i%2])

    return '\n'.join(res)
