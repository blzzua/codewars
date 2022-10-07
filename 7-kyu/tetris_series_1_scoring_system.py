# https://www.codewars.com/kata/5da9af1142d7910001815d32

def get_score(arr) -> int:
    scores_per_line = {0:0, 1: 40, 2: 100, 3: 300, 4: 1200}
    res = 0
    level = 0
    total_lines = 0
    for line in arr:
        level_coef = level + 1
        res += scores_per_line[line] * level_coef
        total_lines += line
        level = total_lines // 10
    return res

