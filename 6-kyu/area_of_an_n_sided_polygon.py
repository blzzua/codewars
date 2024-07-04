# https://www.codewars.com/kata/5727500a20c7f837fc001869

from statistics import mean
def area_polygon(vertex):
    def s_tri(a,b,c):
        la = ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5
        lb = ((b[0] - c[0])**2 + (b[1] - c[1])**2) ** 0.5
        lc = ((a[0] - c[0])**2 + (a[1] - c[1])**2) ** 0.5
        p = (la + lb + lc)/2
        sq = (p * (p-la) * (p-lb) * (p-lc)) ** 0.5
        return sq
    x_center, y_center = [mean(c) for c in zip(*vertex)]
    res = sum(s_tri(p1, p2, (x_center, y_center )) for p1, p2 in zip(vertex, vertex[1:] + vertex[:1]))
    return round(res, 1)


# clever solution: https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates 
