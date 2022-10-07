# https://www.codewars.com/kata/58fa273ca6d84c158e000052

from math import log,ceil
def digits(n):
    return max(1,int(ceil(log(abs(n+1),10))))


