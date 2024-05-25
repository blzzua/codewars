# https://www.codewars.com/kata/55031bba8cba40ada90011c4

import re

def is_sum_of_cubes(s):
    nums = re.findall('\d{1,3}', s)
    res = []
    for str_i in nums:
        i = int(str_i)
        if sum(int(j)**3 for j in str_i) == int(i):
            res.append(i)
    if res:
        return ' '.join(map(str,res +[sum(res)])) + ' Lucky'
    else:
        return "Unlucky"
