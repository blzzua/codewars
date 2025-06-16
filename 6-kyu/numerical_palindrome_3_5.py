# https://www.codewars.com/kata/58e2708f9bd67fee17000080

# from more_itertools import substrings
def substrings(iterable):
    seq = []
    for item in iter(iterable):
        seq.append(item)
        # yield (item,)
    seq = tuple(seq)
    item_count = len(seq)
    for n in range(2, item_count + 1):
        for i in range(item_count - n + 1):
            if seq[i] != '0':
                yield seq[i : i + n]

def palindrome(num):
    if not isinstance(num, int):
        return "Not valid"
    if num <= 0:
        return "Not valid"
       
    res = []
    
    for comb in substrings(str(num)):
        if comb == comb[::-1]:
            res.append(int(''.join(comb)))
    if res:
        return sorted(set(res))
    else:
        return 'No palindromes found'
