# https://www.codewars.com/kata/59f4a0acbee84576800000af

from itertools import combinations
def pos_average(s):
    cnt = 0
    numbers = s.split(', ')
    for pair in combinations(numbers, 2):
        for a, b in zip(*pair):
            if a == b: 
                cnt+= 1
                
    return cnt / (len(numbers) * (len(numbers) - 1) // 2 * len(numbers[0])) * 100

