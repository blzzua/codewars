# https://www.codewars.com/kata/5ac95cb05624bac42e000005

def bucketize(*arr):
    cnt = {}
    for i, val in enumerate(arr):
        if val not in cnt:
            cnt[val] = 0
        cnt[val] += 1
    res = [None] * (len(arr)+1)
    for key,val in cnt.items():
        if res[val] is None:
            res[val] = [key]
        else:
            res[val].append(key)
    for subres in res:
        if not(subres is None):
            subres.sort()
    return res
