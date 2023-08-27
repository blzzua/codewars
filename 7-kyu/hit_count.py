# https://www.codewars.com/kata/57b6f850a6fdc76523001162

def counter_effect(hit_count):
    return [[j for j in range(int(i)+1)] for i in hit_count]
