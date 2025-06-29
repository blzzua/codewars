# https://www.codewars.com/kata/5886e082a836a691340000c3

from math import floor, ceil, radians, sin, cos
def rotate_rectangle(a, b):
    angle = radians(45)
    corners = [(-a/2, -b/2), (a/2, -b/2), (a/2, b/2), (-a/2, b/2)]
    rotated_corners = []
    for x, y in corners:
        x_rot = x * cos(angle) - y * sin(angle)
        y_rot = x * sin(angle) + y * cos(angle)
        rotated_corners.append((x_rot, y_rot,))
    return rotated_corners

def intersect_x(x, x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    xm = (x1+x2)/2
    ym = (y1+y2)/2
    b = ym - slope * xm
    return slope * x  + b

def rectangle_rotation(a, b):
    down, right, up, left =  rotate_rectangle(a, b)
    min_x = int(min(coord[0] for coord in (left, down, right, up ))) - 1
    res = 0
    for x in range(min_x, -min_x+1):
        lu = intersect_x(x, *left, *up)
        ld = intersect_x(x, *left, *down)
        ru = intersect_x(x, *right, *up)
        rd = intersect_x(x, *right, *down)
        scan_dn = max(ld, rd)
        scan_up = min(lu, ru)
        scan_points = 0 if ceil(scan_dn) > floor(scan_up) else floor(scan_up) - ceil(scan_dn) + 1  
        res += scan_points
    return res

