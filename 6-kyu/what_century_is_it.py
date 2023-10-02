# https://www.codewars.com/kata/52fb87703c1351ebd200081f

def what_century(year):
    cent, yy = int(year[:2]), year[2:]
    if yy != '00':
        cent += 1
    if cent in (11, 12, 13):
        ends = 'th'
    else:
        ends = {1:'st', 2:'nd', 3:'rd'}.get(cent%10, 'th')
    return f'{cent}{ends}'
