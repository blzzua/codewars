# https://www.codewars.com/kata/65006177f534f65b2594df05

def rank(lst):
    slst = sorted(lst)
    result = []
    cache = {}
    for i in lst:
        if i not in cache:
            r = slst.index(i)
            a = lst.count(i)
            result.append(r + a*(a-1)/2/a)
            cache[i] = r + a*(a-1)/2/a
        else:
            result.append(cache[i])
    return result
