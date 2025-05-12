# https://www.codewars.com/kata/595c4b480bb139b96100005c

def max_gap(a):
    return max(j-i for i, j in zip(a,a[1:]))
    
def min_max_gap(arr):
    res = arr[-1] - arr[0]
    for i in range(1, len(arr)-1):
        a = arr[:]
        a.pop(i)
        gap = max_gap(a) 
        if res > gap:
            res = gap
    return res

