# https://www.codewars.com/kata/5d10d53a4b67bb00211ca8af

def waterbombs(fire, w):
    return sum(int(len(l)/w + 0.9) for l in fire.split('Y'))

