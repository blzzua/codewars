# https://www.codewars.com/kata/51edd51599a189fe7f000015

def solution(array_a, array_b):
    return sum((a-b)**2 for a,b in zip(array_a, array_b))/ len(array_a)
