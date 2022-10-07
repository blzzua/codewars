# https://www.codewars.com/kata/5aa1bcda373c2eb596000112

def max_tri_sum(numbers):
    return sum(sorted(set(numbers),reverse=True)[0:3])
    

