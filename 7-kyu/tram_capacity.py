# https://www.codewars.com/kata/5b190aa7803388ec97000054

def tram(stops, descending, onboarding):
    cur, mx = 0, 0
    for o, i, _ in zip(descending, onboarding, range(stops)):
        cur = cur - o + i
        if mx < cur:
            mx = cur
    return mx

# clever compact:
from itertools import accumulate
def tram(stops, descending, onboarding):
    return max(accumulate(i - o  for o, i, _ in zip(descending, onboarding, range(stops))))
