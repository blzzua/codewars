# https://www.codewars.com/kata/64fbfa3518692c2ed0ebbaa2

def diving_minigame(lst):
    breath = 10
    for i in lst:
        if i < 0:
            breath -= 2
        else:
            breath = min(10, breath + 4)
        if breath <= 0:
            return False
    return True
