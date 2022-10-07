# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d

def solution(string, ending):
    #return string.endswith(ending)
    if len(ending) > 0:
        return string[-len(ending):] == ending 
    else: 
        return True

