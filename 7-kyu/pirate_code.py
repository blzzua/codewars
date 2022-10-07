# https://www.codewars.com/kata/59e77930233243a7b7000026

def amaro_plan(pirate_num):
    return [pirate_num * 20 - (pirate_num - 1) // 2] + [i % 2 for i in range(pirate_num - 1)]
        

