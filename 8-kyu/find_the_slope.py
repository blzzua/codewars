# https://www.codewars.com/kata/55a75e2d0803fea18f00009d

def find_slope(points):
    try:
        return str((points[3]-points[1])//(points[2]-points[0]))
    except ZeroDivisionError:
        return "undefined"

