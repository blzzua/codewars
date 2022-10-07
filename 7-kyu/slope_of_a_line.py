# https://www.codewars.com/kata/53222010db0eea35ad000001

def get_slope(p1, p2):
    d = [p2[0] - p1[0] , p2[1] - p1[1]]
    if d == [0, 0] or d[0] == 0:
        return None
    else:
        return d[1]/d[0]

