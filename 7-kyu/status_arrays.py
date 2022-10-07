# https://www.codewars.com/kata/601c18c1d92283000ec86f2b

from collections import Counter

def status(nums):
    statuses = [i + sum(v for k, v in Counter(nums).items() if k < n) for i, n in enumerate(nums)]
    return [a for a,b in sorted(zip(nums, statuses), key=lambda x: x[1])]

