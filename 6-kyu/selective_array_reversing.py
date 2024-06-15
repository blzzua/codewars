# https://www.codewars.com/kata/58f6000bc0ec6451960000fd

from itertools import islice
def batched(iterable, n):
    # almost from itertools import batched
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        yield batch
        
def sel_reverse(arr,l):
    if l == 0:
        return arr
    res = []
    for batch in batched(arr,l):
        res.extend(sorted(batch, reverse=True))
    return res

