# https://www.codewars.com/kata/58b8cc7e8e7121740700002d

def rank_of_element(arr, i):
    c1 = c2 = 0
    val = arr[i]
    for e in arr[:i]:
        if e <= val:
            c1 += 1
    for e in arr[i+1:]:
        if e < val:
            c2 += 1
    return c1 + c2

# compact-clever sum(item <= arr[i] for item in arr[:i]) + sum(item < arr[i] for item in arr[i+1:])
