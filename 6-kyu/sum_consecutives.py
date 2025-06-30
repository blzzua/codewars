# https://www.codewars.com/kata/55eeddff3f64c954c2000059

# my ugly solution
def sum_consecutives(lst):
    prev = None
    subsum = 0
    res = []
    for i in lst:
        if i == prev:
            subsum += i
            prev = i
        else:
            if prev != None:
                res.append(subsum)
            subsum = i
            prev = i
    if prev == i:
        res.append(subsum)
    return res

#  best practices work with res list.
def sum_consecutives(s):
    prev = None
    res = []
    for i in lst:
        if i == prev:
            res[-1] += i
        else:
            res.append(i)
        prev = i
    return res

# clever itertoools.groupby
[sum(group) for _, group in itertoools.groupby(lst)]
