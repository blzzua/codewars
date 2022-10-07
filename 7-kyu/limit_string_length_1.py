# https://www.codewars.com/kata/5208fc3cb613bc725f000142

def solution(st, limit): 
    if len(st) > limit:
        return st[:limit] + "..." 
    else:
        return st

