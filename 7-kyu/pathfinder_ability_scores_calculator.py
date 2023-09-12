# https://www.codewars.com/kata/5df0041acec189002d06101f

sc_map = {7: -4, 8: -2, 9: -1, 10: 0, 11: 1, 12: 2, 13: 3, 14: 5, 15: 7, 16: 10, 17: 13, 18: 17}
SOME_BIG_NUM = 9999
def pathfinder_scores(scores):
    return sum(sc_map.get(i, SOME_BIG_NUM) for i in scores) <= 25
