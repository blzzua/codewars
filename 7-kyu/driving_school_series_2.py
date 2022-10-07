# https://www.codewars.com/kata/589b1c15081bcbfe6700017a

def cost(mins):
    total = mins // 30 + int(mins % 30 > 5)
    return max(30, 30 + 10* (total-2))

