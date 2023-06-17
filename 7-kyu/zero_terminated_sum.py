# https://www.codewars.com/kata/5a2d70a6f28b821ab4000004

def largest_sum(s):
    return max(sum(map(int,ss)) for ss in s.split('0')) 
