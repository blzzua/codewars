# https://www.codewars.com/kata/57ed30dde7728215300005fa

def bumps(road):
    return ["Woohoo!","Car Dead"][sum(r == "n" for r in road)>15]


