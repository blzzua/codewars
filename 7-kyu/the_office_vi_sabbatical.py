# https://www.codewars.com/kata/57fe50d000d05166720000b1

from collections import Counter
def sabb(s, val, happiness):
    return ['Sabbatical! Boom!','Back to your desk, boy.']\
           [val + happiness + sum(v for k, v in Counter(s).items() if k in 'sabbatical') <= 22]

